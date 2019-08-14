sentence=input("What is the word?\n")
letter=input("Which letter?\n")
def checker(sentence, letter):
    result=[]
    for i in range(0,len(sentence)):
            if letter==sentence[i]:
                a=i
                result.append(a)
     
    return result
print(checker(sentence,letter))
    
    
