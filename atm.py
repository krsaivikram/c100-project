class Atm:
    def __init__(self,cardno,pin):
        self.cardno  = cardno
        self.pin = pin
    def checkbalance(self):
        print("your balance is 1000")
    def withdraw(self,amount):
        newamount = 1000-amount
        print("You have withdrawn"+str(amount)+"The balance is"+str(newamount))
def main():
     card_no = input("Insert your card number")
     pin_no = input("Insert pin number")
     newuser = Atm(card_no,pin_no)
     print("Choose your activity")
     print("1.Balance enquiry 2.Withdrawal")
     activity = int(input("Enter activity number"))
     if (activity == 1):
         newuser.checkbalance()
     elif (activity == 2):
        amount = int(input("Enter the amountyou wanna withdraw"))
        newuser.withdraw(amount)
     else:
        print("Enter a valid number") 
main()                
              

