length=int(input("Enter the length of list: "))
list1=[]
str1=""
for num in range(length):
    n=int(input("Enter a number: "))
    list1.append(n)
for l in list1:
    str1=str1+str(l)
print("converted number: ",int(str1))
if(int(str1)>0):
    print("perfect")
