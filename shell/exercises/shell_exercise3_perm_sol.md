<!-- JavaScript Bundle with Popper -->
<head>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    </head>
    <body>
      <div class="container">

Exercise 3: Permissions

AIM
To get comfortable with Unix permission system.
Issues covered
Commands: chmod, ls -l, more, less, chgrp
Instructions
1.  Explain permissions to other people.
a.	Change directory to "acsoe/freetex-98/Jungfrau". 
b.	Use ls –l to look at the files.
c.	Run the script "./set_chmod.sh".  This script will change the permissions on some of the files in this directory.
$ ./set_chmod.sh
d.	Use ls –l again to look at the file permissions.
e.	Pair up and describe to your partner what the permission mean.
f.	Use the more (or less) command to see if you can access the files. Try to run the files.
2. Which do you think are most sensible set of permissions.
a.	Change the files to have sensible permissions.
b.	Make a new directory
c.	Experiment with the permissions on the directory.


 
Solution 3: Permissions
1. a-d)
workshop_shell$ cd acsoe/freetex-98/Jungfrau
Jungfrau$ ls -l
total 33064
-rwxr-x---  1 sjp23  staff   183188 26 Feb 16:21 jf980314.em3
-rwxr-x---  1 sjp23  staff   291474 26 Feb 16:21 jf980315.em1
-rwxr-x---  1 sjp23  staff   200955 26 Feb 16:21 jf980315.em2
-rwxr-x---  1 sjp23  staff    31641 26 Feb 16:21 jf980317.nox
…
Jungfrau$ ./set_chmod.sh 
Jungfrau$ ls -l
total 33064
-rwx------  1 sjp23  staff   183188 26 Feb 16:21 jf980314.em3
----rwx---  1 sjp23  staff   291474 26 Feb 16:21 jf980315.em1
-------rwx  1 sjp23  staff   200955 26 Feb 16:21 jf980315.em2
-rwxrwx---  1 sjp23  staff    31641 26 Feb 16:21 jf980317.nox
…

1. f)
No user permission…
Jungfrau$ more jf980315.em2
jf980315.em2: Permission denied
Jungfrau$ more jf980315.em1
jf980315.em1: Permission denied
Read permission ok…
Jungfrau$ more jf980318.pr1
24 1001
Monks, Paul and Zanis, Prodromos
School of Chemistry, Univesrity Leicester, Leicester, UK
Peroxy Radical Chemical Amplifier II, Free Tropospheric Experiment II, Jungfraujoch, Switzerland
FREETEX '98
Execute permission ok… but not really something you can execute!
Jungfrau$ ./jf980318.fm1
./jf980318.fm1: line 1: 24: command not found
./jf980318.fm1: line 2: Graham: command not found
./jf980318.fm1: line 3: syntax error near unexpected token `('
./jf980318.fm1: line 3: `School of Environmental Sciences, University of East Anglia (UEA), Norwich, UK'

