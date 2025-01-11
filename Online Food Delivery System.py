# 1. Store menu items as a dictionary where item names are keys and (Price, Category) is the value.
menu = {
    "Burger": (120, "Fast Food"),
    "Pizza": (250, "Fast Food"),
    "Pasta": (200, "Italian"),
    "Salad": (100, "Healthy"),
    "Ice Cream": (80, "Dessert"),
    "Coffee": (60, "Beverage"),
}

# 2. Create a list of orders where each order is a tuple (Order ID, Customer Name, Item List, Total Bill).
orders = []

# 3. Use a set to store unique customer names who have placed orders.
unique_customers = set()

# Function to display the menu
def display_menu():
    print("\n--- Menu ---")
    print("{:<20} {:<10} {:<10}".format("Item", "Price", "Category"))
    for item, (price, category) in menu.items():
        print(f"{item:<20} {price:<10} {category:<10}")

# Function to place an order
def place_order(order_id):
    customer_name = input("\nEnter your name: ")
    unique_customers.add(customer_name)  # Add customer to the unique customers set

    item_list = []
    total_bill = 0

    while True:
        display_menu()
        item_name = input("\nEnter item name to add to your order (or 'done' to finish): ").strip()

        if item_name.lower() == "done":
            break

        if item_name in menu:
            item_list.append(item_name)
            total_bill += menu[item_name][0]
            print(f"Added '{item_name}' to your order. Current Total: {total_bill}")
        else:
            print("Item not found in the menu. Please try again.")

    if item_list:
        # Add the order to the list of orders
        orders.append((order_id, customer_name, item_list, total_bill))
        print(f"\nOrder placed successfully! Your Total Bill: {total_bill}")
    else:
        print("No items selected. Order not placed.")

# Function to display total revenue generated from all orders
def display_total_revenue():
    total_revenue = sum(order[3] for order in orders)  # Sum up the total bill of all orders
    print(f"\nTotal Revenue Generated: {total_revenue}")

# Function to display the list of unique customers who have placed orders
def display_unique_customers():
    print("\nUnique Customers:")
    for customer in unique_customers:
        print(customer)

# Menu-driven program
order_id = 1
while True:
    print("\n--- Online Food Delivery System ---")
    print("1. Place an Order")
    print("2. Display Total Revenue")
    print("3. Display Unique Customers")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        place_order(order_id)
        order_id += 1
    elif choice == "2":
        display_total_revenue()
    elif choice == "3":
        display_unique_customers()
    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")