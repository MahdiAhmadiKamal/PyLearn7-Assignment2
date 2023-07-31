
a = 1
b = 1

n = int (input("enter the number of terms: "))

if n == 1:
    print (a)

elif n ==2:
    print (a)
    print (b)

else:
    print (a)
    print (b)
    
    for i in range (n-2):

        c = a + b
    
        print (c)

        a = b
        b = c