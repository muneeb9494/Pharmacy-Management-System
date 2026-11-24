import json

with open("Pharmacy-Management-System/data/medicines.json", "r") as f:
    medicines = json.load(f)

# search medicine by batch
def search():
    search_med = input("Enter batch to find medicine: ").strip().lower()
    for medicine in medicines["Medicines"]:
        if medicine["Batch"].lower() == search_med:
            return(medicine)


    return None

# changing stoke quantity
def Change_Quantity():
    medicine = search()
    new_qua = int(input("Enter new quantity of medicine to add: "))
    medicine["Quantity"] = new_qua
    with open("Pharmacy-Management-System/data/medicines.json", "w") as f:
        json.dump(medicines, f, indent=4)
    print("quantity changed sucessfully")
    print(medicine)
#changing batch of medicine
def Change_Batch():
    medicine = search()

    if medicine is None:
        print("Medicine not found")
        return
    new_batch = input("Enter new batch of medicine to add: ").strip()
    medicine["Batch"] = new_batch
    with open("Pharmacy-Management-System/data/medicines.json", "w") as f:
        json.dump(medicines, f, indent=4)
    print("batch changed sucessfully")
    print(medicine)
#deleting a medicine
def Del_medicine():
    medicine = search()

    if medicine is None:
        print("Medicine not found")
        return
    medicines["Medicines"].remove(medicine)
    with open("Pharmacy-Management-System/data/medicines.json", "w") as f:
        json.dump(medicines, f, indent=4)
    print("medicine deleted")
# adding new medicine
def New_Medicine():
    Name = input("enter medicine name: ")
    P_Price = int(input("enter medicine purchase price: "))
    S_price = int(input("enter medicine sell price: "))
    Batch = input("enter medicine Batch: ")
    Quantity = int(input("enter medicine quantity: "))
    new_med = {"Name": Name, "P_Price": P_Price, "S_price": S_price, "Batch": Batch, "Quantity": Quantity}
    medicines["Medicines"].append(new_med)
    with open("Pharmacy-Management-System/data/medicines.json", "w") as f:
        json.dump(medicines, f, indent=4)
    print("Medicine added successfully")


print("Welcome to Pharmacy Management System")
print("which option you like to choose \npress 1 To View All Medicines \npress 2 to Search Medicine \nPress 3 to Add New Medicine \nPress 4 to Update Medicine \npress 5 to Delete Medicine \npress 6 to Exit")
user_choise = int(input("Enter your choice: "))
if user_choise == 1:
    print(medicines)
elif user_choise == 2:
    search()
elif user_choise == 3:
    New_Medicine()
elif user_choise == 4:
    print("if you want to Update medicine batch press 1\n if you want to update Quantity press2")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Change_Batch()
    elif choice == 2:
        Change_Quantity()
elif user_choise == 5:
    Del_medicine()
elif user_choise == 6:
    print("Thank you for choosing Pharmacy Management System")