
str1=input("Enter a String: ")
str2="-".join(str1)
list1=str2.split("-")
for i in range(len(list1)):
    c=0
    #print("loop1")
    for j in range(i+1,len(list1)):
        #print("loop2")
        if(list1[j]!='0'):
            if(list1[i]==list1[j]):
                c=c+1
                list1[j]='0'
    if(list1[i]!='0'):
        print(list1[i],": ",c+1,end=" ")

/**********
str1=input("Enter a String: ")
dict1={}
for i in str1:
    keys=dict1.keys()
    if i in keys:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)
