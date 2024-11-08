#A Menu for the 3 thing
#Aaron Hayes 07/01/2021

import os #Imports the os module

counter = 0 #Defines the counter

def Hash_Cracking():
    '''This function is to execute the Cracker.py file in comamand line'''
    os.chdir("Hash_cracking")
    os.system('cmd /k "Cracker.py"')

def SSH_Brute():
    '''This function is to execute the ssh_brute_force.py file in comamand line'''
    os.chdir("ssh")
    os.system('cmd /k "ssh_brute_force.py"')

def Unit_test():
    '''This function is to execute the Unit testing file in comamand line'''
    os.system('cmd /k "python3 -m unittest -v Test.test_mangles"')


while counter == 0: #Starts a while loop till a awnser is entered
    Choice = input("What program do you want to run (1 = Hash cracking, 2 = SSH brute force, 3 = Unit test mangle rules)?\n") #This is where Choice is defined and the user enters there choice
    
    if Choice == "1": #This is where it checks if the the choice was one
        print (Hash_Cracking()) #This is used to call the Hash_Cracking() function
        counter = 1
        
    elif Choice == "2": #This is where it checks if the the choice was two
        print (SSH_Brute()) #This is used to call the SSH_Brute() function
        counter = 1

    elif Choice == "3": #This is where it checks if the the choice was three
        print (Unit_test()) #This is used to call the Unit_test() function
        counter = 1
        
    else: #This is if the awnser is not one of the choices
        print ("Error-Please use the numbers!!!")




