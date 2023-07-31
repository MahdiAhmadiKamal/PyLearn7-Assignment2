import random

dice_number = random.randint (1, 6)

while dice_number != 6:
    print (dice_number)
    break
else:
    while dice_number == 6:

        print (dice_number,"Congratulations")
        dice_number2 = random.randint (1, 6)
        dice_number = dice_number2
        print ("your bonus:", dice_number)
    