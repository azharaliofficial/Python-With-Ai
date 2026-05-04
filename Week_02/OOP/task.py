class Account:
    def __init__(self , balance):
        self.__balance = balance
    def deposit(self , amount):
        self.__balance+=amount
        print(f"Deposit Amount: {amount}\nCurrent Balance:{self.__balance}")
    def withdraw(self):
        return self.__balance
    def get(self):
        return self.__balance

class SavingsAcc(Account):
    def withdraw(self):
        check_balance = self.get()
        if check_balance<500:
            print(f"You cann't withdraw this amount : {check_balance}") 
        else:
            print("Successfully Withdraw")              

user1 = SavingsAcc(int(input("Enter your current balance: ")))
user1.deposit(int(input("Enter your deposit amount: ")))
user1.withdraw()



            