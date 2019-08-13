ch=input("Enter a Character: ")
a=ord(ch)
if(a>=97) and (a<=122):
    a=a-32
    ch=chr(a)
    print("In UPPERCASE: ",ch)
elif(a>=65) and (a<=90):
    a=a+32
    ch=chr(a)
    print("IN LOWERCASE: ",ch)
else:
    print("Inavlid Chracter")
