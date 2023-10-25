"""Check and compile the python-basics notebooks.

For the basics course, this script will:
* Run all the "answers" notebooks to check they still run.
* Process the "answers" notebooks into "exercies" notebooks,
by removing cells from the "answers" notebooks which are tagged
"clear_answer_cell" or "remove_answer_cell".
* Overwrite and replace the existing exercies notebooks with the above.

"""
import argparse
import os
import pathlib
import shutil

import nbconvert
import nbformat
import traitlets
import traitlets.config


class TagClearPreprocessor(nbconvert.preprocessors.Preprocessor):
    """NBConvert preprocessor to clear notebook cells."""

    clear_cell_tags = traitlets.Set(
        traitlets.Unicode(),
        default_value=[],
        help="Tags indicating which cells are to be cleared.",
    ).tag(config=True)

    def preprocess_cell(self, cell, resources, cell_index):
        if self.clear_cell_tags.intersection(cell.get("metadata", {}).get("tags", {})):
            cell.source = ""
            cell.outputs = []
        return cell, resources


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "base_folder",
        help="Folder which contains subfolders for worksheets and exercises.",
    )
    parser.add_argument(
        "--rewrite-answers",
        action="store_true",
        help="Should the solutions be written back after they are run?",
    )
    parser.add_argument(
        "--rewrite-exercies",
        action="store_true",
        help="Should the exercieses be removed and regenerated from the answer sheets?",
    )
    parser.add_argument(
        "--kernel-name",
        default="jaspy",
        help="The jupyter kernel the notebooks will be run with.",
    )
    args = parser.parse_args()

    # setup nbconvert
    config = traitlets.config.Config()
    config.TagRemovePreprocessor.remove_cell_tags = "remove_answer_cell"
    config.TagRemovePreprocessor.enabled = True
    config.TagClearPreprocessor.clear_cell_tags = "clear_answer_cell"
    config.TagClearPreprocessor.enabled = True

    tag_remover = nbconvert.preprocessors.TagRemovePreprocessor(config=config)
    tag_clearer = TagClearPreprocessor(config=config)

    # setup paths
    root_folder = pathlib.Path(args.base_folder)
    answers_folder = root_folder / "solutions"
    questions_folder = root_folder / "exercises"

    # Find all the notebooks.
    all_answer_notebooks = list(
        set(answers_folder.glob("*.ipynb")) | set(answers_folder.glob("**/*.ipynb"))
    )
    all_answer_notebooks = [
        x for x in all_answer_notebooks if "ipynb_checkpoints" not in str(x)
    ]

    # save our working directory so we can go back.
    workdir = os.getcwd()

    # Execute all the notebooks in the answers folder.
    for nb_path in all_answer_notebooks:
        # Change to notebook location so that relative file loads work.
        os.chdir(nb_path.parent)
        with open(nb_path, "r+", encoding="utf-8") as f:
            try:
                nb = nbformat.read(f, as_version=nbformat.current_nbformat)
            except nbformat.reader.NotJSONError:
                print(f"{nb} was not successfully parsed.")
            else:
                executor = nbconvert.preprocessors.ExecutePreprocessor(
                    timeout=600, kernel_name=args.kernel_name, allow_errors=True
                )
                result = executor.preprocess(nb)

                # Check the processed result for unexpected errors.
                # We have to do this so we can allow errors where appropriate.
                for node in result:
                    for cell in node.get("cells", []):
                        tags = cell.get("metadata", {}).get("tags", [])
                        if cell["cell_type"] == "code" and "allow_errors" not in tags:
                            for output in cell["outputs"]:
                                if output["output_type"] == "error":
                                    raise Exception(
                                        f"Error processing {nb_path}. A cell not tagged with `allow_errors` raised an error in {nb_path}."
                                    ) from nbconvert.preprocessors.CellExecutionError.from_cell_and_msg(
                                        cell=cell, msg={}
                                    )
                if args.rewrite_answers:
                    # Write-out the executed version to answers.
                    f.seek(0)
                    f.truncate()
                    nbformat.write(nb, f)
                del executor
    # Go back to previous workdir.
    os.chdir(workdir)

    # Create "worksheet" notebooks by
    # removing cells tagged as answer from the answers.
    if args.rewrite_exercises:
        # Clean up the worksheets folder.
        shutil.rmtree(questions_folder)
        questions_folder.mkdir()
        # Loop through and process each answer notebook into a question notebook
        for nb in all_answer_notebooks:
            # Get the path for the worksheet.
            rel_path = nb.relative_to(answers_folder)
            new_path = questions_folder / rel_path
            new_path.parent.mkdir(exist_ok=True, parents=True)

            # Load the answer sheet.
            with open(nb, "r", encoding="utf-8") as f:
                try:
                    nb = nbformat.read(f, as_version=nbformat.current_nbformat)
                except nbformat.reader.NotJSONError:
                    continue

            # Remove tagged cells and write back.
            tag_remover.preprocess(nb, resources={})
            tag_clearer.preprocess(nb, resources={})

            with open(new_path, "w", encoding="utf-8") as f:
                nbformat.write(nb, f)


if __name__ == "__main__":
    main()
