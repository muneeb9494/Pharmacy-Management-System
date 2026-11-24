import json

with open("Pharmacy-Management-System/data/medicines.json", "r") as f:
    medicines = json.load(f)

Name = input("enter medicine name: ");
P_Price= int(input("enter medicine purchase price: "));
S_price =int(input("enter medicine sell price: "));
Batch= input("enter medicine Batch: ");
Quantity= int(input("enter medicine quantity: "));
new_med={"Name": Name,"P_Price":P_Price,"S_price":S_price,"Batch":Batch,"Quantity":Quantity }
medicines["Medicines"].append(new_med)
with open("Pharmacy-Management-System/data/medicines.json", "w") as f:
    json.dump(medicines, f, indent=4)
print(medicines)