#Q.3 create a list of numbers in a specified range as emtered by the user
#reverse the list and print its values also take an inut of number of steps
#Step is skip
num1=int(input("Enter starting number: "))
num2=int(input("Enter ending number: "))
steps=int(input("Enter steps: "))   
list1=[]
for i in range(num1,num2+1,steps):
    list1.append(i);
list1.reverse()
print(list1)

