num=str(input("Enter a program: "))
p=0
n=0
sp=0
sn=0
while(num!='@'):
    n=int(num)
    if(n<0):
        n=n+1
        sn=sn+n
    elif(n>0):
        p=p+1
        sp=sp+p
    else:
        print("Invalid")
    num=str(input("Enter a number: "))
avgp=sp/p
avgn=sn/n

print("negatives avg: ",avgn)

print("positives avg: ",avgp)    
