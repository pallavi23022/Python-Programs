print("This is the program to find greatest number")
one=float(input("Enter 1st number: "))
two=float(input("Enter 2nd number: "))
three=float(input("Enter 3rd number: "))

if(one>two):
    if(one>three):
        print("The largest number of ",one,two,three, "is",one)
    else:
        print("The largest number of ",one,two,three, "is",three)
else:
    if(two>three):
        print("The largest number of ",one,two,three, "is",two)
    else:
        print("The largest number of ",one,two,three, "is",three)
