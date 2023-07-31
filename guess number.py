import random

computer_number = random.randint (10,40)
count = 0

while True:
    
    user_number = int (input())
    count = count +1

    if computer_number == user_number:
        print ("Congratulations, you won.")
        print ("🎉")
        print ("You succeeded after", count, "tries")
        break

    elif computer_number > user_number:
        print ("Go up. ⬆")
    
    elif computer_number < user_number:
        print ("Go down. ⬇")