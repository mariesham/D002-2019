n=int(input("Input a number\n"))
def factors(n):
    list=[]
    for x in range(1, n + 1):
        if n % x == 0:
           list.append(x)
    return (list)

print(factors(n))

   



