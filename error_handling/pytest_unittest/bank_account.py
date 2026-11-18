class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
            if self.balance < amount:
                raise ValueError("insufficient funds")

            self.balance -= amount
            return (f"successful, your balance is {self.balance}")


def main():
    account1 = BankAccount()
    account1.deposit(50000)
    print(account1.withdraw(25000))
    print(account1.withdraw(30000))

if __name__ == "__main__":
    main()
