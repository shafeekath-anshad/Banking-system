class Customers:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def cus_detail(self):
        print("Customer Details")
        print("---------------------")
        print("name:", self.name, "\nplace:", self.place)


class Accounts:
    def __init__(self, acc_no, deposite, withdraw, transfer_fund):
        self.acc_no = acc_no
        self.deposite = deposite
        self.withdraw = withdraw
        self.transfer = transfer_fund

    def acc_detail(self):
        print("Account Details")
        print("----------------")
        print("acc_no", self.acc_no, "\n DEposite:", self.deposite, "\n Withdrawn:", self.withdraw,
              "\nFund transferred", self.transfer)


class Transactions(Accounts, Customers):
    def view_account_details(self):
        print("Welcome to the bank")
        print("\n View The Details")
        print("==================================\n")


acc_obj = Accounts("SBI2564855", 50000, 5000, 10000)
cus_obj = Customers("anu", "Banglore")
Tran_obj = Transactions
Tran_obj.view_account_details(self=Transactions)
cus_obj.cus_detail()
acc_obj.acc_detail()
