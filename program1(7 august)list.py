#Q.1 WAP that creates a list of words by combining the words
#in two individual lists
list1=['a','b','c','d']
list2=['1','2','3']
list3=[]
str1=[]
str1=list1[len(list2):]
for i in range(len(list1)):
    for j in range(len(list2)):
        if(i==j):
            string=list1[i]+list2[j]
            list3.append(string)
        
print(list3)
