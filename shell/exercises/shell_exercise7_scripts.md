| [Solutions](shell_exercise7_scripts_sol.md) | [Exercise list](shell_exercise_index.md) |
 
# Exercise 7: Shell scripts

## Aim
Use a shell script to look at output and error redirection.

## Issues covered
`>`, `>>`, `which`, `head`, `for` loops. Interpreter header lines.

## Instructions

1. Go into `acsoe/eae-97/macehead`. This is a directory containing only files and no subdirectories. 
2. Make a shell script that loops over the files in a directory printing the first line in each file.
3. Make sure your script is only executable by you and it has the right `#!` first line. Use `which bash` to find the right interpreter. 
4. Run the script redirecting the output to a file.
5. Make a subdirectory to trigger an error message; the head command will not know what to do with a directory. 
6. Run the script again appending error messages to an error log. Run the command a few times to convince yourself that the errors are being written to the end of the log each time.
7. Use `which` to find the python interpreter. Try changing the first line to point to that interpreter instead. What happens now when you run it?
    

 
