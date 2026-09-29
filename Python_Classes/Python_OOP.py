class Atm:
    count = 0

    def __init__(self, count):
        self.__pin = ""
        self.__balance = 0
        self.__count = count

    def get_pin(self):
        return self.__pin

    def set_pin(self, new):
        if isinstance(new, str) and new.isdigit() and len(new) == 4:
            self.__pin = new
            return True
        print("Invalid PIN. Use a 4-digit numeric PIN.")
        return False

    def check_balance(self):
        return self.__balance
    def get_count(self):
        return self.__count
    def set_count(self, new_count):
        if type(new_count) == int:
            Atm.__count = new_count
        else:
            print("Not allowed")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        print("Deposit amount must be greater than zero.")
        return False

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False
        if amount > self.__balance:
            print("Insufficient balance.")
            return False
        self.__balance -= amount
        return True

    def menu(self):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Your balance is: {self.__balance}")
            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: "))
                    if self.deposit(amount):
                        print("Deposit successful.")
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    if self.withdraw(amount):
                        print("Withdrawal successful.")
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "4":
                new_pin = input("Enter your new 4-digit PIN: ")
                if self.set_pin(new_pin):
                    print("PIN changed successfully.")
            elif choice == "5":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    atm = Atm()

    while True:
        pin = input("Set your 4-digit PIN: ")
        if atm.set_pin(pin):
            break

    atm.menu()
