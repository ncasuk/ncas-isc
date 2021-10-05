| [Solutions](shell_exercise7_scripts_sol.md) | [Exercise list](shell_exercise_index.md) |
 
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
 
