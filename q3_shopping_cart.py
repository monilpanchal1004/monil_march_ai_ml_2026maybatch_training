def create_cart(owner, discount=0):
    cart = {
        "owner": owner,
        "items": [],
        "discount": discount
    }
    return cart
def add_to_cart(cart):
    name = input("Enter Item Name : ")
    price = float(input("Enter Item Price : "))
    qty = int(input("Enter Quantity : "))

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }
    cart["items"].append(item)
    print("Item Added")
def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total = total + (item["price"] * item["qty"])
    discount_amount = (total * cart["discount"]) / 100
    final_total = total - discount_amount
    return final_total
owner = input("Enter Customer Name : ")
discount = float(input("Enter Discount Percentage : "))
cart = create_cart(owner, discount)
n = int(input("How many items do you want to add? : "))
for i in range(n):
    print("\nEnter Item", i + 1)
    add_to_cart(cart)
print("\n----- CART DETAILS -----")
print("Customer :", cart["owner"])
print("\nItems:")
for item in cart["items"]:
    print(item["name"], "-", item["price"], "x", item["qty"])
total = calculate_total(cart)
print("\nFinal Total :", total)
