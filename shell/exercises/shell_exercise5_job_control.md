| [Solutions](shell_exercise5_job_control_sol.md) | [Exercise list](shell_exercise_index.md) |

# Exercise 5: Job control

## Aim
Start and stop a sleep job. Confidence in starting and stopping jobs and familiarity with variables.

## Issues covered
Commands: `set`, `export`, `echo`, `ps`, `top`, `fg`, `bg`, `jobs`, `kill`, `sleep`, `time`, `&`, ^C, ^Z
Writing commands in a file to make a shell script.

## Instructions
1. Run `sleep 10`. What does it do?
2. Make a `snooze.sh` file with `nano` with the following content.

        echo feeling sleepy...
        sleep 10
        echo wake up!

    Run the script 

        $ ./snooze.sh

3. Edit the `snooze.sh` script to use a variable `X` to control the length of sleep.

        echo feeling sleepy...
        sleep $X
        echo wake up!

4. Set `X` to 40 using `export X=40` then run it again in the background using `&`. Use `ps` to see the process at work.
5. Run 3 instances of the process at once. 
    - Start 3 snooze jobs in the background.
    - Use the jobs command to see the processes. 
    - Kill 2 of them while they sleep. 
    - Bring the last one to the foreground and let it complete.

6. Run 3 instances of the process.
    - Start 2 snooze jobs in the background with `&`.
    - Start another in the foreground.
    - Use ^Z to stop the foreground job. 
    - Use bg to put the that job in the background.
    - Bring `%1` to the foreground with the `fg` command.
    - Kill that job with ^C.
    - Let the other jobs finish. 

7. Find the difference between `" "` and `' '`. Make a shell variable `Y` set to text of your choice. Use echo to print the variable. Try the following

        $ echo * $Y
        $ echo '* $Y' 
        $ echo "* $Y"

