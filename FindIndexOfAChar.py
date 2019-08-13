str1=input("Enter a String: ")
char=input("Enter a Character: ")
joinstr="-".join(str1)
list1=joinstr.split("-")
index=0
for i in range(len(list1)):
    if(char==list1[i]) or ( char==chr(ord(list1[i])+32) ) or (char==chr( ord(list1[i])-32) ):
        index=i
        #break
print(char," is present at ",i,"index")
