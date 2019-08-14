import random
count1=0
count2=0
n = random.randint(1,100)

print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid. Players have to compete bewteen each other to see who can guess the number of bananas first!.''')
while n>0:
    y=int(input("Player 1 input your guess:"))
    if y!=n:
        if (n-y)<10 and (y-n)<10:
            print("You are quite close. Try again!")
            count1=count1+1
        elif (y-n)>10:
            print("Your guess is too high. Try again!")
            count1=count1+1
        elif (n-y)>10:
            print("Your guess is too low. Try again!")
            count=count1+1


    x=int(input("Player 2 input your guess:"))
    if x != n:
        if (n-y)<20 or (y-n)<20:
          print("You are quite close. Try again!")
          count2=count2+1
        elif (x-n)>10:
            print("Your guess is too high. Try again!")
            count2=count2+1
        elif (n-x)>10:
            print("Your guess is too low. Try again!")
            count2=count2+1
    if y==n:
        print("Player 1 wins! You tried %d times!"%count1)
        break
    if x==n:
        print("Player 2 wins! You tried %d times!"%count2)
        break

    continue
