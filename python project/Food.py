import streamlit as st
import pandas as pd
from fpdf import FPDF
import os

# Function to load menu from session state or CSV
def load_menu():
    menu_file = "menu.csv"
    if not os.path.exists(menu_file):
        # Initialize CSV file if it doesn't exist
        menu = pd.DataFrame({
            "Item": ["Burger", "Pizza", "Pasta", "Salad"],
            "Price": [5.99, 8.99, 7.49, 4.99]
        })
        menu.to_csv(menu_file, index=False)
    else:
        menu = pd.read_csv(menu_file)
    return menu

# Function to save menu to CSV
def save_menu(menu):
    menu.to_csv("menu.csv", index=False)

# Admin Panel - For adding and deleting items
def admin_panel():
    st.title("Admin Panel")

    # Admin credentials
    admin_username = "admin"
    admin_password = "admin123"

    # Admin login form
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        with st.form(key="login_form"):
            username_input = st.text_input("Username", "")
            password_input = st.text_input("Password", "", type="password")
            login_button = st.form_submit_button("Login")

            if login_button:
                if username_input == admin_username and password_input == admin_password:
                    st.session_state.logged_in = True
                    st.success("Login successful! Welcome to the Admin Panel.")
                else:
                    st.error("Incorrect username or password. Please try again.")
    else:
        # Load menu from CSV file
        menu = load_menu()

        # Adding New Menu Item
        with st.form(key="add_item_form"):
            new_item = st.text_input("New Item Name")
            new_price = st.number_input("Price", min_value=0.01, step=0.01)
            submit_button = st.form_submit_button(label="Add Item")

            if submit_button:
                if new_item and new_price:
                    new_row = {"Item": new_item, "Price": new_price}
                    menu = pd.concat([menu, pd.DataFrame([new_row])], ignore_index=True)
                    save_menu(menu)  # Save the updated menu to CSV
                    st.session_state.menu = menu
                    st.success(f"{new_item} added to the menu!")

        # Deleting Menu Item
        item_to_delete = st.selectbox("Select Item to Remove", menu["Item"].tolist())
        delete_button = st.button("Delete Item")

        if delete_button:
            menu = menu[menu["Item"] != item_to_delete]
            save_menu(menu)  # Save the updated menu to CSV
            st.session_state.menu = menu
            st.success(f"{item_to_delete} has been removed from the menu.")

        # Display current menu after modifications
        st.write("### Current Menu")
        st.write(menu)

        # Log out button
        if st.button("Log out"):
            st.session_state.logged_in = False
            st.rerun()  # Use this instead of st.experimental_rerun()

# User Panel - For ordering items
def user_panel():
    st.title("Online Food Ordering")

    # Collect User Details
    if "user_details" not in st.session_state:
        st.session_state.user_details = {}

    if not st.session_state.user_details:
        user_name = st.text_input("Name")
        phone_number = st.text_input("Phone Number")
        address = st.text_area("Address")

        if st.button("Enter"):
            if user_name and phone_number and address:
                st.session_state.user_details = {
                    "Name": user_name,
                    "Phone": phone_number,
                    "Address": address
                }
                st.write(f"### Your Details")
                st.write(f"Name: {user_name}")
                st.write(f"Phone: {phone_number}")
                st.write(f"Address: {address}")
            else:
                st.error("Please fill in all the details before proceeding.")
    else:
        user_name = st.session_state.user_details["Name"]
        phone_number = st.session_state.user_details["Phone"]
        address = st.session_state.user_details["Address"]

        st.write(f"### Your Details")
        st.write(f"Name: {user_name}")
        st.write(f"Phone: {phone_number}")
        st.write(f"Address: {address}")

    # Load menu automatically after entering details
    menu = load_menu()

    # Initialize cart list if not already in session state
    if "cart" not in st.session_state:
        st.session_state.cart = []

    # Display the menu and allow users to add items to their cart
    for index, row in menu.iterrows():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader(row["Item"])
            st.write(f"💰 Price: ${row['Price']}")
        with col2:
            # Set default quantity to 0, allow the user to adjust
            quantity_key = f"quantity_{index}"  # Key for this item's quantity input
            current_quantity = st.session_state.get(quantity_key, 0)  # Default to 0 if not set

            # Use number_input for quantity
            quantity = st.number_input(f"Quantity ({row['Item']})", min_value=0, step=1, key=quantity_key, value=current_quantity)

            # Update cart if quantity > 0
            if quantity > 0:
                # Check if the item already exists in the cart
                item_in_cart = next((item for item in st.session_state.cart if item['Item'] == row["Item"]), None)
                if item_in_cart:
                    item_in_cart['Quantity'] = quantity  # Update quantity if item exists
                else:
                    st.session_state.cart.append({"Item": row["Item"], "Price": row["Price"], "Quantity": quantity})

    # If cart has items, display the cart
    if st.session_state.cart:
        st.write("### Your Cart")
        cart_df = pd.DataFrame(st.session_state.cart)
        cart_df["Total"] = cart_df["Price"] * cart_df["Quantity"]
        st.write(cart_df)

        total = cart_df["Total"].sum()
        st.write(f"Total: ${total:.2f}")

        # Button to finalize order
        if st.button("Place Order"):
            st.write("Order placed successfully!")

            # Generate the bill as a PDF
            generate_pdf(user_name, phone_number, address, cart_df, total)

            # Clear the cart after order is placed
            st.session_state.cart = []

    else:
        st.write("Your cart is empty.")

# Function to generate PDF bill
def generate_pdf(user_name, phone_number, address, cart_df, total):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set font for the title
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Order Bill", ln=True, align="C")

    # Set font for the content
    pdf.set_font("Arial", size=12)

    # Add user details
    pdf.ln(10)
    pdf.cell(100, 10, txt=f"Name: {user_name}", ln=True)
    pdf.cell(100, 10, txt=f"Phone: {phone_number}", ln=True)
    pdf.cell(100, 10, txt=f"Address: {address}", ln=True)

    # Add order details
    pdf.ln(10)
    pdf.cell(100, 10, txt="Item", border=1)
    pdf.cell(30, 10, txt="Price", border=1)
    pdf.cell(30, 10, txt="Quantity", border=1)
    pdf.cell(30, 10, txt="Total", border=1)
    pdf.ln(10)

    # Add cart items
    for index, row in cart_df.iterrows():
        pdf.cell(100, 10, txt=row["Item"], border=1)
        pdf.cell(30, 10, txt=f"${row['Price']}", border=1)
        pdf.cell(30, 10, txt=str(row["Quantity"]), border=1)
        pdf.cell(30, 10, txt=f"${row['Total']:.2f}", border=1)
        pdf.ln(10)

    # Add total amount
    pdf.ln(10)
    pdf.cell(160, 10, txt="Total Amount", align="R")
    pdf.cell(30, 10, txt=f"${total:.2f}", border=1)

    # Save the PDF to a file
    pdf.output("order_bill.pdf")

    # Provide a download link
    with open("order_bill.pdf", "rb") as f:
        st.download_button(
            label="Download Bill",
            data=f,
            file_name="order_bill.pdf",
            mime="application/pdf"
        )

# Main function to control the flow
def main():
    menu = load_menu()

    # Select the mode (Admin or User)
    mode = st.sidebar.radio("Select Mode", ["User", "Admin"])

    if mode == "Admin":
        admin_panel()
    elif mode == "User":
        user_panel()

if __name__ == "__main__":
    main()
