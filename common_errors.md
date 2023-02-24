# ISC - Common Errors/Issues and Solutions
This file is a work in progress. Please add any additional errors and solutions encountered by one or more participants of the ISC course.
Added: 24/02/2023

## 0. Contents:
 - Syntax Errors
 - Git Errors
 - Importing Issues

## 1. Syntax Errors
A list of common syntax errors made by users during ISC sessions

### Incorrect syntax in importing - ImportError
```
from data_file import MyClass
```
From the above import, the correct syntax to invoke the class is `instance = MyClass()` and not `instance = data_file.MyClass()`.

### Incorrect syntax when naming variables - NameError
```
myNum = 1
yourNum = mynum + 1
```
__NameError: name 'mynum' is not defined__

## 2. Git Errors
The correct pipeline for pushing changes is:
 - git add "file"
 - git commit -m "message about file"
 -__repeat for each file or group of files that can be related to one commit message__
 - git push (-u origin main)

### Common mistakes
 - On git push: Everything is up to date - you have probably missed the _commit_ or _add_ stages.
 - On git status: `fatal: not a git repository...` - you are not currently in the git repository and need to use `cd` to navigate to the correct directory.
 - On git clone: `fatal: destination path already exists...` - you already have a directory with the same name as the repository you're trying to clone, you need to move that directory somewhere else or rename it.

## 3. Import Errors
Common issues are with locating files to import into a script/notebook because the relative paths are wrong

### Local and sub-directory imports
You can import a python file if it is in either the current directory or a sub-directory of the current directory.
i.e 
```
/home/users/user123
 - Documents
   - python_files
     - program1.py
     - import1.py
     - other_files
       - import2.py
   - code
     - import3.py
```
In the file _program1.py_ we can import _import1_ and _import2_, but _import3_ is in a parent directory requires extra work
```
from import1 import function1
from other_files.import2 import function2
```

### Parent Directory imports
To import the objects from import3.py we require an extra step.
```
import sys
sys.path.append('/home/users/user123/Documents/code/')
from import3 import function3
```
Appending the file path to the PATH variable of the environment means that when you try to import a module, there is an extra place the python interpreter can check for that module/file as well as the defaults (usually /home/users/user123/lib, the current directory etc.)