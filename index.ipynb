class Product:
    def __init__(self, name, category, status, stock_date):
        self.name = name
        self.category = category
        self.status = status
        self.stock_date = stock_date

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Category: {self.category} | Status: {self.status} | Stock Date: {self.stock_date}"


class StationeryManager:
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def add_product(self, name, category, status, stock_date):
        product = Product(name, category, status, stock_date)
        product.id = self.next_id
        self.products[self.next_id] = product
        self.next_id += 1
        return f"Product {product.id} added successfully!"

    def show_all_products(self):
        if not self.products:
            return "No products available."
        return "\n".join(str(product) for product in self.products.values())

    def show_product(self, product_id):
        product = self.products.get(product_id)
        if product:
            return str(product)
        return f"Product with ID {product_id} not found."

    def update_product(self, product_id, name=None, category=None, status=None, stock_date=None):
        product = self.products.get(product_id)
        if product:
            if name:
                product.name = name
            if category:
                product.category = category
            if status:
                product.status = status
            if stock_date:
                product.stock_date = stock_date
            return f"Product {product_id} updated successfully!"
        return f"Product with ID {product_id} not found."

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            return f"Product {product_id} deleted successfully!"
        return f"Product with ID {product_id} not found."


# ------------------ MENU ------------------ #

manager = StationeryManager()

while True:
    print("\n===== Stationery Shop Menu =====")
    print("1. Add Product")
    print("2. Show All Products")
    print("3. Show Product by ID")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # 1. Add product
    if choice == "1":
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        status = input("Enter status (Available / Out of Stock): ")
        stock_date = input("Enter stock date (DD-MM-YYYY): ")
        print(manager.add_product(name, category, status, stock_date))

    # 2. Show all
    elif choice == "2":
        print(manager.show_all_products())

    # 3. Show by ID
    elif choice == "3":
        pid = int(input("Enter product ID: "))
        print(manager.show_product(pid))

    # 4. Update product
    elif choice == "4":
        pid = int(input("Enter product ID to update: "))
        print("\nEnter new values (press Enter to skip):")
        name = input("New name: ") or None
        category = input("New category: ") or None
        status = input("New status: ") or None
        stock_date = input("New stock date: ") or None
        print(manager.update_product(pid, name, category, status, stock_date))

    # 5. Delete product
    elif choice == "5":
        pid = int(input("Enter product ID to delete: "))
        print(manager.delete_product(pid))

    # 6. Exit
    elif choice == "6":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
