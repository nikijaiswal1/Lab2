products = {}

def add_product():
    name = input("Enter product name: ").strip().lower()
    if name in products:
        print("Product already exists.")
    else:
        try:
            price = float(input("Enter price: "))
            products[name] = price
            print("Product added successfully.")
        except ValueError:
            print("Invalid price. Try again.")

def update_price():
    name = input("Enter product name to update: ").strip().lower()
    if name in products:
        try:
            new_price = float(input("Enter new price: "))
            products[name] = new_price
            print("Price updated successfully.")
        except ValueError:
            print("Invalid price.")
    else:
        print("Product not found.")

def find_in_price_range():
    try:
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        found = False
        print(f"Products in price range {min_price} - {max_price}:")
        for name, price in products.items():
            if min_price <= price <= max_price:
                print(f"{name} : {price}")
                found = True
        if not found:
            print("No products found in this range.")
    except ValueError:
        print("Invalid price range.")

def display_all():
    if not products:
        print("No products available.")
    else:
        print("Product List:")
        for name, price in products.items():
            print(f"{name} : {price}")

while True:
    print("\n=== Product Management Menu ===")
    print("1. Add New Product")
    print("2. Update Product Price")
    print("3. Find Products in Price Range")
    print("4. Display All Products")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_product()
    elif choice == '2':
        update_price()
    elif choice == '3':
        find_in_price_range()
    elif choice == '4':
        display_all()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select from 1 to 5.")
