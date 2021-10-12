| [Solutions](shell_exercise8_ssh_sol.md) | [Exercise list](shell_exercise_index.md) |

# SSH

## Aim
Have a go at using ssh.

## Issues covered
`ssh`, `scp`, `df`, `touch`

## Instructions

1. cd to `/tmp` and make a file `touch <username>.txt`
> `touch` just changes a files modified time to now. It is also useful for creating an empty file quickly which is what we are doing here.
2.	ssh to `<username>@sci2.jasmin.ac.uk`. 
3.	This computer shares the same home directory as `sci1.jasmin.ac.uk` but not `/tmp`.  Use ls, pwd and other commands to prove to yourself it’s the same home directory. Then change directory to `/tmp`. The `<username>.txt` will not be there as it is a different computer.
4.	Logout (use exit or ^D)
5.	Use scp to copy some files to `/tmp` on the remote computer. 
6.	Login again and list the files you copied. 
7.	Logout
8.	Use ssh to run `df /tmp` on the remote computer.
> `df` gives information about the how much space there is on a file system.  

