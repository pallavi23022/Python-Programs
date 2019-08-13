quantity=float(input("Enter quantity"))
value=float(input("Enter price"))* quantity
discount=float(input("Enter discount percentage"))
tax=float(input("Enter tax amount percentage"))

bill= value-( (discount/100)*value )+ ( (tax/100)*value )
print("Total bill: " , bill)




