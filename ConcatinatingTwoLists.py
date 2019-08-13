length1=int(input("Enter a length of list 1: "))
list1=[]
list2=[]
length2=int(input("Enter a length of list 2: "))
for i in range(length1):
    num1=int(input("Enter a element of list 1: "))
    list1.append(num1)
for j in range(length2):
    num2=int(input("Enter a element of list 2: "))
    list2.append(num2)
list1.extend(list2)
print(list1)
