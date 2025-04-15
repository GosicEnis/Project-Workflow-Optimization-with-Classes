class User:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.shopping_history = []

# Provjeravamo da li email sadrzi "@".
    def check_email(self):
        return "@" in self.email

# Izracunavamo ukupnu potrosenu sumu.
    def total_spent(self):
        return sum(item.price * item.quantity for item in self.shopping_history)

# Dodaje proizvod u listu kupljenih proizvoda.
    def add_product(self, product):
        self.shopping_history.append(product)
