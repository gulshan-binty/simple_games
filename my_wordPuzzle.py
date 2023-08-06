import random

words=['programming','tiger','doctor','lamp','television','youtube','water','laptop','project','today']
random_word= random.choice(words)
print("***Word Guessing Game***")

user_guess=''
chances=10
while chances>0:
    wrong_guesses=0
    for character in random_word:
        if character in user_guess:
            print(f"Correct Guess:{character}")
        else:
            wrong_guesses+=1
            print("_")

    if wrong_guesses==0:
        print("Correct")
        print(f"Word: {random_word}")
        break
    guess=input("Make a Guess: ")
    user_guess+=guess
    if guess not in random_word:
        chances-=1
        print(f"Wrong. You Have {chances} More Chances")

        if chances ==0:
            print("Game Over")



    

