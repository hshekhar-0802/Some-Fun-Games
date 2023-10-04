import random
guess_total=7
for i in range(5):
    print("Level "+str(i+1)+": ")
    n=random.randint(1,100)
    guess=guess_total
    while(guess>0):
        s=int(input("Enter your guess: "))        
        if(s==n):
            print("Your guess is correct..! Congratulations")
            print("Number of guesses you took: "+str(guess_total+1-guess))
            break
        elif(s<n):
            print("Your guess needs to be greater..")
        else:
            print("Your guess needs to be smaller..")
        guess-=1
    guess_total-=1
    if(guess==0):
        print("Sorry...! You lost the game..The correct guess was "+str(n))
        print("Levels crossed: "+str(i))
        break
if(i==0):
    print("You crossed all the levels of this game..!!!")