"""
Script to tag, for all Notebooks following a certain glob pattern
in a given directory, all code-only cells with a chosen tag - with
the main intention to tags specified solutions Notebooks with the
tag 'clear_answer_cell' ready for generating into exercises
Notebooks with the 'processor.py' script. 

You are likely to want to adapt the filename-pattern which
controls which Notebooks under the config, directory to tag.
"""

import nbformat as nbf
from glob import glob
import os


base_dir = "./solutions"  # directory of Notebooks to tag
filename_pattern = "ex04*_cf_tools_*.ipynb" # pattern of Notebook filenames to filter
tag_to_add = "clear_answer_cell" # tag to add to each code-only cell


# Build the notebook search path with filename pattern
search_path = os.path.join(base_dir, "**", filename_pattern)
notebook_paths = glob(search_path, recursive=True)

for ipath in notebook_paths:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)
    changed = False

    for cell in ntbk.cells:
        # Only modify code cells
        if cell.get("cell_type") != "code":
            continue

        cell_tags = cell.get("metadata", {}).get("tags", [])

        if tag_to_add not in cell_tags:
            cell_tags.append(tag_to_add)
            cell.setdefault("metadata", {})["tags"] = cell_tags
            changed = True

    if changed:
        nbf.write(ntbk, ipath)
        print(f"Updated: {ipath}")
    else:
        print(f"No change: {ipath}")
