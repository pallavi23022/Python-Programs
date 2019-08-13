x=int(input("Enter x: "))
y=int(input("Enter y: "))
m=int(input("Enter m: "))
list1=[ (( ( x+(x**y) )/ 2*m )+3) for x in range(100) ]
print(list1)
