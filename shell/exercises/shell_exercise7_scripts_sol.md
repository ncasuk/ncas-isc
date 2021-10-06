| [Questions](shell_exercise7_scripts.md) | [Exercise list](shell_exercise_index.md) |


# Solution 7: Shell scripts

1.

        cd
        cd acsoe/eae-97/macehead

2. 

        $ nano my.sh
        $ cat ./my.sh
        #!/bin/bash

        for i in *
        do
        head -1 $i
        done

3. 

        $ chmod u=rwx,go= my.sh
        $ ls -l my.sh          
        -rwx------  1 sam.pepler  staff  43  6 Oct 10:33 my.sh

4. 

        $ ./my.sh > out.txt
        $ cat out.txt 
        ????JFIF??C



        ????JFIF??C



        ????JFIF??C
        ...

        28 1001
        24 1001
        24 1001
        25 1001
        35 1001
        41 1001
        24 1001
        22 1001
        24 1001
        34 1001
        32 1001
        34 1001
        22  1001
        36          1001
        20 1001
        20 1001
        23 1001 
        ...

    The output contains the last lines from some binary files so it may not make a lot of sence! 

5. 

        $ mkdir trip_hazard

6.

        $ ./my.sh > output.txt 2>> err.log
        $ ./my.sh > output.txt 2>> err.log
        $ ./my.sh > output.txt 2>> err.log
        $ cat err.log 
        head: Error reading trip_hazard
        head: Error reading trip_hazard
        head: Error reading trip_hazard

7. 

        $ emacs my.sh
        $ cat my.sh
        #!/usr/bin/python

        for i in *
        do
        head -1 $i
        done
        sam.pepler@RSMLSP1 macehead % ./my.sh
          File "./my.sh", line 3
            for i in *
                    ^
        SyntaxError: invalid syntax

