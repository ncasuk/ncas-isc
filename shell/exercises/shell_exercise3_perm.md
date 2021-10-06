| [Solutions](shell_exercise3_perm_sol.md) | [Exercise list](shell_exercise_index.md) |

# Exercise 3: Permissions

## Aim
To get comfortable with Unix permission system.

## Issues covered
Commands: `chmod`, `ls -l`, `more`, `less`, `chgrp`

## Instructions
1.  Let's have a look at some of examples of permissions.
    1. Change directory to `acsoe/freetex-98/Jungfrau`. 
    2. Use `ls –l` to look at the files and their permissions.
    3. Run the script `./set_chmod.sh`.  This script will change the permissions on some of the files in this directory.

        $ ./set_chmod.sh

    4. Use `ls –l` again to look at the file permissions.
    5. Work out what the permissions would mean.
    6. Use the `more` (or `less`) command to see if you can access the files. Try to execute some files. e.g.

        $ ./jf980314.em3

2. Which do you think are most sensible set of permissions.
    1. Change the files to have sensible permissions.
    2. Make a new directory
    3. Experiment with the permissions on the directory.

 
