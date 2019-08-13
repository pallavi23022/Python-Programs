print("Calculate sum and avg of first 10 numbers: ")
num=1
sum1=0
c=0
while (num<=10):
    if (num%2==0):
        sum1=sum1+num
        c=c+1
    num=num+1
        
avg=sum1/c

print("Sum is: ",sum1)
print("Average is: ",avg)
