# class Animal():
#     def __init__(self, species_name, type):
#         self.species_name = species_name
#         self.type = type
#
#
# horse = Animal("horse", "mammal")
# alligator = Animal("alligator", "reptile")
#
# print(horse.species_name, horse.type)
# print(alligator.species_name, alligator.type)

class Bank:
    def __init__(self):
        self.customers = {}

    def add_account(self, account_no, balance = 0):
        if not account_no in self.customers:
            self.customers[account_no] = balance

    def deposit(self, account_no, deposit_value):
        if account_no in self.customers:
            self.customers[account_no] += deposit_value
            print(f"Deposited {deposit_value} successfully")
        else:
            print("There is no account with the number provided")

    def withdrawal(self, account_no, withdrawal_value):
        if account_no in self.customers:
            if withdrawal_value <= self.customers[account_no]:
                self.customers[account_no] -= withdrawal_value
            else:
                print("Not enough balance")
        else:
            print("There is no account with the number provided")

    def show_balance(self, account_no):
        if account_no in self.customers:
            print(f"Your balance is {self.customers[account_no]}")





al_ahly_bank = Bank()
al_ahly_bank.add_account("1")
print(al_ahly_bank.customers)
al_ahly_bank.deposit("1", 12000)
al_ahly_bank.show_balance("1")
al_ahly_bank.withdrawal("1", 2000)
al_ahly_bank.show_balance("1")

class Mb(Bank):

    def __init__(self, origin):
        super().__init__()
        self.origin = origin


mb = Mb("Mars")
print(mb.origin)
mb.add_account("2")
mb.deposit("2", 3422)

