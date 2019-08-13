#input function stores a variable stores a variable in the form of string 
#so we always type cast it into the specific type required by the user
#17 july 2019
print("Enter first real number")
ar=int(input())
print("Enter first imaginary number")
ai=int(input())
print("Enter second real number")
br =int(input())
print("Enter second imaginary number")
bi=int(input())

c1=complex(ar,ai)
c2=complex(br,bi)

c3=c1+c2
print(c3)


