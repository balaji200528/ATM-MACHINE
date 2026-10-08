class ATM:

    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()
    
    def check(self,pin):
        try:
            if self.pin=="":
                raise ValueError("create a pin")
            
            if pin!=self.pin:
                raise ValueError("wrong pin")
        
        except ValueError as e :
            print("error",e)
            self.menu()
         
    def menu(self):

        try:
            user_input = input(
                """
                Hello, how would you like to proceed?

                1. Enter 1 to create PIN
                2. Enter 2 to deposit
                3. Enter 3 to withdraw
                4. Enter 4 to check balance
                5. Enter 5 to exit

                Enter your choice: 
                """
            )

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.deposit()

            elif user_input == "3":
                self.withdraw()

            elif user_input == "4":
                self.check_balance()

            elif user_input == "5":
                self.exit()

            else:
                raise ValueError("Invalid menu choice1")

        except ValueError as e:
            print("Error:", e)
            self.menu()


    def create_pin(self):

        try:
            if self.pin=="":
                pin = int(input("Enter the PIN: "))

                if len(str(pin)) != 4:
                    raise ValueError("PIN must contain exactly 4 digits")

                self.pin = pin

                print("PIN created successfully")
            else:
                print("pin already exits")

        except ValueError as e:
            print("Error:", e)

        self.menu()


    def deposit(self):
        pin = int(input("Enter the PIN: "))
        self.check(pin)
        try:
            amount = int(input("Enter the amount: "))

            if amount <= 0:
                raise ValueError("Deposit amount must be greater than 0")

            self.balance += amount

            print("The amount has been deposited successfully")

        except ValueError as e:
            print("Error:", e)

        self.menu()


    def withdraw(self):
        pin = int(input("Enter the PIN: "))
        self.check(pin)
        try:
            amount = int(input("Enter the amount to withdraw: "))

            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than 0")

            if amount > self.balance:
                raise ValueError("Insufficient balance")

            self.balance -= amount

            print(f"{amount} has been withdrawn successfully")

        except ValueError as e:
            print("Error:", e)

        self.menu()


    def check_balance(self):

        try:

            if self.pin == "":
                raise ValueError("Please create a PIN first")

            pin = int(input("Enter the PIN: "))

            if pin != self.pin:
                raise ValueError("Incorrect PIN")

            print(f"Your balance is: ₹{self.balance}")

        except ValueError as e:
            print("Error:", e)

        self.menu()


    def exit(self):
        print("Bye Bye")


p1 = ATM()