import random
options = ['R','P','S']
print("We are going to play Rock ,paper and scissors")
print("please Select for the following")
print("Rock - R \n Paper - P \n Scissors - S")
urChoice = input("What are you going to choose").upper()
comChoice = random.randint(0,2)

if(urChoice == 'R'):
    print(options[comChoice])
    if(options[comChoice] == 'R'):
        print("draw")
    elif(options[comChoice] == 'P'):
        print("computer wins")
    else:
        print("You win")
elif(urChoice == 'P'):
    print(options[comChoice])
    if(options[comChoice] == 'P'):
        print("Draw")
    elif(options[comChoice] == "R"):
        print("You win")
    else:
        print("Computer wins")
elif(urChoice=='S'):
    print(options[comChoice])
    if(options[comChoice] =='S'):
        print("Draw")
    elif(options[comChoice] == 'P'):
        print("you win")
    else:
        print("computer wins")