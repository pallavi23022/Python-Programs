str1="without,hello,python,world"
list1=str1.split(",")
for i in range(len(list1)):
    j=i+1
    for j in range(len(list1)):
        if(list1[i]<list1[j]):
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
print(list1)
    
    
