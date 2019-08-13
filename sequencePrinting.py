c=50
h=30
q=0
str1=""

for i in range(0,3,1):
    d=int(input(" Enter a Number: "))    
    q=int(((2*c*d)/h)**(1/2))
    str1=str1+str(q)+","
   
print(str1)
