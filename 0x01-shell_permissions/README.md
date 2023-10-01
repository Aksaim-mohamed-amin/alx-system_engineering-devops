# 0x01. Shell, Permissions
This repository is part of a series of learning materials aimed at helping individuals understand and master the fundamentals of shell scripting and permissions management in Unix-like operating systems. The contents of this repository provide a structured approach to learning, including explanations, examples, and exercises.

## Introduction

The shell is a command-line interface that enables you to interact with your computer's operating system. It is a powerful tool for managing files, executing programs, and automating tasks. This repository is your guide to becoming proficient in using the shell and writing shell scripts.

## Getting Started
Before diving into shell scripting, it's essential to have a basic understanding of computer programming concepts, including syntax, data types, and control flow statements. Additionally, familiarity with the fundamentals of the C programming language and the use of the gcc compiler is recommended.

## Project Requirements
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your scripts will be tested on Ubuntu 20.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file`  should print 2)
-   All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
-   The first line of all your files should be exactly  `#!/bin/bash`
-   A  `README.md`  file at the root of the repo, containing a description of the repository
-   A  `README.md`  file, at the root of the folder of  _this_  project, describing what each script is doing
-   You are not allowed to use backticks,  `&&`,  `||`  or  `;`
-   All your scripts must be executable. To make your file executable, use the  `chmod`  command:  `chmod u+x file`. Later, we’ll learn more about how to utilize this command.

## Mandatory Tasks

- [x] 0. My name is Betty :
	Create a script that switches the current user to the user  `betty`.

	-   You should use exactly 8 characters for your command (+1 character for the new line)
	-   You can assume that the user  `betty`  will exist when we will run your script

- [x] 1. Who am I :
	Write a script that prints the effective username of the current user.
	
- [x] 2. Groups :
	Write a script that prints all the groups the current user is part of.

- [x] 3. New owner :
	Write a script that changes the owner of the file `hello` to the user `betty`.

- [x] 4. Empty! :
	Write a script that creates an empty file called `hello`.

- [x] 5. Execute :
	Write a script that adds execute permission to the owner of the file  `hello`.

	-   The file  `hello`  will be in the working directory

- [x] 6. Multiple permissions :
	Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file  `hello`.

	-   The file  `hello`  will be in the working directory

- [x] 7. Everybody! :

	Write a script that adds execution permission to the owner, the group owner and the other users, to the file  `hello`

	-   The file  `hello`  will be in the working directory
	-   You are not allowed to use commas for this script

- [x] 8. James Bond :
	Write a script that sets the permission to the file  `hello`  as follows:

	-   Owner: no permission at all
	-   Group: no permission at all
	-   Other users: all the permissions

	The file  `hello`  will be in the working directory You are not allowed to use commas for this script
	
- [x] 9. John Doe :
    
	Write a script that sets the mode of the file  `hello`  to this:

	```
	-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

	```

	-   The file  `hello`  will be in the working directory
	-   You are not allowed to use commas for this script

- [x] 10. Look in the mirror :
	Write a script that sets the mode of the file  `hello`  the same as  `olleh`’s mode.

	-   The file  `hello`  will be in the working directory
	-   The file  `olleh`  will be in the working directory

- [x] 11. Directories :
	Create a script that adds execute permission to all subdirectories of the  **current directory**  for the owner, the group owner and all other users.

	Regular files should not be changed.

- [x] 12. More directories :
	Create a script that creates a directory called `my_dir` with permissions 751 in the working directory.

- [x] 13. Change group :
	Write a script that changes the group owner to  `school`  for the file  `hello`

	-   The file  `hello`  will be in the working directory

## Advanced Tasks

- [x] 14. Owner and group :
	Write a script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.

- [x] 15. Symbolic links :
	Write a script that changes the owner and the group owner of  `_hello`  to  `vincent`  and  `staff`  respectively.

	-   The file  `_hello`  is in the working directory
	-   The file  `_hello`  is a symbolic link

- [x] 16. If only :
    
	Write a script that changes the owner of the file  `hello`  to  `betty`  only if it is owned by the user  `guillaume`.

	-   The file  `hello`  will be in the working directory

- [x] 17. Star Wars :
	Write a script that will play the StarWars IV episode in the terminal.

## Contributing
If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.
