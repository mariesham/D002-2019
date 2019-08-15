secret=input("Enter a word.\n")
opened=int(input("Enter the indexes of the letters to be revealed.\n"))
def printer(secret, opened):
    i=0
    x=[]
    while i < len(secret):
        if i == opened:
            a=secret[i]
            x.append(a)
        else:
            x.append('_')
        i= i + 1
    print(x)

printer(secret, opened)
# Note: you might use print(x, end="") to print x without changing line
