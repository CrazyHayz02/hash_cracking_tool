#A cracking program for cracking hashes
#Aaron Hayes 07/01/2021

import hashlib #imports the module hashlib
import datetime #imports the module hashlib

count = 0 #defines count

hashlist, wordlist = input("Please enter the hashlist and wordlist. Enter like this(Hashlist, wordlist)\n").split(", ")
hashlistRead = open(hashlist, "r") #defines hashlist by opening the hashlist
dic = open(wordlist, "r") #defines dic by opening the wordlist


def cap(keyword):
    '''This function is used to mangle the word to have a capital letter at the beggining'''
    return [keyword.capitalize()]

def up(keyword):
    '''This function is used to mangle the word to have all the letters in upper case'''
    return [keyword.upper()]

def append_num(keyword, start=0, end=11):
    '''This function is used to mangle the word to add a number to the end'''
    return [keyword + str(num) for num in range(start,end)]

def replace_a(keyword, A = ["@", "4"]):
    '''This function is used to mangle the word to change a to "@" and "4"'''
    return [keyword.replace("a", a) for a in A]

def replace_s(keyword, S = ["$", "5"]):
    '''This function is used to mangle the word to change s to "$" and "5"'''
    return [keyword.replace("s", s) for s in S]

def replace_i(keyword, I = ["!", "1"]):
    '''This function is used to mangle the word to change i to "!" and "1"'''
    return [keyword.replace("i", i) for i in I]

def replace_t(keyword, T = ["7", "+"]):
    '''This function is used to mangle the word to change t to "7" and "+"'''
    return [keyword.replace("t", t) for t in T]

def replace_b(keyword, B = ["8", "&"]):
    '''This function is used to mangle the word to change b to "8" and "&"'''
    return [keyword.replace("b", b) for b in B]

def reverse(keyword):
    '''This function is used to mangle the word to reverse the leters so e.g. cat becomes tac'''
    return [keyword[:: - 1]]

def replace_h(keyword):
    '''This function is used to mangle the word to change h to "#"'''
    return [keyword.replace("h", "#")]

def replace_o(keyword):
    '''This function is used to mangle the word to change o to "0"'''
    return [keyword.replace("o", "0")]

def replace_e(keyword):
    '''This function is used to mangle the word to change e to "3"'''
    return [keyword.replace("e", "3")]

def replace_l(keyword):
    '''This function is used to mangle the word to change l to "1"'''
    return [keyword.replace("l", "1")]

def append_symbol(keyword, symbol = ["!", "@", "2", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "<", ">", "?"]):
    '''This function is used to mangle the word to add symbols to the end"'''
    return [keyword + sym for sym in symbol]

with open("Success_cracked.txt", "a") as Cracked_words:
    Cracked_words.truncate(0) #Clears the txt file
    

        
for lines in hashlist: #Goes for the lines in the hashlist
    startTime = datetime.datetime.now() 
    salt, hashword = lines.strip().split(":") #Seperates the salts from the hash
    dic.seek(0) #goes to the top of the word list every run

    for x in range(0, 10):
        next(dic) #Skips the first ten lines
        

    count += 1 #This add every time it goes through a word 

    if len(hashword) == 32: #Check if the length of the hashword is 32 charactors long as that means its a md5 hash
        for keyword in dic: #Goes through the wordlist
            
            word = keyword.strip("\n") + salt #Adds the salt to the words
            hash_obj = hashlib.md5((word).encode('utf-8')).hexdigest() #Encodes the mangled word from the list and makes it a md5 hash
            if hash_obj ==  hashword: #Check if the hash from hashlist is the same as the hashed word from the word list 
                endTime = str(str(datetime.datetime.now() - startTime).split(".")[0])
                decryptword = ("Word"+str(count)+ ": " +keyword)
                with open("Success_cracked.txt", "a") as Cracked_words:
                    Cracked_words.write(decryptword) #Writes the word to the word list
                print (decryptword.strip("\n"), " Time:", endTime)
                break
            
            #These are the rule that need the word to run through and the 
            permutations = [keyword.strip("\n")]
            rules = [reverse, replace_a, replace_s, replace_o, replace_e, replace_i, replace_t, replace_h, replace_l, replace_b, cap, up, append_num]
            for rule in rules: #Goes through the rules in the rules list
                permutations = list(dict.fromkeys(permutations))
                new_perm = []
                for perm in permutations: #Goes through the words in the permutations list 
                    new_perm.extend(rule(perm))#This will mange the words in permutations with the rule its on add to the new_perm list
                for words in new_perm: #Goes through the words in the new_perm list
                    word = words + salt #Adds the salt to the mangled words
                    hash_obj = hashlib.md5((word).encode('utf-8')).hexdigest() #Encodes the mangled word from the list and makes it a md5 hash
                    if hash_obj ==  hashword: #Check if the hash from hashlist is the same as the hashed mangled word from the word list 
                        endTime = str(str(datetime.datetime.now() - startTime).split(".")[0])
                        decryptword = ("Word"+str(count)+ ": " +words+ "\n")
                        with open("Success_cracked.txt", "a") as Cracked_words:
                            Cracked_words.write(decryptword) #Writes the word to the mangle word list
                        print (decryptword.strip("\n"), " Time:", endTime)
                        break
                    
                permutations.extend(new_perm) #Add to the permutations list for the next rule

           #Breaks if the programe finds the word     
                if hash_obj ==  hashword:
                    break

            if hash_obj ==  hashword:
                break


    elif len(hashword) == 64: #Check if the length of the hashword is 64 charactors long as that means its a sha256 hash
        for keyword in dic: #Goes through the wordlist
            word = keyword.strip("\n") + salt #Adds the salt to the words
            hash_obj = hashlib.sha256((word).encode('utf-8')).hexdigest() #Encodes the mangled word from the list and makes it a md5 hash
            if hash_obj ==  hashword: #Check if the hash from hashlist is the same as the hashed word from the word list 
                endTime = str(str(datetime.datetime.now() - startTime).split(".")[0])
                decryptword = ("Word"+str(count)+ ": " +keyword)
                with open("Success_cracked.txt", "a") as Cracked_words:
                    Cracked_words.write(decryptword) #Writes the word to the word list
                print (decryptword.strip("\n"), " Time:", endTime)
                break
            
            #These are the rule that need the word to run through and the 
            rules = [reverse, replace_a, replace_s, replace_o, replace_e, replace_i, replace_t, replace_h, replace_l, replace_b, cap, up, append_num]
            permutations = [keyword.strip("\n")]
            for rule in rules: #Goes through the rules in the rules list
                permutations = list(dict.fromkeys(permutations))
                new_perm = []
                for perm in permutations: #Goes through the words in the permutations list 
                    new_perm.extend(rule(perm))#This will mange the words in permutations with the rule its on add to the new_perm list

                for words in new_perm: #Goes through the words in the new_perm list
                    word = words + salt #Adds the salt to the mangled words
                    hash_obj = hashlib.sha256((word).encode('utf-8')).hexdigest() #Encodes the mangled word from the list and makes it a md5 hash
                    if hash_obj ==  hashword: #Check if the hash from hashlist is the same as the hashed mangled word from the word list 
                        endTime = str(str(datetime.datetime.now() - startTime).split(".")[0])
                        decryptword = ("Word"+str(count)+ ": " +words+ "\n")
                        with open("Success_cracked.txt", "a") as Cracked_words:
                            Cracked_words.write(decryptword) #Writes the word to the mangle word list
                        print (decryptword.strip("\n"), " Time:", endTime)
                        break
                    
                permutations.extend(new_perm) #Add to the permutations list for the next rule

           #Breaks if the programe finds the word     
                if hash_obj ==  hashword:
                    break

            if hash_obj ==  hashword:
                break

        
    elif len(hashword) == 128: #Check if the length of the hashword is 128 charactors long as that means its a sha512 hash
        for keyword in dic: #Goes through the wordlist
            word = keyword.strip("\n") + salt #Adds the salt to the words
            hash_obj = hashlib.sha512((word).encode('utf-8')).hexdigest() #Encodes the word from the list and makes it a sha512 hash
            if hash_obj ==  hashword: #Check if the hash from hashlist is the same as the hashed word from the word list 
                endTime = str(str(datetime.datetime.now() - startTime).split(".")[0])
                decryptword = ("Word"+str(count)+ ": " +keyword)
                with open("Success_cracked.txt", "a") as Cracked_words:
                    Cracked_words.write(decryptword) #Writes the word to the word list
                print (decryptword.strip("\n"), " Time:", endTime)
                break
            
            #These are the rule that need the word to run through and the 
            rules = [reverse, replace_a, replace_s, replace_o, replace_e, replace_i, replace_t, replace_h, replace_l, replace_b, cap, up, append_num]
            permutations = [keyword.strip("\n")]
            for rule in rules: #Goes through the rules in the rules list
                permutations = list(dict.fromkeys(permutations))
                new_perm = []
                for perm in permutations: #Goes through the words in the permutations list 
                    new_perm.extend(rule(perm))#This will mange the words in permutations with the rule its on add to the new_perm list

                for words in new_perm: #Goes through the words in the new_perm list
                    word = words + salt #Adds the salt to the mangled words
                    hash_obj = hashlib.sha512((word).encode('utf-8')).hexdigest() #Encodes the mangled word from the list and makes it a sha512 hash
                    if hash_obj ==  hashword: #Check if the hash from hashlist is the same as the hashed mangled word from the word list 
                        endTime = str(str(datetime.datetime.now() - startTime).split(".")[0])
                        decryptword = ("Word"+str(count)+ ": " +words+ "\n")
                        with open("Success_cracked.txt", "a") as Cracked_words:
                            Cracked_words.write(decryptword) #Writes the word to the mangle word list
                        print (decryptword.strip("\n"), " Time:", endTime)
                        break
                    
                permutations.extend(new_perm) #Add to the permutations list for the next rule

           #Breaks if the programe finds the word     
                if hash_obj ==  hashword:
                    break

            if hash_obj ==  hashword:
                break



