import random

while True:
    computer = random.randint(0,2)
    

    print("Enter '0' for STONE \nEnter '1' for PAPER \nEnter '2' for SCISSORS \n ")
    user = int(input("Choose Your Number: "))

    print(f"You Choose {user} and Computer Choose {computer}")
    if computer == user:
        print("Draw")
    elif(computer == 0 and user == 1):
        print("You Win")
    elif(computer == 0 and user == 2):
        print("Computer Win")
    elif(computer == 1 and user == 0):
        print("Computer Win")
    elif(computer == 1 and user == 2):
        print("You Win")
    elif(computer == 2 and user == 0):
        print("You Win")
    elif(computer == 2 and user == 1):
        print("Computer Win")
    else:
        print("Enter A Valid Number")
    print("\n \n \n \n")
