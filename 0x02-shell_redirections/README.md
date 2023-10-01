
# 0x02. Shell, I/O Redirections and filters

This repository is part of a series of learning materials aimed at helping individuals understand and master advanced concepts in shell scripting, input/output redirections, and filters in Unix-like operating systems. The contents of this repository provide a structured approach to learning, including explanations, examples, and exercises.

## Getting Started
Before diving into shell scripting, it's essential to have a basic understanding of computer programming concepts, including syntax, data types, and control flow statements. Additionally, familiarity with the fundamentals of the C programming language and the use of the gcc compiler is recommended.

## Project Requirements
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your scripts will be tested on Ubuntu 20.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file`  should print 2)
-   All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
-   The first line of all your files should be exactly  `#!/bin/bash`
-   A  `README.md`  file, at the root of the folder of the project, describing what each script is doing
-   You are not allowed to use backticks,  `&&`,  `||`  or  `;`
-   All your files must be executable
-   You are not allowed to use  `sed`  or  `awk`

## Mandatory Tasks

- [x] 0. Hello World :
	Write a script that prints “Hello, World”, followed by a new line to the standard output.

- [x] 1. Confused smiley :

	Write a script that displays a confused smiley `"(Ôo)'`.
	
- [x] 2. Let's display a file :

	Display the content of the  `/etc/passwd`  file.

	Example:

	```
	$ ./2-hellofile
	##
	# User Database
	#
	# Note that this file is consulted directly only when the system is running
	# in single-user mode. At other times this information is provided by
	# Open Directory.
	#
	# See the opendirectoryd(8) man page for additional information about
	# Open Directory.
	##
	nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
	root:*:0:0:System Administrator:/var/root:/bin/sh
	daemon:*:1:1:System Services:/var/root:/usr/bin/false
	_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
	_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
	_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
	_installassistant:*:25:25:Install Assistant:/var/empty:/usr/bin/false
	_lp:*:26:26:Printing Services:/var/spool/cups:/usr/bin/false
	_postfix:*:27:27:Postfix Mail Server:/var/spool/postfix:/usr/bin/false
	_scsd:*:31:31:Service Configuration Service:/var/empty:/usr/bin/false
	_ces:*:32:32:Certificate Enrollment Service:/var/empty:/usr/bin/false
	_mcxalr:*:54:54:MCX AppLaunch:/var/empty:/usr/bin/false
	_krbfast:*:246:-2:Kerberos FAST Account:/var/empty:/usr/bin/false
	```

- [x] 3. What about 2? :

	Display the content of  `/etc/passwd`  and  `/etc/hosts`

	Example:

	```
	$ ./3-twofiles
	##
	# User Database
	#
	# Note that this file is consulted directly only when the system is running
	# in single-user mode. At other times this information is provided by
	# Open Directory.
	#
	# See the opendirectoryd(8) man page for additional information about
	# Open Directory.
	##
	nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
	root:*:0:0:System Administrator:/var/root:/bin/sh
	daemon:*:1:1:System Services:/var/root:/usr/bin/false
	##
	# Host Database
	#
	# localhost is used to configure the loopback interface
	# when the system is booting. Do not change this entry.
	##
	127.0.0.1   localhost
	255.255.255.255 broadcasthost
	::1 localhost
	```
- [x] 4. Last lines of a file :

	Display the last 10 lines of  `/etc/passwd`

	Example:

	```
	$ ./4-lastlines
	_assetcache:*:235:235:Asset Cache Service:/var/empty:/usr/bin/false
	_coremediaiod:*:236:236:Core Media IO Daemon:/var/empty:/usr/bin/false
	_launchservicesd:*:239:239:_launchservicesd:/var/empty:/usr/bin/false
	_iconservices:*:240:240:IconServices:/var/empty:/usr/bin/false
	_distnote:*:241:241:DistNote:/var/empty:/usr/bin/false
	_nsurlsessiond:*:242:242:NSURLSession Daemon:/var/db/nsurlsessiond:/usr/bin/false
	_nsurlstoraged:*:243:243:NSURLStorage Daemon:/var/empty:/usr/bin/false
	_displaypolicyd:*:244:244:Display Policy Daemon:/var/empty:/usr/bin/false
	_astris:*:245:245:Astris Services:/var/db/astris:/usr/bin/false
	_krbfast:*:246:-2:Kerberos FAST Account:/var/empty:/usr/bin/false

	```
- [x] 5. I'd prefer the first ones actually :

	Display the first 10 lines of  `/etc/passwd`

	Example:

	```
	$ ./5-firstlines
	##
	# User Database
	#
	# Note that this file is consulted directly only when the system is running
	# in single-user mode. At other times this information is provided by
	# Open Directory.
	#
	# See the opendirectoryd(8) man page for additional information about
	# Open Directory.
	##
	```
- [x] 6. Line #2 :

	Write a script that displays the third line of the file  `iacta`.

	The file  `iacta`  will be in the working directory

	-   You’re not allowed to use  `sed`

- [x] 7. It is a good file that cuts iron without making a noise :

	Write a shell script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line.

- [x] 8. Save current state of directory :

	Write a script that writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.
	
- [x] 9. Duplicate last line :

	Write a script that duplicates the last line of the file  `iacta`

	-   The file  `iacta`  will be in the working directory

- [x] 10. No more javascript :

	Write a script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders.

- [x] 11. Don't just count your directories, make your directories count :

	Write a script that counts the number of directories and sub-directories in the current directory.

	-   The current and parent directories should not be taken into account  
	    
	-   Hidden directories should be counted

- [x] 12. What’s new :

	Create a script that displays the 10 newest files in the current directory.

	Requirements:

	-   One file per line
	-   Sorted from the newest to the oldest

- [x] 13. Being unique is better than being perfect :

	Create a script that takes a list of words as input and prints only words that appear exactly once.

	-   Input format: One line, one word
	-   Output format: One line, one word
	-   Words should be sorted

- [x] 14. It must be in that file :

	Display lines containing the pattern “root” from the file `/etc/passwd`

- [x] 15. Count that word :

	Display the number of lines that contain the pattern “bin” in the file `/etc/passwd`

- [x] 16. What's next? :

	Display lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`.

- [x] 17. I hate bins :

	Display all the lines in the file `/etc/passwd` that do not contain the pattern “bin”.
	
- [x] 18. Letters only please :

	Display all lines of the file  `/etc/ssh/sshd_config`  starting with a letter.

	-   include capital letters as well

- [x] 19. A to Z :

	Replace all characters `A` and `c` from input to `Z` and `e` respectively.

- [x] 20. Without C, you would live in hiago :

	Create a script that removes all letters `c` and `C` from input.

- [x] 21. esreveR :

	Write a script that reverse its input.

- [x] 22. DJ Cut Killer :

	Write a script that displays all users and their home directories, sorted by users.

	-   Based on the the  `/etc/passwd`  file

## Advanced Tasks

- [x] 23. Empty casks make the most noise :

	Write a command that finds all empty files and directories in the current directory and all sub-directories.

	-   Only the names of the files and directories should be displayed (not the entire path)  
	    
	-   Hidden files should be listed
	-   One file name per line  
	    
	-   The listing should end with a new line
	-   You are not allowed to use  `basename`,  `grep`,  `egrep`,  `fgrep`  or  `rgrep`

- [x] 24. A gif is worth ten thousand words :

	Write a script that lists all the files with a  `.gif`  extension in the current directory and all its sub-directories.

	-   Hidden files should be listed
	-   Only regular files (not directories) should be listed
	-   The names of the files should be displayed without their extensions
	-   The files should be sorted by byte values, but case-insensitive (file  `aaa`  should be listed before file  `bbb`, file  `.b`  should be listed before file  `a`, and file  `Rona`  should be listed after file  `jay`)
	-   One file name per line
	-   The listing should end with a new line
	-   You are not allowed to use  `basename`,  `grep`,  `egrep`,  `fgrep`  or  `rgrep`

- [x] 25. Acrostic :

	An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval.  [Read more](https://intranet.alxswe.com/rltoken/I2jXYKQIpVouDo0_1XrCJw "Read more").

	Create a script that decodes acrostics that use the first letter of each line.

	-   The ‘decoded’ message has to end with a new line
	-   You are not allowed to use  `grep`,  `egrep`,  `fgrep`  or  `rgrep`

- [x] 26. The biggest fan :

	Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

	-   Order by number of requests, most active host or IP at the top
	-   You are not allowed to use  `grep`,  `egrep`,  `fgrep`  or  `rgrep`

	Format:

	```
	host    When possible, the hostname making the request. Uses the IP address if the hostname was unavailable.
	logname Unused, always -
	time    In seconds, since 1970
	method  HTTP method: GET, HEAD, or POST
	url Requested path
	response    HTTP response code
	bytes   Number of bytes in the reply

	```

	Here is an example with one day of logs of the NASA website (1995).

	```
	julien@ubuntu:/tmp/0x02$ wget https://s3.amazonaws.com/alx-intranet.hbtn.io/public/nasa_19950801.tsv
	--2022-03-08 11:08:26--  https://s3.amazonaws.com/alx-intranet.hbtn.io/public/nasa_19950801.tsv
	Resolving s3.amazonaws.com (s3.amazonaws.com)... 52.217.171.144
	Connecting to s3.amazonaws.com (s3.amazonaws.com)|52.217.171.144|:443... connected.
	HTTP request sent, awaiting response... 200 OK
	Length: 782913 (765K) [binary/octet-stream]
	Saving to: ‘nasa_19950801.tsv’

	nasa_19950801.tsv   100%[===================>] 764.56K  --.-KB/s    in 0.008s

	2022-03-08 11:08:26 (98.4 MB/s) - ‘nasa_19950801.tsv’ saved [782913/782913]

	julien@ubuntu:/tmp/0x02$ head nasa_19950801.tsv
	host    logname time    method  url     response        bytes
	in24.inetnebr.com       -       807249601       GET     /shuttle/missions/sts-68/news/sts-68-mcc-05.txt 200     1839
	uplherc.upl.com -       807249607       GET     /       304     0
	uplherc.upl.com -       807249608       GET     /images/ksclogo-medium.gif      304     0
	uplherc.upl.com -       807249608       GET     /images/MOSAIC-logosmall.gif    304     0
	uplherc.upl.com -       807249608       GET     /images/USA-logosmall.gif       304     0
	ix-esc-ca2-07.ix.netcom.com     -       807249609       GET     /images/launch-logo.gif 200     1713
	uplherc.upl.com -       807249610       GET     /images/WORLD-logosmall.gif     304     0
	slppp6.intermind.net    -       807249610       GET     /history/skylab/skylab.html     200     1687
	piweba4y.prodigy.com    -       807249610       GET     /images/launchmedium.gif        200     11853
	julien@ubuntu:/tmp/0x02$ ./103-the_biggest_fan < nasa_19950801.tsv 
	www-relay.pa-x.dec.com
	piweba3y.prodigy.com
	www.thyssen.com
	130.110.74.81
	ix-min1-02.ix.netcom.com
	uplherc.upl.com
	reggae.iinet.net.au
	seigate.sumiden.co.jp
	ircgate1.rcc-irc.si
	s150.phxslip4.indirect.com
	torben.dou.dk
	```

## Contributing
If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.