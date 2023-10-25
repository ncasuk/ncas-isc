Check and compile the python-basics notebooks.

For the basics course, this script will:
* Run all the "answers" notebooks to check they still run.
* Process the "answers" notebooks into "exercies" notebooks,
by removing cells from the "answers" notebooks which are tagged
"clear_answer_cell" or "remove_answer_cell".
* Overwrite and replace the existing exercies notebooks with the above.
