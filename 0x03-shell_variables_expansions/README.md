
# 0x03. Shell, init files, variables and expansions

This repository contains a collection of knowledge and examples related to Shell scripting, init files, environment variables, and expansions in Unix-like operating systems.

## Getting Started
Before diving into shell scripting, it's essential to have a basic understanding of computer programming concepts, including syntax, data types, and control flow statements. Additionally, familiarity with the fundamentals of the C programming language and the use of the gcc compiler is recommended.

## Project Requirements
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your scripts will be tested on Ubuntu 20.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file`  should print 2)
-   All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
-   The first line of all your files should be exactly  `#!/bin/bash`
-   A  `README.md`  file, at the root of the folder of the project, describing what each script is doing
-   You are not allowed to use  `&&`,  `||`  or  `;`
-   You are not allowed to use  `bc`,  `sed`  or  `awk`
-   All your files must be executable

## Mandatory Tasks

- [x] 0. <o> :

	Create a script that creates an alias.

	-   Name:  `ls`
	-   Value:  `rm *`

- [x] 1. Hello you :

	Create a script that prints `hello user`, where user is the current Linux user.
	
- [x] 2. The path to success is to take massive, determined action :
	
	Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.

- [x] 3. If the path be beautiful, let us not ask where it leads :

	Create a script that counts the number of directories in the `PATH`.
	
- [x] 4. Global variables :

	Create a script that lists environment variables.
	
- [x] 5. Local variables :

	Create a script that lists all local variables and environment variables, and functions.
	
- [x] 6. Local variable :

	Create a script that creates a new local variable.

	-   Name:  `BEST`
	-   Value:  `School`

- [x] 7. Global variable :

	Create a script that creates a new global variable.

	-   Name:  `BEST`
	-   Value:  `School`

- [x] 8. Every addition to true knowledge is an addition to human power :

	Write a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.
	
- [x] 9. Divide and rule :

	Write a script that prints the result of  `POWER`  divided by  `DIVIDE`, followed by a new line.

	-   `POWER`  and  `DIVIDE`  are environment variables

- [x] 10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath :

	Write a script that displays the result of  `BREATH`  to the power  `LOVE`

	-   `BREATH`  and  `LOVE`  are environment variables
	-   The script should display the result, followed by a new line

- [x] 11. There are 10 types of people in the world -- Those who understand binary, and those who don't :

	Write a script that converts a number from base 2 to base 10.

	-   The number in base 2 is stored in the environment variable  `BINARY`
	-   The script should display the number in base 10, followed by a new line

- [x] 12. Combination :

	Create a script that prints all possible combinations of two letters, except  `oo`.

	-   Letters are lower cases, from  `a`  to  `z`
	-   One combination per line
	-   The output should be alpha ordered, starting with  `aa`
	-   Do not print  `oo`
	-   Your script file should contain maximum 64 characters

- [x] 13. Floats :

	Write a script that prints a number with two decimal places, followed by a new line.

	The number will be stored in the environment variable  `NUM`.

## Advanced Tasks

- [x] 14. Decimal to Hexadecimal :

	Write a script that converts a number from base 10 to base 16.

	-   The number in base 10 is stored in the environment variable  `DECIMAL`
	-   The script should display the number in base 16, followed by a new line

- [x] 15. Everyone is a proponent of strong encryption :

	Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.

- [x] 16. The eggs of the brood need to be an odd number :

	Write a script that prints every other line from the input, starting with the first line.

- [x] 17. I'm an instant star. Just add water and stir. :

	Write a shell script that adds the two numbers stored in the environment variables  `WATER`  and  `STIR`  and prints the result.

	-   `WATER`  is in base  `water`
	-   `STIR`  is in base  `stir.`
	-   The result should be in base  `bestchol`
	
## Contributing
If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.
