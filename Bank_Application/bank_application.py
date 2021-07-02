
"""
#create a bank application.
#          : "Account"-parent class, with a "BankName: ABC bank,IFSCcode : 45154,Balance" as
#          class variables. inital balace "10000"common to all customer.
#         :"AccountHolder"-child class, with instance variables "name,AccNo" and functions
#         "Deposit,widrow,Balacecheck" .
#         : if the user use any of these method by passing an amount, we want to get full
#         bank details and  current balance .
#         : for balance checking dont want to pass any amount.
#         : provided min balance required is limited to 1000.
"""

class Account:       #parent class
    Balance=10000    #class variables
    BankName="ABC"
    IFSCcode=45154
    min_balance=1000

class AccountHolder:  # child class
    def __init__(self, name, accNo):
        self.Name = name  # instance variable
        self.AccNo = accNo


    def personal_details(self): #instance functions
        print("BANK DETAILS\n")
        print("Bank Name: ", Account.BankName)
        print("IFSCcode : ", Account.IFSCcode)
        print("")
        print("CUSTOMER DETAILS")
        print("")
        print("Name: ", self.Name)
        print("Account Number",self.AccNo)
        print("")

    def Deposit(self):
        self.personal_details()
        # Account.bank_details()
        amount = float(input("Enter the amount to be deposite:"))
        Account.Balance = Account.Balance + amount
        print("Deposite is succesful and the balance in the account is %f" % Account.Balance)
        print("------------------")

account=Account()
account_holder=AccountHolder("amala",123)
account_holder.Deposit()
