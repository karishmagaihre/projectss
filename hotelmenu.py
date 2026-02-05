
menu = {
    'Pizza': 50,
    'Pasta': 80,
    'Burger': 100,
    'Coffee': 80,
    'Mo:mo': 150,
    'Chowmein': 60
}

print("Welcome to our restaurant 🍽️")
print("Menu:")
for item, price in menu.items():
    print(f"{item} : Rs.{price}")

order_total = 0

while True:
    item = input("\nWhat would you like to order? = ")

    if item in menu:
        order_total += menu[item]
        print(f"Thank you for your order 😊 ({item} added)")
    else:
        print("Sorry, we do not have that item available.")
        print("Could you please order something else?")
        continue   

    another_order = input("Do you want to order something else? (Yes/No) = ")

    if another_order.lower() == "no":
        break

print(f"\nThe total amount to pay is Rs.{order_total}")
print("Thank you for visiting our restaurant ❤️")
