n=int(input("Please input a number larger than 2\n"))
y=2
while y<n/2:
    if n%y!=0:
        y=y+1
        break
    else:
        print("It is not a prime number.")
        
print("It is a prime number.")
    

    
    
    
