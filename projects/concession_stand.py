menu = {
    "pizza":230,
    "popcorn":300,
    "nachos":100,
    "fries":80,
    "chips":20,
    "pritzel":50,
    "soda":30,
    "lemonade":20,
}

cart = []
total = 0


print("---------MENU----------")
for key , value in menu.items():
    print(f"{key:10}: Rs {value}")
print("-----------------------")


while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break

    elif menu.get(food) is not None:
        cart.append(food)


print("-------YOUR ORDER-------")
print(cart)
for food in cart:
    total += menu.get(food)

print(f"Total = Rs {total}")

print("-------------------------")
