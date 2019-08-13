list1=[]
length=int(input("Enter length of list: "))
for i in range(length):
    num=int(input("Enter a element: "))
    list1.append(num)


l=[ [list1[i],list1[j],list1[k]] for i in range(length) for j in range(i+1,length) for k in range(j+1,length) if(list1[i]+list1[j]+list1[k])==0 ]
print(l)
