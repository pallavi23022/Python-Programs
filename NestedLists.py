list1=[ [input(),float(input())] for _ in range( int( input() ) ) ]
second=-8963.25
first=-8968.25
for i in range(len(list1)):
    if (list1[i][1])>first:
        first=list1[i][1]
    if(list1[i][1]!=first)and(second<list1[i][1]):
        second=list1[i][1]
            
name=[]
for a,b in list1:
    if(b==second):
        name.append(a)
name.sort()

print('\n'.join([n for n in name]))
    
