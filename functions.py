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
    for medicine in medicines["Medicines"]:
        if medicine["Name"].lower() == Name.lower() or medicine["Batch"].lower() == Batch.lower():
            print("medicine already exists")
            break
    else:
        new_med = {"Name": Name, "P_Price": P_Price, "S_price": S_price, "Batch": Batch, "Quantity": Quantity}
        medicines["Medicines"].append(new_med)
        with open("Pharmacy-Management-System/data/medicines.json", "w") as f:
            json.dump(medicines, f, indent=4)
        print("Medicine added successfully")