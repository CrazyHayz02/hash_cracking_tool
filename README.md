# hash_cracking_tool

How to start the Menu

You need to Open the Menu.py file you can do this multiple ways:

1) You can open the Menu folder an and then click the Menu.py file and then it will start the program

2) You can go into the command prompt (Click on the start menu in the bottom left and type "cmd" 
and it will be there) then you need to change directory to the Menu folder and then type Menu.py.




Select the program you want:

Then you have three options:

1) You can press 1 to start the Hash Cracker.

2) You can press 1 to start the SSH Brute Force.

3) You can press 1 to start the Unit test.




Change the Unit test:

You can change it by:

1) Going into the Menu folder

2) Then go into the Test folder

3) Then open the test_mangles.py file

4) Then change the file




Change to Different user and host SSH

You can change the SSH User, Host by:

1) Going into the Menu folder

2) Then go into the Menu.py file

3) In the function "def SSH_Brute():" change the "os.system('cmd /k "ssh_brute_force.py"')" 
to "os.system('cmd /k"ssh_brute_different.py"')"

4) Save and run Menu.py




Change to Different hashlist and wordlist hashcracker

You can change the hashlist, wordlist by:

1) Going into the Menu folder

2) Then go into the Menu.py file

3) In the function "def SSH_Brute():" change the "os.system('cmd /k "Cracker.py"')" 
to "os.system('cmd /k"Cracker_different.py"')"

4) Save and run Menu.py




Importing modules

1) Go on your command prompt or terminal
2) Then "cd" On your C: drive, go through "Users", then your account name, then "AppData", then "Local", "Programs", "Python", then your python folder, then "Scripts"
3) Then type "pip install" Module_name. Then press enter.
4) Then test if it can be imported by going into a python shell and import the new module
