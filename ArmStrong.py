num=int(input("Enter a number: "))
c=0
n=num
n1=num
sum1=0
while(num>=1):# tb tk chle jb tl num greater than 1 hai
    r=num%10
    c=c+1
    num=int(num/10)

while(n>=1):
    re=n%10
    #print("re: ",re)
    sum1=sum1+(re**c)
    n=int(n/10)
   # print("sum inside while: ",sum1)
    #print("n: ",n)
#print("sum1: ",sum1)
if(sum1==n1):
    print("ArmStrong Number!!")
else:
    print("Not !!!")
    
    
