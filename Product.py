class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

# Provjerava stanje zaliha proizvoda i vraca False ako je kolicina manja od 10.
    def check_quantity(self):
        return self.quantity >= 10
