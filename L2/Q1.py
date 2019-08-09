n=int(input("Please input a number larger than 2\n"))
x=2
y=0
while x<n:
    if n%x>0:
       x=x+1
       y=1
       continue
    else:
        print("It is not a prime number.")
        y=0
        break
if y==1:
    print("It is a prime number")
        
