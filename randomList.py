import random
list1=[]
even=[]
odd=[]
r=0
for i in range(10):
    r=int((random.random())*10)
    list1.append(r)
print(list1)

even=[num for num in list1 if (num%2)==0 ]
print("Even list: ",even)
odd=[num for num in list1 if (num%2)!=0 ]
print("odd list: ",odd)


