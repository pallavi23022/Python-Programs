#Q.2 WAP that forms a list of  first characater of every word in another list 
#Create a list of numbers until user enters @ create a list of the given list
#such that no duplicate entries exists
list1=[]
first=[]
result=[]
num=int(input("Enter the length of list: "))
for i in range(num):
    string=input("ENter element: ")
    list1.append(string)
for words in list1:
    f=words[0:1]
    first.append(f)
print("List contains first letter of each word is : ",first)
'''
for letter in range(len(first)):
    for j in range(letter+1,len(first)):
        if(first[letter]!=first[j]):
            if( first[letter].isupper() ) and ( first[letter]==first[j].upper() ):
                result.append(first[letter])
            if ( first[letter].islower() ) and (first[letter]==first[j].lower() ):      
                result.append(first[letter]);'''

for l in range(len(first)):
    result.append(first[l].upper())

set1=set(result)
        
print("Unique list: ",set1)
