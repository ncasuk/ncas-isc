<!-- JavaScript Bundle with Popper -->
<head>
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
   </head>
   <body>
     <div class="container">

Exercise 5: Job control

AIM
Start and stop a sleep job. Confidence in starting and stopping jobs and familiarity with variables.
Issues covered
Commands: set, export, echo, ps, top, fg, bg, jobs, kill, sleep, time, &, ^C, ^Z
Writing commands in a file to make a shell script.
Instructions
1. Run "sleep 10". What does it do?
2. Make a "snooze.sh" file with gedit with the following content.
echo feeling sleepy…
sleep 10
echo wake up!
Run the script 
$ ./snooze.sh
3. Edit the snooze.sh script to use a variable X to control the length of sleep.
4. Set X to 40 then run it again in the background using &. Use ps to see the process at work. Remember to export X.
5. Run 3 instances of the process at once. 
a.	Start 3 snooze jobs in the background.
b.	Use the jobs command to see the processes. 
c.	Kill 2 of them while they sleep. 
d.	Bring the last one to the foreground and let it complete.

6. Run 3 instances of the process.

a.	Start 2 snooze jobs in the background.
b.	Start another in the foreground.
c.	Use ^Z to stop the foreground job. 
d.	Use bg to put the job in the background.
e.	Bring %1 to the foreground with the fg command.
f.	Kill that job with ^C.
g.	Let the other jobs finish. 



7. Find the difference between " " and ' '. Make a shell variable Y set to text of your choice. Use echo to print the variable. Try the following
echo * $Y
echo '* $Y' 
echo "* $Y"

    
Solution 5: Job control

1.
workshop_shell$ sleep 10
2.
workshop_shell$ gedit snooze.sh
workshop_shell$ ./snooze.sh
-bash: ./snooze.sh: Permission denied
workshop_shell$ chmod 755 snooze.sh 
workshop_shell$ ./snooze.sh
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




