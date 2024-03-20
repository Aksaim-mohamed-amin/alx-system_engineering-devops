
# 0x04. Loops, conditions and parsing

Welcome to the "0x04. Loops, Conditions, and Parsing" project! In this project, you will delve into the fundamentals of loops, conditions, and parsing in Python programming. These concepts are essential for controlling the flow of your programs and handling data effectively.

## Project Requirements
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 20.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   You are not allowed to use  `awk`
-   Your Bash script must pass  `Shellcheck`  (version  `0.7.0`) without any error
-   The first line of all your Bash scripts should be exactly  `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

## Shellcheck

[Shellcheck](https://intranet.alxswe.com/rltoken/joK6l_yEZ9N7T0GQ1RDjLA "Shellcheck")  is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about.  `Shellcheck`  is your friend!  **All your Bash scripts must pass  `Shellcheck`  without any error or you will not get any points on the task**.

## Mandatory Tasks

- [x] 1. For Best School loop : 

	Write a Bash script that displays  `Best School`  10 times.

	Requirement:

	-   You must use the  `for`  loop (`while`  and  `until`  are forbidden)
	
- [x] 2. While Best School loop : 

	Write a Bash script that displays  `Best School`  10 times.

	Requirements:

	-   You must use the  `while`  loop (`for`  and  `until`  are forbidden)

- [x] 3. Until Best School loop : 

	Write a Bash script that displays  `Best School`  10 times.

	Requirements:

	-   You must use the  `until`  loop (`for`  and  `while`  are forbidden)

- [x] 4. If 9, say Hi! :

	Write a Bash script that displays  `Best School`  10 times, but for the 9th iteration, displays  `Best School`  _and then_  `Hi`  on a new line.

	Requirements:

	-   You must use the  `while`  loop (`for`  and  `until`  are forbidden)
	-   You must use the  `if`  statement

- [x] 5. 4 bad luck, 8 is your chance : 

	Write a Bash script that loops from 1 to 10 and:

	-   displays  `bad luck`  for the 4th loop iteration
	-   displays  `good luck`  for the 8th loop iteration
	-   displays  `Best School`  for the other iterations

	Requirements:

	-   You must use the  `while`  loop (`for`  and  `until`  are forbidden)
	-   You must use the  `if`,  `elif`  and  `else`  statements

- [x] 6. Superstitious numbers :

	Write a Bash script that displays numbers from 1 to 20 and:

	-   displays  `4`  _and then_  `bad luck from China`  for the 4th loop iteration
	-   displays  `9`  _and then_  `bad luck from Japan`  for the 9th loop iteration
	-   displays  `17`  _and then_  `bad luck from Italy`  for the 17th loop iteration

	Requirements:

	-   You must use the  `while`  loop (`for`  and  `until`  are forbidden)
	-   You must use the  `case`  statement

- [x] 7. Clock :
	Write a Bash script that displays the time for 12 hours and 59 minutes:

	-   display hours from 0 to 12
	-   display minutes from 1 to 59

	Requirements:

	-   You must use the  `while`  loop (`for`  and  `until`  are forbidden)

	Note that in this example, we only display the first 70 lines using the  `head`  command.

- [x] 8. For ls :

	Write a Bash script that displays:

	-   The content of the current directory
	-   In a list format
	-   Where only the part of the name after the first dash is displayed (refer to the example)

	Requirements:

	-   You must use the  `for`  loop (`while`  and  `until`  are forbidden)
	-   Do not display hidden files

- [x] 9. To file, or not to file :

	Write a Bash script that gives you information about the  `school`  file.

	Requirements:

	-   You must use  `if`  and,  `else`  (`case`  is forbidden)
	-   Your Bash script should check if the file exists and print:
	    -   if the file exists:  `school file exists`
	    -   if the file does not exist:  `school file does not exist`
	-   If the file exists, print:
	    -   if the file is empty:  `school file is empty`
	    -   if the file is not empty:  `school file is not empty`
	    -   if the file is a regular file:  `school is a regular file`
	    -   if the file is not a regular file: (nothing)

- [x] 10. FizzBuzz :

	Write a Bash script that displays numbers from 1 to 100.

	Requirements:

	-   Displays  `FizzBuzz`  when the number is a multiple of 3 and 5
	-   Displays  `Fizz`  when the number is multiple of 3
	-   Displays  `Buzz`  when the number is a multiple of 5
	-   Otherwise, displays the number
	-   In a list format

## Advanced Tasks

- [x] 11. Read and cut :

	help:  `read`

	Write a Bash script that displays the content of the file  `/etc/passwd`.

	Your script should only display:

	-   username
	-   user id
	-   Home directory path for the user

	Requirements:

	-   You must use the  `while`  loop (`for`  and  `until`  are forbidden)

- [x] 12. Tell the story of passwd :
	Read:

	-   [IFS (internal field separator)](https://intranet.alxswe.com/rltoken/8VeAz2XHCtuECDJ0PfMNIg "IFS (internal field separator)")
	-   [Understanding /etc/passwd](https://intranet.alxswe.com/rltoken/jm2-sSa3VlvI4zgRdreAsg "Understanding /etc/passwd")

	The file  `/etc/passwd`  has already been covered in a  [previous project](https://intranet.alxswe.com/rltoken/5Y_b9prAxb_Y-l8xCaZwgQ "previous project")  and you should be familiar with it. Today we will make up a story based on it.

	Write a Bash script that displays the content of the file  `/etc/passwd`, using the  `while`  loop + IFS.

	Format:  `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`

	Requirements:

	-   You must use the  `while`  loop (`for`  and  `until`  are forbidden)

- [x] 13. Let's parse Apache logs :

	[Apache](https://intranet.alxswe.com/rltoken/JfEwR2qcLdKkoihJNDZR0g "Apache")  is among the most popular web servers in the world, serving 50% of all active websites, no doubt that you will have to interact with it within your career.

	As a Full-Stack Software Engineer, you have to master the art of parsing log files. Today we will do a simple parsing of  [Apache log access files](http://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/80/apache-access.log "Apache log access files").

	Today the Customer Support department reported that a user reported that the site is being “buggy”. Not being a detailed description, you want to have a look at the Apache logs and gather data about the traffic.

	Write a Bash script that displays the visitor IP along with the  [HTTP status code](https://intranet.alxswe.com/rltoken/7de-UBmf8xgwH1iSwzX1MA "HTTP status code")  from the Apache log file.

	Requirement:

	-   Format: IP HTTP_CODE
	    -   in a list format
	    -   See example
	-   You must use  `awk`
	-   You are not allowed to use  `while`,  `for`,  `until`  and  `cut`
	-   Download and commit the  [apache-access.log file](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/80/apache-access.log "apache-access.log file")  along with your answers files

## Contributing

If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.
