| [Solutions](shell_exercise9_other_stuff_sol.md) | [Exercise list](shell_exercise_index.md) |

 
# Other stuff

## Aim
Find out about some other useful stuff.

### Xargs

1. Use `find` piped to `xargs` to do something (`wc`, `ls –l` , `head -1`, etc)

### Wget

2. Look at `ftp://sparc-ftp1.ceda.ac.uk/sparc/hres/1_second/text/2011/03020/` in a web browser.
3. Use `wget` to download `ftp://sparc-ftp1.ceda.ac.uk/sparc/hres/1_second/text/2011/03020/03020_2011010112.tgz`

### Copying data

4. Copy the data in the `acsoe` directory to an `acsoe2` directory with `rsync`. Use the `–v` verbose option so you can see what is happening.
5. Run the command again and note what is copied.
6. Add a new file to the `acsoe` directory, modify another file and delete a third. Run the command a third time. 
7. Try `rsync` to the remote machine used in the `scp` exercise. 

### Globbing

8. Use glob matching in `acsoe/freetex-98/Jungfrau` to match files for dates from `980323` to `980327`
9. Make a for loop that word counts only files from that date range. 

### Getting out of text editors

Some editors use the terminal window. The default editor used by some commands means you need to know how to get out of them sometimes. If you are not used to them you can get stuck.

10. Emacs – get out with with ^X followed by ^C

        $ emacs test.txt
    
    Then try to exit.

11. Vi – get out with : followed by q. 

        $ vi test.txt

    Then try to exit.

### `/dev/null`

12. Give this a go 

        $ head -1 `find acsoe/freetex-98 -type f` 

    Find the errors printed to the screen if you can. There will be too much output to notice the errors. Then try this:

        $ head -1 `find acsoe/freetex-98 -type f` > /dev/null

### Sourcing files

13. Make a script file that sets a variable

        Z=Dino 

    Run the file and then use `echo` to look at the `Z` variable. Try again but this time do this

        $ source ./myscript

    This is called sourcing a file is runs it in the current shell instead of starting a new one. Use `echo` to see 
    the set variable. 

### Tar and Gzip

14. Make a tar file

        $ tar cvf macehead.tar acsoe/lterm/macehead

    Compress is with `gzip`

        $ gzip macehead.tar 

    Move the file to `/tmp
    Uncompress it with `gunzip`


