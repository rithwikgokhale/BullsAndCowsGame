#This script is the actual game which the user plays/uses

from PA2_Functions import *
#This will import the functions from the module done before

print ("Bulls and Cows Game")#Welcoming Statement

secret = generateSecretNumber ()#secret is the randomly generated number

print secret#THIS IS ONLY FOR GRADING PURPOSES NOT IN THE FINAL GAME SCRIPT

guess = str(input("Enter your guess: "))
#Note that the guess is converted into strings
while guess != secret:
    bulls = str(findBulls (secret, guess))
    cows = str(findCows (secret, guess))
    print bulls+("A")+cows+("B")
    guess = str(input("Enter your guess: "))

#Using the while loop allows the user to try several times
#While keeping the script short and easy to understand

print ("That's it!")

#This final print command is only given once the user has 
#Guessed the generated number correctly
