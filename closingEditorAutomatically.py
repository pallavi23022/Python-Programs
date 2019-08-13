import random
c=0
num=random.randint(1,10)
print("The number is: ",num)
for i in range(1,num+1,1):
    if(num%i==0):
        c=c+1
if(c==2):
    print("Prime")
    print("Bye Bye.....")
    exit(0)
else:
    print("Not prime")
