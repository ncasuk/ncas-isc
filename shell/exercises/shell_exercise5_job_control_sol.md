| [Questions](shell_exercise5_job_control.md) | [Exercise list](shell_exercise_index.md) |



    
# Solution 5: Job control

1.

        $ sleep 10

2.

      $ gedit snooze.sh
      $ ./snooze.sh
      -bash: ./snooze.sh: Permission denied
      $ chmod 755 snooze.sh 
      $ ./snooze.sh
      Feeling sleepy...
      Wake up!

3.
workshop_shell$ gedit snooze.sh
workshop_shell$ cat snooze.sh 
echo Feeling sleepy...
sleep $X 
echo Wake up!

workshop_shell$ export X=5
workshop_shell$ ./snooze.sh 
Feeling sleepy...
Wake up!
4.
workshop_shell$ export X=40
workshop_shell$ ./snooze.sh &
[1] 3509
workshop_shell$ Feeling sleepy...

workshop_shell$ ps
  PID TTY           TIME CMD
  612 ttys000    0:00.58 -bash
 3509 ttys000    0:00.00 -bash
 3510 ttys000    0:00.00 sleep 40
workshop_shell$ 
workshop_shell$ Wake up!

[1]+  Done                    ./snooze.sh
workshop_shell$ 
5.
workshop_shell$ ./snooze.sh &
[1] 3550
workshop_shell$ Feeling sleepy...
workshop_shell$ ./snooze.sh &
[2] 3552
workshop_shell$ Feeling sleepy...
./snooze.sh &
[3] 3554
workshop_shell$ Feeling sleepy...

workshop_shell$ jobs
[1]   Running                 ./snooze.sh &
[2]-  Running                 ./snooze.sh &
[3]+  Running                 ./snooze.sh &
workshop_shell$ kill %1
workshop_shell$ 
[1]   Terminated: 15          ./snooze.sh
workshop_shell$ kill %2
[2]-  Terminated: 15          ./snooze.sh
workshop_shell$ 
workshop_shell$ fg %3
./snooze.sh
Wake up!
workshop_shell$ 
6.
workshop_shell$ ./snooze.sh  &
[1] 11411
workshop_shell$ Feeling sleepy...

workshop_shell$ ./snooze.sh  &
[2] 11413
workshop_shell$ Feeling sleepy...
./snooze.sh 
Feeling sleepy...
^Z
[3]+  Stopped                 ./snooze.sh
workshop_shell$ bg
[3]+ ./snooze.sh &
workshop_shell$ fg %1
./snooze.sh
^Cworkshop_shell$ 
workshop_shell$ Wake up!
Wake up!

[2]-  Done                    ./snooze.sh
[3]+  Done                    ./snooze.sh




