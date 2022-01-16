from datetime import datetime, time

inp = [  
    {
    "item": "Headache pills",
    "itemCategory": "Medicine",
    "quantity": 5,
    "price": 50
    },
    {
    "item": "Sandwich",
    "itemCategory": "Food",
    "quantity": 2,
    "price": 200
    },
    {
    "item": "Perfume",
    "itemCategory": "Imported",
    "quantity": 1,
    "price": 4000
    },
    {
    "item": "Black Swan",
    "itemCategory": "Book",
    "quantity": 1,
    "price": 300
    }
]
def tax_percent(a,b):
    if a == "Medicine" or a == "Food":
        return 5
    elif a == "Clothes":
        if b < 1000:
            return 5
        else:
            return 12
    elif a == "Music":
        return 3
    elif a == "Imported":
        return 18
    elif a == "Book":
        return 0  
total_tax = 0
amount_payable = 0 
for opt in inp:
    tax_rate = tax_percent(opt["itemCategory"], opt["price"])   
    tax = ((tax_rate/100)*opt["price"]) 
    finalPrice = opt["price"] + tax
    opt["taxRate"] = tax_rate
    opt["tax"] = tax
    opt["finalPrice"] = finalPrice
    total_tax = total_tax + tax
    amount_payable = amount_payable + finalPrice
if amount_payable > 2000:
    amount_payable = amount_payable - ((5/100)*amount_payable)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
det = []
for i in range(len(inp)):
    det.append("  " + inp[i]['item'] + "  Price : " + str(inp[i]['price']) + "  Tax_Rate : " + str(inp[i]['taxRate']) + " Tax_Amount : " + str(inp[i]['tax']) )
det.sort()
print("\n \t \t Receipt: ")
print("\t Time:",dt_string)
for i in det:
    print(i)
print("\t Total_Tax=",total_tax)
print("\t Amount_Payable=",amount_payable)
