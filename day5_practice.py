import json
import functions
from datetime import datetime

def Save_Purchase_History():

    with open("Pharmacy-Management-System/data/purchases.json", "r") as f:
        purchases = json.load(f)

    Name = input("Enter medicine name: ")
    Batch = input("Enter medicine batch: ")
    P_Price = float(input("Enter purchase price: "))
    Quantity = int(input("Enter purchased quantity: "))

    Total = P_Price * Quantity

    Purchase_ID = len(purchases) + 1

    Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    purchase_record = {
        "Purchase_ID": Purchase_ID,
        "Name": Name,
        "Batch": Batch,
        "P_Price": P_Price,
        "Quantity": Quantity,
        "Total": Total,
        "Date": Date
    }

    purchases.append(purchase_record)

    with open("Pharmacy-Management-System/data/purchases.json", "w") as f:
        json.dump(purchases, f, indent=4)

    print("\nPurchase recorded successfully!")
    print("Purchase ID:", Purchase_ID)
    print("Medicine:", Name)
    print("Total purchase amount:", Total)
    print("Purchase date:", Date)


Save_Purchase_History()

"""
def Purchased_order():
    medicine = functions.search()
    if medicine is None:
        print("No medicine found")
        print("Please add new medicine")
        return
    else:
        Purchased_medicine = int(input("Enter quantity of medicine purchased: "))
        medicine["Quantity"] += Purchased_medicine
    with open("Pharmacy-Management-System/data/medicines.json", "w") as f:
        json.dump(functions.medicines, f, indent=4)
    print("quantity changed sucessfully")
Purchased_order()

"""
