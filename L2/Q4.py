a=1
b=1
c=1

while a<60 and b<60 and c<60:
    d=60-a-b-c
    a=a+1
    b=b+1
    c=c+1
    print(a*b+b*c+c*d)

    max=0
    for n in [a*b+b*c+c*d]:
        if n>max:
            max=n

print("Max=%d"%max)
