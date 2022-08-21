class Account(object):

    '''Account class with total_balance variable and methods for checking balance, withdraw money and deposit money are defined'''
    def __init__(self): 
        self.total_balance=0
    
    def deposit(self,deposit_money):
        self.total_balance+=int(deposit_money)

    def balance(self):
        print("total balance in your account is",self.total_balance)

    def withdraw(self,withdrw_money):
        if int(withdrw_money)>self.total_balance:
            print("Sorry not enough funds available in account.")
            return self.total_balance
        else:
            self.total_balance-=int(withdrw_money)

    #method to check card and pin, which is set to 1234 by default.  
    def checkCardandpin(self):
        card=input("did you enter card? Y/N ") #a way to check if card is there or not.
        if card=='yes' or card=='y' or card=='Y':
            pin=input("Please input the pin: ")
            if pin=='1234':
                return True
            else:
                return False

def main(self):
        print("Please insert a Card")
        if self.checkCardandpin():
            while True:
                print("Welcome to Bear Robotics Bank!")
                print("Please select from following options:")
                print("1.Depost")
                print("2.Withdrawal")
                print("3.Check balance")
                choose=input("Please enter your options from 1,2 or 3: ")
                if int(choose) == 1:
                    deposit_money=input("Enter amount you want to deposti: ")
                    self.deposit(deposit_money)
                elif int(choose) == 2:
                    withdrw_money=input("Enter amount you want to withdraw: ")
                    self.withdraw(withdrw_money)
                elif int(choose)== 3:
                    self.balance()
                else:
                    print("invalid option")
                ask=input("Do you want to continue? ")
                if ask=='yes' or ask=='y' or ask=='Y':
                    continue
                else:
                    break
    
      
if __name__=='__main__':
    a=Account()
    main(a) 
