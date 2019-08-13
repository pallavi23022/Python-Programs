#1. WAP which can find all such numbers which are divisible by seven but are
#not multiple of 5 between 2000 to 3200 both inclusive. Print the numbers in
#the form of comma seperated sequence


str1=""
for i in range(2000,3200,1):
    if(i%7==0) and (i%5!=0):
        str1=str1+str(i)+","    
   
        
print(str1)
