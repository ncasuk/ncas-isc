| [Solutions](shell_exercise8_ssh_sol.md) | [Exercise list](shell_exercise_index.md) |

# SSH

## Aim
Have a go at using ssh.

- Create a file on one machine.
- Go to a remote machine and see that your file is not there
- Exit that remote machine
- use `scp` to copy the file to the remote `/tmp` directory
- Login to the remote machine and see that your file is now there


## Issues covered
`ssh`, `scp`, `df`, `touch`

## Instructions

**NOTE: This exercise assumes you are starting on sci1.jasmin.ac.uk but it will work between any two hosts. If you want to hop between sci hosts, either return to the login node or login to the sci machine using the `-A` flag. e.g `ssh -A <username>@login1.jasmin.ac.uk` -> `ssh -A sci1`**

1. cd to `/tmp` and make a file `touch <username>.txt`
> `touch` just changes a files modified time to now. It is also useful for creating an empty file quickly which is what we are doing here.
2.	ssh to `<username>@sci2.jasmin.ac.uk`. (or a different host, if you started on sci2)
3.	This computer shares the same home directory as `sci1.jasmin.ac.uk` but not `/tmp`.  Use ls, pwd and other commands to prove to yourself it’s the same home directory. Then change directory to `/tmp`. The `<username>.txt` will not be there as it is a different computer.
4.	Logout (use exit or ^D)
5.	Use scp to copy some files to `/tmp` on the remote computer. 
6.	Login again and list the files you copied. 
7.	Logout
8.	Use ssh to run `df /tmp` on the remote computer.
> `df` gives information about the how much space there is on a file system.  

