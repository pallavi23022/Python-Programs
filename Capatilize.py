string=input("Enter a String: ")
list1=string.split(" ")

for word in list1:
    mid=word[1:]
    f=word[0].capitalize()
    f=f+mid
    last=f[:-1]
    l=f[-1].capitalize()
    l=last+l
    print(l,end=" ")
    
