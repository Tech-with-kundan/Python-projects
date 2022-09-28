"""
Problem Statement: You have to write a Word Puzzle Game in which the user has to form
the correct word out of a given set of characters. In the game the user has to solve this
puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
in random sequence. Give the user score +1 for each correct answer and give -1 for each
wrong answer. At last print the final score. You can store any number of words in the list, but
in each round of the game only 5 words are shown to the user.
Sample output of the game:
Arrange the letters to form a valid word:
RAEHTF
Father
Correct
Arrange the letters to form a valid word:
KABRE
Barke
Wrong
Arrange the letters to form a valid word:
CYROTNU
Cry
Wrong
Arrange the letters to form a valid word:
RENEG
green
Correct
Arrange the letters to form a valid word:
OAERELANP
aeroplane
Correct
Net Score is 1
"""
import random 
def checktheword(word, score):
    tempword=random.sample(word, len(word))   #  here  we have added random module which is so important to arrange the  randomaly 
    newword="".join(tempword)  
    print(newword)  # in this line we have printed the radomaly word  on the screen . 
    string=""       # in this line we have   taken a string 
    print("enter the word:  ")
    string=input()   # by calling input method we are taking the  string into string variable 
    print()  # for one space I have given the pritn() method . 
    
    if string.upper() == word :  # here we have put one condition for checking the  string that user has  entered is same to oringal word if it is yes then increaase score value by 1 otherwise decrease by 1  
        print("CORRECT")
        score+=1 
    else :
        score-=1
        print("\n INCORRECT")
    return score   # at the end we are returning the updated value of score  . which will  oour answer . 




def main():
    # inside the main() first we have created  a list with 5 words 
     original_chart=['COUNTRY','BREAK','ROSE','HUMANITY','SCENARIO']
    
     score=0   # this will be our score variable which will be keept the record of scoring . 

     for word in original_chart :  # here we are  perfroming our operations on each and evdry words . 
        score=checktheword(word, score)
     print("TOTAL SCORE = ", score)
     


# this is the our main () fuction to whom we have called . 
main()

 
