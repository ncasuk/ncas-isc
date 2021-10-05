

# Exercise 1: Exploring the file system

## Aim
Login and look at some files. 

## Issues covered
Commands: `pwd`, `ls`, `gedit`, `cd`, `cp`, `mv`, `mkdir`, `rm`, `rmdir`, `man`. What’s in  `/tmp`, `/` and `/etc`

## Instructions

1. Let's get started by logging in. 
   - Login to the laptop (you should have a username and password).
   - Start a terminal window.

2. Have a look around your home directory.  Try the following commands.

        pwd
        ls 
        ls -l
        ls -a
        ls ..
        ls shell

    [Solutions](shell_exercise_files_sol.md#ex2)        

3. Let’s have a look somewhere else. Change directory to `acsoe`. 

        cd ncas-isc/shell/acsoe

     Now repeat (2)

4. Manipulating some files and directories.

    - Make a file called "myfile" in "/tmp" with gedit.
    - Make a subdirectory in "/tmp" called "mydir"
    - Rename the file "myfile.txt" and the subdirectory "X"
    - Copy "myfile.txt" into the "X" subdirectory
    - Tidy up - delete the file and subdirectory

    Use the `man ls` command to find other listing options. Experiment… have a look in `/`, and `/etc`.

5. How not to do it:
    Use `cd` with no arguments to jump back to your home directory.
    Go into the `pain` directory
    Use `ls` to see what files are here
    Move them to more sensible names (if you can).

