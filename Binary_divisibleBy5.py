str1=input("Enter four digit comma seperated number")
list1=str1.split(",")
l=[]
for num in list1:
    dec=int(num,2)
    if(dec%5==0):
        l.append(num)
print(",".join(l))
