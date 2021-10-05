<!-- JavaScript Bundle with Popper -->
<head>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
</head>
<body>
  <div class="container">

 
 
Other stuff


Aim: find out about some other useful stuff

Xargs
1)	Use find piped to xargs to do something (wc, ls –l , head -1, etc)

Wget
2)	Look at ftp://sparc-ftp1.ceda.ac.uk/sparc/hres/1_second/text/2011/03020/ in a web browser.
3)	Use wget to download ftp://sparc-ftp1.ceda.ac.uk/sparc/hres/1_second/text/2011/03020/03020_2011010112.tgz

Copying data
4)	Copy the data in the acsoe directory to an acsoe2 directory with rsync. Use the –v (verbose) option so you can see what is happening.
5)	Run the command again and note what is copied.
6)	Add a new file to the "acsoe" directory, modify another file and delete a third. Run the command a third time. 
7)	Try rsync to the remote machine used in the scp exercise. 

Globbing
8)	Use glob matching in "acsoe/freetex-98/Jungfrau" to match files for dates from 980323 to 980327
9)	Make a for loop that word counts only files from that date range. 

Getting out of text editors
Some editors use the terminal window. The default editor used by some commands means you need to know how to get out of them sometimes. If you are not used to them you can get stuck.

Emacs – get out with with ^X followed by ^C
<pre>$ emacs test.txt</pre>

Vi – get out with : followed by q. 

Have a go…


/dev/null

Give it a go with 
<pre>
  $ head -1 `find acsoe/freetex-98 -type f` 
</pre>
Too much output to notice the errors.
<pre>
  $ head -1 `find acsoe/freetex-98 -type f` > /dev/null
</pre>
Sourcing files

Try this:
Make a script file that sets a variable
Z=Dino 
Run the file and then use echo to look at the Z variable.
Try again but this time do this
$ ../myscript
This is called sourcing a file is runs it in the current shell instead of starting a new one.

Tar
Make a tar file
$ tar cvf macehead.tar acsoe/lterm/macehead
Compress is with gzip
$ gzip macehead.tar 
Move the file to "/tmp"
Uncompress it with gunzip

</div>
</body>
