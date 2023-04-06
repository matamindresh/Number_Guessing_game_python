import random as r

def rand_num():
    a=int(input("Enter the starting range:"))
    b=int(input("Enter the ending range:"))
    return r.randint(a,b)

print("Welcome to NUMBER GUESSING GAME")
x=rand_num()
count=0
status=True
while(status):
    guess_number=int(input("Enter your number:"))
    count=count+1
    print(count)
    if(guess_number==x):
        print(x,"YOUR GUESS IS CORRECT")
        print("you took ",count,"times")
        decision=int(input("THANK YOU FOR PLAYING \n do you want to play again \n 1.yes  2.No  :"))
        if (decision!=1):
            status=False
        else:
            x=rand_num()
    elif(guess_number>x):
        print("the number is lower than your guess")
    elif(guess_number<x):
        print("the number is greater than your guess")
    if(count==5):
        b=int(input("Do you still wanna continue \n 1.Yes 2.No  :"))
        if(b!=1):
            print("Thanking for playing.")
            status=False
