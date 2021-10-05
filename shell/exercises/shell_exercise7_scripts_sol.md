| [Questions](shell_exercise7_scripts.md) | [Exercise list](shell_exercise_index.md) |




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
