print("Enter a number: ")
num=int(input())
n=0
p=0
z=0
while(num != -1 ):
    if(num<0):
        n=n+1
    elif(num>0):
        p=p+1
    elif(num==0):
        z=z+1
    else:
        print("Invalid choice")
    num=int(input())

print("positives: ",p,"Negatives: ",n,"Zeroes: ",z)

    
