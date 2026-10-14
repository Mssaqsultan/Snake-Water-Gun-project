import random
'''
computer - -1 = water
1 = snake
0 = gun
'''
computer = random.choice([-1,0,1])
user_str = input("Enter your choice: ")
user_dict = {"s":1, "w":-1, "g":0}
user = user_dict[user_str]
reverse_dict = {1 : "Snake", 0: "Gun", -1:"Water"}
print(f"User choose {reverse_dict[user]}\nComputer choose {reverse_dict[computer]}")

if(computer == user):
    print("Its Draw")
else:
    if(computer == -1 and user == -1):
        print("You win!")
    elif(computer == -1 and user == 0):
        print("You Lose!")
    
    elif(computer == -1 and user == 1):
        print("You lose!")
    
    elif(computer == 1 and user == 0):
        print("You Win!")
    
    elif(computer == 0 and user == -1):
        print("You win!")
    
    elif(computer == 0 and user == 1):
        print("You Lose!")
    
    else:
        print("Something went wrong!")
