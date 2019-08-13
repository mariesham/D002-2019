#As there are two Q6 for L2 (one in Lecture slides and one as a skeleton code)and the instructions to make this program is a bit unclear, I have combined both assignments.
import random
count=0
n = random.randint(1,100)

print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid. You have 3 chances.''')
while count <3:
    y=int(input("What is your guess?\n"))
    if y!= n:
        if (n-y)<10 and (y-n)<10:
            print("You are quite close. Try again!")
            count=count+1
        elif (y-n)>10:
            print("Your guess is too high. Try again!")
            count=count+1
        elif (n-y)>10:
            print("Your guess is too low. Try again!")
            count=count+1





while count ==3 or n==y:
    if n==y:
        print('You got the correct guess in %d trials' % count)
        print('Dave\'s banana are now all yours!')
        break
    else:
        print("You failed to find the number of bananas. Dave hid %d bananas. Try again next time!"%n)
        break
