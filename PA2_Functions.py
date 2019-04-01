#Note that the script below is the module with the functions
#That will be used in the interface for the bulls & cows game

from random import randint
#The command above will import the randint built in Python function
#It will be needed in the function defined next

def generateSecretNumber ():
    r = randint (0, 9999)
    stringR = str(r)
    l = len(stringR)
    s = ((4-l)*"0" + stringR)
    return s
#The defined function above will generate a random 4-digit number
#This number is converted to a string, the length is taken and zero is added if
#Need be

def findUniqueDigits (s):
    uniqueDigits = []
    for i in s:
        if uniqueDigits.count(i)==0:
            uniqueDigits.append(i)
    return findUniqueDigits
#this function finds the unique numbers which are present in the 
#random 4-digit number generate above. for loop is used here


def findBulls (secret, guess):
    bulls = 0
    for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                bulls += 0
    return bulls
#This function gives us the number of digits which are similar in number and position
#Between the generated and guessed numbers (Bulls)


def findCows (secret, guess):
    bothBC = 0
    
    secretUniDigits = str(findUniqueDigits (secret))
    for i in secretUniDigits:
        secretcount = secret.count(i)
        guesscount = guess.count(i)
        minimum = min(secretcount, guesscount)
        bothBC += minimum

    bulls = findBulls (secret, guess)
    return (bothBC - bulls)
#This function gives out/returns the number of matched digits 
#In numbers but not positions (Cows)
