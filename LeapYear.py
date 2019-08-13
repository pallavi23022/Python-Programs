year=int(input("Enter Year: "))

if year%4==0 and (year%100)!=0 :
    print("It is a Leap Year")
elif year%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
