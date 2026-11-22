
 #list
medicine =["panadol","arinac","brufen","calpol"]
"""
print(medicine[1])
print(medicine[2])
print(medicine[0])
print(medicine[3])
med = input("enter medicine")
medicine.append(med)
medicine.remove(medicine[0])
print(medicine)


for i in medicine:

    print(i)
    
"""
"""
med_dic = {'name':'panadol', 'price':'22', 'batch':"mns"}
print(med_dic)
meddd = input("enter medicine")
price= int(input("enter price"))
batch = input("enter batch")
user_med_dic = {'name':meddd, 'price':price, 'batch':batch}
print(user_med_dic)
"""
def input_medicine(medicine):
    medicine = input("enter medicine")
    return medicine
lisst=[]
for i in range(0,4):
    lisst.append(input_medicine(medicine))
print(lisst)