med_name = input("enter medcine name ?")
pur_price = float(input("enter purchase price ?"))
quantity = int(input("enter quantity ?"))

print("Medicine name is :",med_name)
print("Purchase price is : $",pur_price)
if quantity<=0:
    print("Medicine is not available")
else:
    print("Total quantity is :",quantity)
    print("total stock value is ", pur_price*quantity)