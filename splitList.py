length=int(input("Enter length of a list: "))
list1=[]
list2=[]
srange=int(input("ENter range of splitting: "))
for i in range(length):# makine a list
    num=int(input("Enter a number"))
    list1.append(num)

for i in range(len(list1)):
    list2.append(list1[0:srange])#appending srange into a new list
    del list1[0:srange]#deleting the range elements from list1
for i in list2:
    if(i==[]):
        list2.remove(i)
print(list2)
#print(list2[0][2])
