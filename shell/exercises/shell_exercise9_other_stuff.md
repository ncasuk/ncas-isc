| [Exercise list](shell_exercise_index.md) |

 
# Other stuff to try out.

## Aim
Find out about some other useful stuff.

### Xargs

1. Use `find` piped to `xargs` to do something (`wc`, `ls –l` , `head -1`, etc). For example try this:

        $ find acsoe  -type f  -name "ab*" | xargs ls -l
        
### Wget and curl

1. Have a look here: https://dap.ceda.ac.uk/badc/cira/data/ 
2. Grab the `nht.lsn` file using curl. `curl https://dap.ceda.ac.uk/badc/cira/data//nht.lsn`
3. Try this wget command: `wget -e robots=off --mirror --no-parent -r https://dap.ceda.ac.uk/badc/cira/data/`. Look for the dap.ceda.ac.uk directory for the results.

### Copying data

1. Copy the data in the `acsoe` directory to an `acsoe2` directory with `rsync`. Use the `–v` verbose option so you can see what is happening.
2. Run the command again and note what is copied.
3. Add a new file to the `acsoe` directory, modify another file and delete a third. Run the command a third time. 
4. Try `rsync` to the remote machine used in the `scp` exercise. 

### Globbing

1. Use glob matching in `acsoe/freetex-98/Jungfrau` to match files for dates from `980323` to `980327`
2. Make a for loop that word counts only files from that date range. 

### Getting out of text editors

We have been using `nano`. There are a couple of other common editors that use the terminal window. 
The default editor used by some commands means you need to know how to get out of them sometimes and 
it's not obvious how.  If you are not used to them you can get stuck.

1. `emacs` – get out with with ^X followed by ^C 

        $ emacs test.txt
    
    Then try to exit.

2. `vi` – get out with : followed by q. 

        $ vi test.txt

    Then try to exit.

### `/dev/null`

1. Try this:

        $ head -1 `find acsoe/freetex-98 -type f` 

    Find the errors printed to the screen if you can. There will be too much output to notice the errors. 

2. Try this instead to dump the output and just make the errors visible:

        $ head -1 `find acsoe/freetex-98 -type f` > /dev/null

### Sourcing files

1. Make a script file that sets a variable

        $ nano myscript.sh
        $ cat myscript.sh
        Z=Dino 

2. Run the script and then use `echo` to look at the `Z` variable. 

        $ chmod u+x m.sh 
        $ ./m.sh 
        $ echo $X

        $

    Does not set X in the current shell.

3. Try again but this time use the `source` command

        $ source ./myscript

    This is called sourcing a file.  It runs the commands in the files as if you had typed them in at the command line. 
    This means the commands are executed in the current shell instead of starting a new one. 
    
4. Use `echo` to see the set variable. 

        $ echo $X
        Dino

### Tar and Gzip

1. Make a tar file

        $ tar cvf macehead.tar acsoe/lterm/macehead

2. Compress is with `gzip`

        $ gzip macehead.tar 

3. Move the file to `/tmp`

4. Uncompress it with `gunzip`

5. Untar it with 


