str1="ABCDEFGH"
str2="ate"
str3=""
join1="-".join(str1)
list1=join1.split("-")
for alpha in list1:
    str3=str3+(alpha+str2)+" "
print(str3)
