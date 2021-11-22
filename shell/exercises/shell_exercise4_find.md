| [Solutions](shell_exercise4_find_sol.md) | [Exercise list](shell_exercise_index.md) |

# Exercise 4: Needle in a haystack

# Aim
Use `find` and `grep` to find the "Needle".

## Issues covered
Commands: `find`, `grep`.

## Instructions

1. Find the file `needle.txt` in the `acsoe` directory.
    1. Change directory to acsoe.
    2. Use the find command to look for the file called `needle.txt`.

2. Expand your search to look for files with `needle` anywhere in the filename. You need the same command again but use a `*` or two. 
3. Use grep to find the word needle in the files under `acsoe/ease-96/jetstream`.
4. Use the `man` page for `grep` to work out how to do a case insensitive search for needle. 
5. Use `grep` on the `js960724.ps2` file to print all lines without `1` in. (use the man page to find the right option)
6. Use grep on the `js960724.ps2` file to print all lines without `4` or `6` in, but do contain `33`.  
   (Hint: use pipes to  chain `grep` commands together)


