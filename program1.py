#Q 2. WAP to create list of numbers divisible by 4  or 13
#all th eelements of the list should lie in the range from 200 to 500
list1=[]
for num in range(200,501,1):
    if(num%4==0) or (num%13==0):
        list1.append(num)
print(list1)
