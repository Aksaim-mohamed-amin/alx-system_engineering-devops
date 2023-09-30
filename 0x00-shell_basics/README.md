
# 0x00. Shell Basics
This repository contains a series of exercises and resources to help you master the basics of shell scripting and command-line usage. Whether you're a beginner or looking to reinforce your knowledge, this repository is designed to provide you with a strong foundation in shell scripting and command-line navigation.

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

- [x] 0. Where am I?
	Write a script that prints the absolute path name of the current working directory.

	Example:

	```
	$ ./0-current_working_directory
	/root/alx-system_engineering-devops/0x00-shell_basics
	```

- [x] 1. What’s in there? :
	Display the contents list of your current directory.

	Example:

	```
	$ ./1-listit
	Applications    Documents   Dropbox Movies Pictures
	Desktop Downloads   Library Music Public
	```
- [x] 2. There is no place like home :
		Write a script that changes the working directory to the user’s home directory.

	-   You are not allowed to use any shell variables
- [x] 3. The long format :
	Display current directory contents in a long format

- [x] 4. Hidden files :
	Display current directory contents, including hidden files (starting with  `.`). Use the long format.

	Example:

	```
	$ ./4-listmorefiles
	total 32
	drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
	drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
	-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
	-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
	-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
	-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
	-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
	```

- [x] 5. I love numbers :
	Display current directory contents.

	-   Long format
	-   with user and group IDs displayed numerically
	-   And hidden files (starting with .)

	Example:

	```
	$ ./5-listfilesdigitonly
	total 32
	drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
	drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
	-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
	-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
	-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
	-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
	-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
	-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
	```

- [x] 6. Welcome :
	Create a script that creates a directory named  `my_first_directory`  in the  `/tmp/`  directory.

	Example:

	```
	$ ./6-firstdirectory
	$ file /tmp/my_first_directory/
	/tmp/my_first_directory/: directory
	```
- [x] 7. Betty in my first directory :

	Move the file  `betty`  from  `/tmp/`  to  `/tmp/my_first_directory`.

	Example:

	```
	$ ./7-movethatfile
	$ ls /tmp/my_first_directory/
	betty
	```
- [x] 8. Bye bye Betty :
	Delete the file  `betty`.

	-   The file  `betty`  is in  `/tmp/my_first_directory`

	Example:

	```
	$ ./8-firstdelete
	$ ls /tmp/my_first_directory/
	```

- [x] 9. Bye bye My first directory :
    
	Delete the directory  `my_first_directory`  that is in the  `/tmp`  directory.

	Example:

	```
	$ ./9-firstdirdeletion
	$ file /tmp/my_first_directory
	/tmp/my_first_directory: cannot open `/tmp/my_first_directory' (No such file or directory)
	```
- [x] 10. Back to the future :
	  Write a script that changes the working directory to the previous one.

- [x] 11. Lists :
	Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

- [x] 12. File type :
	Write a script that prints the type of the file named  `iamafile`. The file  `iamafile`  will be in the  `/tmp`  directory when we will run your script.

	Example

	```
	ubuntu@ip-172-31-63-244:~$ ./12-file_type
	/tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
	```

- [x]  13. We are symbols, and inhabit symbols :
	Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.

- [x]   14. Copy HTML files :
    
	Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

	You can consider that all HTML files have the extension  `.html`

## Advanced Tasks

- [x] 15. Let’s move :
	Create a script that moves all files beginning with an uppercase letter to the directory  `/tmp/u`.

	You can assume that the directory  `/tmp/u`  will exist when we will run your script

- [x]  16. Clean Emacs :
    
	Create a script that deletes all files in the current working directory that end with the character `~`.

- [x]  17. Tree :
	Create a script that creates the directories  `welcome/`,  `welcome/to/`  and  `welcome/to/school`  in the current directory.

	You are only allowed to use two spaces (and lines) in your script, not more.

- [x] 18. Life is a series of commas, not periods :
	Write a command that lists all the files and directories of the current directory, separated by commas (`,`).

	-   Directory names should end with a slash (`/`)  
	    
	-   Files and directories starting with a dot (`.`) should be listed  
	    
	-   The listing should be alpha ordered, except for the directories  `.`  and  `..`  which should be listed at the very beginning
	-   Only digits and letters are used to sort; Digits should come first
	-   You can assume that all the files we will test with will have at least one letter or one digit
	-   The listing should end with a new line

- [x] 19. File type: School :
	Create a magic file `school.mgc` that can be used with the command `file` to detect `School` data files. `School` data files always contain the string `SCHOOL` at offset 0.

## Contributing
If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated