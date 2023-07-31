
count = 0
total = 0

while True:

    score = input(("enter student's score: "))

    if score == "exit":
        break
    else:
        score = float (score)
        total = total + score
    
    print ("total score is: ",total)

    count = count + 1

print ("average:" ,total/count)
print ("The End.")