| [Questions](shell_exercise5_job_control.md) | [Exercise list](shell_exercise_index.md) |

# Solution 5: Job control

1. It will do nothing for 10 seconds.

        $ sleep 10

2. 

        $ nano snooze.sh
        $ ./snooze.sh
        -bash: ./snooze.sh: Permission denied
        $ chmod 755 snooze.sh 
        $ ./snooze.sh
        Feeling sleepy...
        Wake up!

3.

        $ nedit snooze.sh
        $ cat snooze.sh 
        echo Feeling sleepy...
        sleep $X 
        echo Wake up!

        $ export X=5
        $ ./snooze.sh 
        Feeling sleepy...
        Wake up!

4.

        $ export X=40
        $ ./snooze.sh &
        [1] 3509
        $ Feeling sleepy...

        $ ps
          PID TTY           TIME CMD
          612 ttys000    0:00.58 -bash
         3509 ttys000    0:00.00 -bash
         3510 ttys000    0:00.00 sleep 40
        $ 
        $ Wake up!

        [1]+  Done                    ./snooze.sh
        $ 

5.

        $ ./snooze.sh &
        [1] 3550
        $ Feeling sleepy...
        $ ./snooze.sh &
        [2] 3552
        $ Feeling sleepy...
        ./snooze.sh &
        [3] 3554
        $ Feeling sleepy...

        $ jobs
        [1]   Running                 ./snooze.sh &
        [2]-  Running                 ./snooze.sh &
        [3]+  Running                 ./snooze.sh &
        $ kill %1
        $ 
        [1]   Terminated: 15          ./snooze.sh
        $ kill %2
        [2]-  Terminated: 15          ./snooze.sh
        $ 
        $ fg %3
        ./snooze.sh
        Wake up!
        $ 

6.

        $ ./snooze.sh  &
        [1] 11411
        $ Feeling sleepy...

        $ ./snooze.sh  &
        [2] 11413
        $ Feeling sleepy...
        ./snooze.sh 
        Feeling sleepy...
        ^Z
        [3]+  Stopped                 ./snooze.sh
        $ bg
        [3]+ ./snooze.sh &
        $ fg %1
        ./snooze.sh
        ^C$ 
        $ Wake up!
        Wake up!

        [2]-  Done                    ./snooze.sh
        [3]+  Done                    ./snooze.sh

7.

        $ Y=hello
        $ echo * $Y
        aria2-1.34.0 aria2-1.34.0.tar bcron bcron.old crontamer.py csum csum_old Desktop Documents downloader Downloads edc_reformat eumetcast_transfers extract-era-data.sh york_workshop_shell york_workshop_shell.tar.gz hello
        $ echo "* $Y"
        * hello
        $ echo '* $Y'
        * $Y

        



