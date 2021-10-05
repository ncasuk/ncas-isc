<!-- JavaScript Bundle with Popper -->
<head>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
</head>
<body>
  <div class="container">

 
<h1>Exercise 7: Shell scripts</h1>
<a class="btn">test</a>
<h2>AIM</h2>
<p>Use a shell script to look at output and error redirection.</p>
<h2>Issues covered</h2>
<code> >, >>, >>, which, tail, for</code> loops. Interpreter header lines.

<h2>Instructions</h2>

<ol>
<li>Go into "acsoe/eae-97/macehead". This is a directory containing only files and no subdirectories.</li>
<li>Make a shell script that loops over the files in a directory printing the last line in each file. Redirect the output to a file.</li>
  <li>Make a subdirectory to trigger an error message from the tail command. Append this to an error log. Run the command a few times. </li>
    <li>Make sure your script is only executable by you and it has the right #! first line. </li>
      <li>Use which to find the python interpreter. Try changing the first line to point to that interpreter instead. What happens now when you run it?</li>
    </ol>
 

<h2>Solution 7: Shell scripts</h2>
1-4.
<pre>$ cat ./my.sh
#!/bin/bash

for i in *
do
tail -1 $i
done
</pre>

<pre>
$ ./my.sh > output.txt
$ cat output.txt
150.9375	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999	-999
150.593	150.349	150.838	208.8	287	88.43	204	5.6
150.592    150.351  150.832   15.938          92.504            41.925          15.106            42.969          123.124         2.592      111.401      1.188       12.862       2.393       7.397        112.808     61.752
150.592    150.351       150.832   77.378          31.374       52.149       20.287       354.200     228.634    0.000       2.486       23.683      6.034       36.593       73.681
147.10     146.85      147.35      14.3            2.17E-07        1.85E-07        7.78E-07        9.36E-08       1.63E-08       3.09E-08
147.10     146.85      147.35      14.3            1.27E-03        7.67E-05        9.77E-05        1.57E-03       7.78E-05       1.90E-04          2.77E-05
done
done
$ 
</pre>


5.
<pre>
$ which python
/usr/bin/python
$ emacs my.sh
$ ./my.sh 
  File "./my.sh", line 3
    for i in *
             ^
SyntaxError: invalid syntax 
</pre>



</div>
</body>
