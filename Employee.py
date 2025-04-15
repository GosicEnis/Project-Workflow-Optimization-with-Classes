class Employee:
    def __init__(self, name, email, salary, address):
        self.name = name
        self.email = email
        self.salary = salary
        self.address = address

# Metoda za provjeru da li je email ispravan.
    def check_email(self):
        return "@" in self.email

# Metoda povecanja plate za odredjeni procenat
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)
