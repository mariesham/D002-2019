a=[]
y=0
while y<10:
    L=input("Please enter a word.\n")
    if L[0]=="A" or L[0]=="E" or L[0]=="I" or L[0]=="O" or L[0]=="U" or L[0]=="a" or L[0]=="e" or L[0]=="i" or L[0]=="o" or L[0]=="u":
        a.append(L)
        y=y+1
    else:
        y=y+1
while y==10:
    print(a)
    break
