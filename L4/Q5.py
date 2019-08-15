def printer(secret, opened):
    i=0
    x=[]
    while i < len(secret):
        if i in opened:
            a=secret[i]
            x.append(a)
        else:
            x.append('_')
        i= i + 1
    print(x)

printer("avocado",[0,3])
