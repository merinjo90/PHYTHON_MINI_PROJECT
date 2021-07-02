
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