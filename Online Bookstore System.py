import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def calculate_price(self):
        return self.price

class EBook(Book):
    def __init__(self, title, author, genre, price, tax_rate):
        super().__init__(title, author, genre, price)
        self.tax_rate = tax_rate

    def calculate_price(self):
        return self.price * (1 + self.tax_rate)

class PrintedBook(Book):
    def __init__(self, title, author, genre, price, shipping_cost):
        super().__init__(title, author, genre, price)
        self.shipping_cost = shipping_cost

    def calculate_price(self):
        return self.price + self.shipping_cost

class CustomerOrder:
    def __init__(self, customer_name, customer_email, payment_details):
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.__payment_details = payment_details
        self._order_items = []

    def add_book(self, book):
        price = book.calculate_price()
        self._order_items.append({
            'title': book.title,
            'price': price
        })

    def calculate_total(self):
        return sum(item['price'] for item in self._order_items)

    def get_order_details(self):
        return {
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'items': self._order_items,
            'total': self.calculate_total()
        }

class Bookstore:
    def __init__(self):
        self.books = []
        self.orders = []

    def add_book(self, book):
        self.books.append(book)

    def process_order(self, order):
        self.orders.append(order)

    def get_total_revenue(self):
        return sum(order.calculate_total() for order in self.orders)

    def import_books_from_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        title = row['title']
                        author = row['author']
                        genre = row['genre']
                        price = float(row['price'])
                        book_type = row['type'].lower()
                        
                        if book_type == 'ebook':
                            tax_rate = float(row.get('tax_rate', 0.1))
                            book = EBook(title, author, genre, price, tax_rate)
                        elif book_type == 'printed':
                            shipping_cost = float(row.get('shipping_cost', 5.0))
                            book = PrintedBook(title, author, genre, price, shipping_cost)
                        else:
                            continue
                        self.add_book(book)
                    except Exception as e:
                        print(f"Error processing row: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import books: {e}")

    def export_orders_to_csv(self, filename):
        try:
            with open(filename, 'w', newline='') as file:
                fieldnames = ['customer_name', 'customer_email', 'book_title', 'price', 'total']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for order in self.orders:
                    order_details = order.get_order_details()
                    for item in order_details['items']:
                        writer.writerow({
                            'customer_name': order_details['customer_name'],
                            'customer_email': order_details['customer_email'],
                            'book_title': item['title'],
                            'price': item['price'],
                            'total': order_details['total']
                        })
            messagebox.showinfo("Success", "Orders exported successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export orders: {e}")

class BookstoreGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Bookstore System")
        self.bookstore = Bookstore()
        
        style = ttk.Style()
        style.theme_use('clam')
        
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        buttons = [
            ("Import Books", self.import_books),
            ("Export Orders", self.export_orders),
            ("View Catalog", self.view_catalog),
            ("Place Order", self.place_order),
            ("View Revenue", self.view_revenue)
        ]

        for text, command in buttons:
            btn = ttk.Button(main_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=3)

    def import_books(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            self.bookstore.import_books_from_csv(filename)
            messagebox.showinfo("Success", "Books imported successfully!")

    def export_orders(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")]
        )
        if filename:
            self.bookstore.export_orders_to_csv(filename)

    def view_catalog(self):
        catalog_window = tk.Toplevel(self.root)
        catalog_window.title("Book Catalog")
        
        tree = ttk.Treeview(catalog_window, columns=('Title', 'Author', 'Genre', 'Price', 'Type'), show='headings')
        tree.heading('Title', text='Title')
        tree.heading('Author', text='Author')
        tree.heading('Genre', text='Genre')
        tree.heading('Price', text='Price')
        tree.heading('Type', text='Type')
        
        for book in self.bookstore.books:
            book_type = "E-Book" if isinstance(book, EBook) else "Printed Book"
            tree.insert('', 'end', values=(
                book.title,
                book.author,
                book.genre,
                f"${book.price:.2f}",
                book_type
            ))
        
        scrollbar = ttk.Scrollbar(catalog_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def place_order(self):
        order_window = tk.Toplevel(self.root)
        order_window.title("Place Order")
        
        fields = [
            ("Customer Name:", tk.StringVar()),
            ("Customer Email:", tk.StringVar()),
            ("Payment Details:", tk.StringVar())
        ]
        
        for i, (label, var) in enumerate(fields):
            ttk.Label(order_window, text=label).grid(row=i, column=0, padx=5, pady=5, sticky='e')
            ttk.Entry(order_window, textvariable=var).grid(row=i, column=1, padx=5, pady=5, sticky='ew')
        
        book_listbox = tk.Listbox(order_window, selectmode=tk.MULTIPLE, height=6)
        book_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')
        
        for book in self.bookstore.books:
            book_listbox.insert(tk.END, f"{book.title} by {book.author} - ${book.calculate_price():.2f}")
        
        def process_order():
            if not all(var.get() for _, var in fields):
                messagebox.showerror("Error", "Please fill all customer details")
                return
            
            selected_books = [self.bookstore.books[i] for i in book_listbox.curselection()]
            if not selected_books:
                messagebox.showerror("Error", "Please select at least one book")
                return
            
            order = CustomerOrder(
                fields[0][1].get(),
                fields[1][1].get(),
                fields[2][1].get()
            )
            
            for book in selected_books:
                order.add_book(book)
            
            self.bookstore.process_order(order)
            messagebox.showinfo("Success", f"Order placed!\nTotal: ${order.calculate_total():.2f}")
            order_window.destroy()
        
        ttk.Button(order_window, text="Complete Order", command=process_order).grid(row=4, column=0, columnspan=2, pady=5)

    def view_revenue(self):
        revenue = self.bookstore.get_total_revenue()
        messagebox.showinfo("Total Revenue", f"Total Store Revenue: ${revenue:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreGUI(root)
    root.mainloop()