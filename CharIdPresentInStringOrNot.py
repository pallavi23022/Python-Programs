str1=input("Enter a String: ")
char=input("Enter a Character: ")
joinstr="-".join(str1)
list1=joinstr.split("-")
c=0
for ch in list1:
    if(char==ch) or ( char==chr(ord(ch)+32) ) or (char==chr( ord(ch)-32) ):
        c=c+1
print(char," is present ",c,"times")
