| [Solutions](shell_exercise6_wakeup_git_sol.md) | [Exercise list](shell_exercise_index.md) |

Exercise 6: Wake up

AIM
What did we do yesterday?
Issues covered
Stuff from yesterday.

Instructions

1.	Make a pipe and filter command to find the third biggest file (by number of lines) in the acsoe directory. (use find, sort tail and head) 
2.	Use $() to store the result in a variable. 
X = $(my long command with |pipes and | filters)
3.	Use echo to show the result is stored in the variable.
echo $X


 
Solution 6: Wake up



ncas-isc$ wc -l $(find shell/acsoe -type f) |sort -n  |tail -4| head -1
14421 shell/acsoe/eae-97/macehead/mh970427.cn1
ncas-isc$ X=$(wc -l $(find shell/acsoe -type f) |sort -n  |tail -4| head -1)
ncas-isc$ echo $X
14421 shell/acsoe/eae-97/macehead/mh970427.cn1


 
Git

Aim: to start using GitHub for course examples.

On the GitHub site
1)  Click to add a new repo
2)  Call new repo "my-isc-work" and 3) Click the add README box
4)	Click the Create repository button
5)	Click "Clone or download" and copy the link.

Now in the terminal window
1)	Make sure you are in your home directory
2)	Write the git clone command and add the URL to the repository (which is different for each user)
$ cd 
$ git clone https://<username>@github.com/<username>/my-isc-work.git

3)	Copy some of the files from yesterday’s exercises into the "my-isc-work" directory
4)	Change directory to "my-isc-work"
5)	Use git status to see what needs adding to the version control system.
$ git status
6)	Add the files
$ git add .
7)	Commit the changes: 
$ git commit -m 'Add some test files'
8)	Update GitHub repo: 
$ git push 
9)	Look on GitHub to see your changes.

 