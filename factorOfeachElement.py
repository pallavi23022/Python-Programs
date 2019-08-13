num=int(input("ENter a number: "))
list1=[]
modified=[]
while(num!=0):
    list1.append(num)
    modified.append(num*10)
    num=int(input("ENter a number: "))
    
print(list1)
print(sorted(list1)," :sorted list")
print(modified)
print(sorted(modified),": modified list")
    

