import random

computer_score = 0
user_score = 0

while computer_score < 5 and user_score < 5:
    x = random.randint (1,3)

    if x == 1:
        computer_choice = "rock"
    elif x == 2:
        computer_choice = "paper"
    elif x == 3:
        computer_choice = "scissors"

    user_choice = input ()

    print ("computer choice: ", computer_choice)
    print ("user choice: ", user_choice)

    if computer_choice == "rock" and user_choice == "paper":
        user_score = user_score +1

    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score = computer_score +1

    elif computer_choice == "paper" and user_choice == "rock":
        computer_score = computer_score + 1

    elif computer_choice == "paper" and user_choice == "scissors":
        user_score = user_score + 1

    elif computer_choice == "scissors" and user_choice == "rock":
        user_score = user_score + 1

    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score = computer_score + 1

print ("computer score:", computer_score)
print ("your score:", user_score)