string=input("Enter String: ")
copies=int(input("Enter number of copies to be printed: "))
l=int(input("Enter length to be extracted: "))
for i in string:
    slice=string[0:l]
print(slice*copies)
