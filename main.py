class Bank:
    def __init__(self):
        self.customers = []
    def add_customer(self, customer):
        self.customers.append(customer)
    def get_total_balance(self):
        total_balance = 0
        for customer in self.customers:
            total_balance += customer.get_balance()
        return total_balance

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

bank = Bank()

customer1 = BankAccount(1000)
customer2 = BankAccount(2000)
customer3 = BankAccount(3000)

bank.add_customer(customer1)
bank.add_customer(customer2)
bank.add_customer(customer3)

total_balance = bank.get_total_balance()
print(total_balance)
