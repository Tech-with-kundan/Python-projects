
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




# now the words have done.
import random

def shuffleWord(word):
     
     word= random.sample(word, k=len(word))
     #  this will return list of word not string to make it strign  we will use one  very useful funtion called join(list) 
     # this join function will reutrn string.
     # below we are also demostrating this join methods.
     
     return ' '.join(word) 


def Find_correct_Word(word, score):
  dup_word=shuffleWord(word)  # calling shuffleWord() to shufle a particular 
  
  print("Arrange the latter to form valid word ")
  print(dup_word)     
  s= input()
  if  s.lower()== word:
    score+=1
    print("correct")
  else :
    score-=1
    print("incorrect")
  return score 
  

 
def main():
    
     words=["country","break","india","nurture","lisp","incridible"]
     words=random.sample(words, k=len(words))
    
     score=0
     
     for wr in  words:
       score=Find_correct_Word(wr, score)
     print("the total score is ", score )
     
# Here we are calling this main method to execute whole code . 
main()
     

  

  
  
  

  