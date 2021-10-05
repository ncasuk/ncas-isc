
# Solution 2: Pipes and filters

1.
        wc -l eae-97/macehead/* | sort -n | tail -n 2 | head -n 1 | cut -c 10-

    As an alternative to the last command in the above pipeline, cut -f 2 -d ' '
    will extract the second field, using space as delimiter between fields – more robust if the character width can vary.

2.
        wc -m eae-97/macehead/* | sort -n | tail -n 2 | head -n 1 | cut -c 10-

3.
        wc -m eae-97/*/* | sort -n | tail -n 2 | head -n 1 | cut -c 10-

4.  Up and down arrows scroll through the command history of the shell (very useful for repeating the same commands). 
    The tab key makes suggestions for completing what you are typing. Often tab completion writes the rest of the 
    filename after typing in the start of it. Tab key twice lists all possible completion alternatives. 
    The history command lists the command history; use !33 to run the 33rd entry in the history list.
  