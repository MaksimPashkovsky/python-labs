class BankAccount:

    def __init__(self, acc_num: int, name: str, balance: float):
        self.account_number = acc_num
        self.name = name
        self.__balance = round(balance, 2)

    def deposit(self, amount: float):
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount: float):
        if amount > self.__balance:
            print("Not enough money on balance!")
            return
        self.__balance = round(self.__balance - amount, 2)

    def apply_fees(self):
        self.__balance = round(self.__balance * 1.05, 2)

    def display(self):
        print(f"Account number: {self.account_number};\n"
              f"Owner name: {self.name};\n"
              f"Balance: {self.__balance}\n")


if __name__ == "__main__":
    account = BankAccount(332, 'Feofan', 1200.0)
    account.display()
    account.deposit(80.12)
    account.display()
    account.withdraw(500)
    account.display()
    account.apply_fees()
    account.display()
