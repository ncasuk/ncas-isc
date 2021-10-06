| [Questions](shell_exercise8_ssh.md) | [Exercise list](shell_exercise_index.md) |

# Solution 8: SSH

1.  
2.	
3.	
4.	Logout (use exit or ^D)
5.	Use scp to copy some files to `/tmp` on the remote computer. 
6.	Login again and list the files you copied. 
7.	Logout
8.	Use ssh to run `df /tmp` on the remote computer.

1. cd to `/tmp` and make a file `touch <username>.txt`

        $ cd /tmp
        $ touch spepler.txt
        $ ls -l spepler.txt 
        -rw-r--r-- 1 spepler badcint 0 Oct  6 12:28 spepler.txt

2. ssh to `<username>@sci2.jasmin.ac.uk`. 

        $ ssh spepler@sci2.jasmin.ac.uk

                    Access to this system is monitored and restricted to
                    authorised users.   If you do not have authorisation
                    to use  this system,  you should not  proceed beyond
                    this point and should disconnect immediately.

                    Unauthorised use could lead to prosecution.

            (See also - http://www.stfc.ac.uk/aup)

        Last login: Wed Oct  6 12:28:08 2021 from sci1.jasmin.ac.uk

        Welcome to JASMIN.

            Administered by STFC RAL SCD Research Infrastructure Group.

            Admin contact:       JASMIN SCD <jc-support@stfc.ac.uk>

        Additional information about JASMIN can be found at: http://jasmin.ac.uk

        For support please contact JASMIN Helpdesk: support@jasmin.ac.uk

        Admin contact:    JASMIN Support <jc-support@stfc.ac.uk>

        ***************************************************************
        ** JASMIN Shared VM status at 2021-10-06 12:25:01.882342     **
        ***************************************************************

        Average load on each VM over the last hour:
        ===============================================================
        Host                                    Users  Free memory  CPU
        ---------------------------------------------------------------
        sci1.jasmin.ac.uk                          23     16.3G   19.0%
        sci2.jasmin.ac.uk                          13     24.2G    4.0%
        sci3.jasmin.ac.uk                          45    838.4G   28.0%
        sci4.jasmin.ac.uk                          11     24.8G   29.0%
        sci5.jasmin.ac.uk                          12     19.5G   35.0%
        sci6.jasmin.ac.uk                          38    988.9G   20.0%
        sci8.jasmin.ac.uk                          16    278.2G   61.0%
        ===============================================================

3. This computer shares the same home directory as `sci1.jasmin.ac.uk` but not `/tmp`.  Use ls, pwd and other commands to prove to yourself it’s the same home directory. Then change directory to `/tmp`. The `<username>.txt` will not be there as it is a different computer.

        spepler@sci2>> $ pwd
        /home/users/spepler
        spepler@sci2>> $ ls
        aria2-1.34.0                       Music
        aria2-1.34.0.tar                   nacs_talk_2021.ipynb
        bcron                              nla
        bcron.old                          nla_client
        crontamer.py                       obstore_sync
        csum                               outputs
        csum_old                           out.txt

        $ cd /tmp
        $ ls -l spepler.txt
        ls: cannot access spepler.txt: No such file or directory

4. Logout (use exit or ^D)

        spepler@sci2>> $ logout
        Connection to sci2.jasmin.ac.uk closed.

5. Use scp to copy some files to `/tmp` on the remote computer.

        $ scp ~/extract-era-data.sh spepler@sci2.jasmin.ac.uk:/tmp

                    Access to this system is monitored and restricted to
                    authorised users.   If you do not have authorisation
                    to use  this system,  you should not  proceed beyond
                    this point and should disconnect immediately.

                    Unauthorised use could lead to prosecution.

            (See also - http://www.stfc.ac.uk/aup)

        extract-era-data.sh                           100%  520   209.9KB/s   00:00    

6. Login again and list the files you copied. 

        $ ssh spepler@sci2.jasmin.ac.uk

                    Access to this system is monitored and restricted to
                    authorised users.   If you do not have authorisation
        ...
        sci6.jasmin.ac.uk                          38    987.6G   21.0%
        sci8.jasmin.ac.uk                          16    276.7G   64.0%
        ===============================================================

        spepler@sci2>> $ cd /tmp
        spepler@sci2>> $ ls -l extract-era-data.sh 
        -rw-r--r-- 1 spepler badcint 520 Oct  6 12:30 extract-era-data.sh

7. 

        spepler@sci2>> $ logout
        Connection to sci2.jasmin.ac.uk closed.

8. Use ssh to run `df /tmp` on the remote computer.

        $ ssh spepler@sci2.jasmin.ac.uk 'df /tmp'

                    Access to this system is monitored and restricted to
                    authorised users.   If you do not have authorisation
                    to use  this system,  you should not  proceed beyond
                    this point and should disconnect immediately.

                    Unauthorised use could lead to prosecution.

            (See also - http://www.stfc.ac.uk/aup)

        Filesystem     1K-blocks  Used Available Use% Mounted on
        /dev/sda5        3997376 70336   3700944   2% /tmp

  For comparision `df` on sci1.
  
        $ df /tmp
        Filesystem     1K-blocks    Used Available Use% Mounted on
        /dev/sda5        3997376 1169952   2601328  32% /tmp