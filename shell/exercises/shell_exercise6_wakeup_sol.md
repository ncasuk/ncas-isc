| [Questions](shell_exercise6_wakeup_git.md) | [Exercise list](shell_exercise_index.md) |
 
# Solution 6: Wake up

1.

        $ wc -l $(find shell/acsoe -type f) |sort -n  |tail -4| head -1
        14421 shell/acsoe/eae-97/macehead/mh970427.cn1

2.

        $ X=$(wc -l $(find shell/acsoe -type f) |sort -n  |tail -4| head -1)


3. 

        $ echo $X
        14421 shell/acsoe/eae-97/macehead/mh970427.cn1


 

 