
| [Questions](shell_exercise1_files.md) | [Exercise list](shell_exercise_index.md) |

# Exercise 1 Solutions: Exploring the file system

[2](#ex2)

    $ pwd
    /Users/sjp23/play/workshop_shell
    $ ls
    acsoe
    $ ls -l
    total 0
    drwxr-x---  16 sjp23  staff  544 26 Feb 16:21 acsoe
    $ ls -a
    .	..	acsoe
    $ ls ..
    badc			dataman		workshop_shell
    $ ls acsoe
    00README	eae-96	ease-96	freetex-96	hillcloud-96	lterm
    c-130	eae-97	ease-97	freetex-98	hillcloud-97	ozprof

[3](#ex3)

    $ cd acsoe
    $ pwd
    /Users/sjp23/play/workshop_shell/acsoe

> Note my working directory is not the same as yours because you are on a different computer. 

    $ ls
    00README	eae-96	ease-96	freetex-96	hillcloud-96	lterm
    c-130	eae-97	ease-97	freetex-98	hillcloud-97	ozprof
    $ ls -l
    total 8
    -rwxr-x---  1 sjp23  staff  190 26 Feb 16:21 00README
    drwxr-x---  8 sjp23  staff  272 26 Feb 16:20 c-130
    drwxr-x---  8 sjp23  staff  272 26 Feb 16:20 eae-96
    drwxr-x---  8 sjp23  staff  272 26 Feb 16:21 eae-97
    drwxr-x---  7 sjp23  staff  238 26 Feb 16:21 ease-96
    drwxr-x---  6 sjp23  staff  204 26 Feb 16:21 ease-97
    drwxr-x---  6 sjp23  staff  204 26 Feb 16:21 freetex-96
    drwxr-x---  6 sjp23  staff  204 26 Feb 16:21 freetex-98
    drwxr-x---  8 sjp23  staff  272 26 Feb 16:21 hillcloud-96
    drwxr-x---  9 sjp23  staff  306 26 Feb 16:21 hillcloud-97
    drwxr-x---  6 sjp23  staff  204 26 Feb 16:21 lterm
    drwxr-x---  6 sjp23  staff  204 26 Feb 16:21 ozprof
    $ ls -a
    .	.summary	eae-96	ease-97	 hillcloud-96	ozprof
    ..	00README	eae-97	freetex-96 hillcloud-97	.checksums	
    c-130		ease-96	freetex-98 lterm
    $ ls ..
    acsoe


[4](#ex4)

Make a file called "myfile" in "/tmp" with gedit.

    $ cd /tmp
    $ gedit myfile
    $ ls
    myfile
    test.txt

Make a subdirectory in "/tmp" called "mydir"

    $ mkdir mydir
    $ ls -l
    total 56
    drwxr-xr-x  2 sjp23           wheel     68 26 Feb 17:14 mydir
    -rw-r--r--  1 sjp23           wheel      7 26 Feb 17:13 myfile

Rename the file "myfile.txt" and the subdirectory "X"

    $ mv myfile myfile.txt
    $ mv mydir X

Copy "myfile.txt" into the "X" subdirectory

    $ cp myfile.txt  X
    $ ls -l
    total 56
    drwxr-xr-x  3 sjp23           wheel    102 26 Feb 17:15 X
    -rw-r--r--  1 sjp23           wheel      7 26 Feb 17:13 myfile.txt
    $ ls -l X
    total 8
    -rw-r--r--  1 sjp23  wheel  7 26 Feb 17:21 myfile.txt

Tidy up - delete the file and subdirectory

    $ rm X/myfile.txt 
    $ rmdir X



Use cd with no arguments to jump back to your home directory. Go into the "pain" directory.
Use ls to see what files are here Move them to more sensible names (if you can).

    $ cd
    $ cd pain
    $ ls -l
    total 0
    -rw-r--r--  1 sjp23  staff  0 20 Mar 12:48 -l
    -rw-r--r--  1 sjp23  staff  0 20 Mar 12:49 What the $
    -rw-r--r--  1 sjp23  staff  0 20 Mar 12:53 Ω
    $ mv -l  L
    $ mv What\ the\ \$ What_the_dollar
    $ mv ? omega
    $ ls -l
    total 0
    -rw-r--r--  1 sjp23  staff  0 20 Mar 12:48 L
    -rw-r--r--  1 sjp23  staff  0 20 Mar 12:49 What_the_dollar
    -rw-r--r--  1 sjp23  staff  0 20 Mar 12:53 omega  
