salary=float(input("Enter Salary: "))
gender=input("Enter Gender: ")

if(gender=="male"):
    salary=salary+ ( (5/100)*salary)
    if(salary> 10000):
        print("YOu Gross SAlary is: ",salary)
    else:
        print("YOu got extra 2% bonus")
        salary=salary + (0.02 * salary)
        print("You net Salary is: ",salary)
else:
    salary=salary+ ( (10/100)*salary)
    if(salary> 10000):
        print("YOu Gross SAlary is: ",salary)
    else:
        print("YOu got extra 2% bonus")
        salary=salary + (0.02 * salary)
        print("You net Salary is: ",salary)
