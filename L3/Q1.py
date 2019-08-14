from math import *

people = int(input("How many people are sharing the bill?\n"))
bill = float(input("How much is the bill?\n"))
print("Kevin paid the bill first. But Kevin only has 100 dollar notes")
print("So Kevin is going to paid $%d." % (ceil(bill/100)*100))
print("The cafe is giving %f to Kevin." % ((ceil(bill/100)*100)-(bill)))  
print("Each one should give %f to Kevin." % ((ceil(bill/100)*100)/people))


number = 1
while number <= 100:
    if number%7==0 or number - (round(number/10)*10)==7:   
        print('X', end=' ')
    else:
        print(number, end=' ')    
    number = number + 1
print("\nGame Over.")

from random import randint
number = randint(1,6)
print("I got a %d" % number)
count = 1
while number !=6: # replace with your code
    # Write some more code
    number = randint(1,6)
    print("I got a %d" % number)
    count = count + 1

print("Oh, it takes me %d times to get a 6!!!" % count)



from random import randint
times=0
a=[]
while times<100:
        count=0
        number=randint(1,6)
        while number!=6:
                number = randint(1,6)
                count = count + 1

        count=count+1
        print("Oh, it takes me %d trials to get a 6!!!" % count)
        a.append(count)
        times=times+1
        continue
while times==100:
        b=sum(a)
        print("The average is %f."%((sum(a))/100))
        break




