from User import User
from Product import Product
from Employee import Employee

# Lista proizvoda
products = [
    Product("Laptop", 2500, 10, "MacBook Air 15-inc."),
    Product("Monitor", 400, 2, "AOC Gaming monitor 27-inc."),
    Product("Mobitel", 2300, 15, "IPhone 16 PRO."),
    Product("Mis", 60, 20, "Wireless mis"),
    Product("TV", 1500, 3, "TV Samsung 4k 65-inc.")
]

# Lista zaposlenih
employees = [
    Employee("Damir", "damir@gmail.com", 1600, "Sarajevo"),
    Employee("Samra", "samra@gmail.com", 1450, "Tuzla")
]

# Kreiramo listu sa korisnicima
users = [
    User("Ismar", "ismar21@gmail.com", "38762345656", "Sarajevo"),
    User("Selma", "selma33@gmail.com", "38761233433", "Sarajevo"),
    User("Ana", "ana23@gmail.com", "38760113131", "Mostar")
]

users[0].add_product(products[0])
users[0].add_product(products[3])
users[2].add_product(products[2])
users[1].add_product(products[4])

# Demonstriramo funkcionalnosti
print("\n Validni email-ovi:")
for user in users:
    print(f"{user.name} validan email? = {user.check_email()}")

for employee in employees:
    print(f"{employee.name} validan email? = {employee.check_email()}")

print("\n Stanje proizvoda:")
for product in products:
    print(f"{product.name} na stanju: {product.check_quantity()}")

print("\n Nove plate zaposlenih:")
for employee in employees:
    employee.increase_salary(10)
    print(f"{employee.name} nova plata: {employee.salary}")

print("\n Aktivnosti korisnika:")
for user in users:
    print(f"{user.name} je potrosio/la {user.total_spent()} ukupno.")
