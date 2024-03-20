import random
class AtmAcct:
    def __init__(self, id, bal2 = 0, annualIntRate = 2.5):
        self.id = id
        self.bal2 = bal2
        self.annualIntRate = annualIntRate
    def getId(self):
        return self.id
    def deposit(self,amt):
        self.bal2 += amt
    def withdraw(self,amt):
        self.bal2 -= amt
    def getbal2(self):
        return self.bal2
    def getannualIntRate(self):
        return self.annualIntRate
    def getMonthlyInt(self):
        return self.bal2 * self.getMonthlyInt()
    
def main():
    accounts = []
    for i in range(1000,9999):
        account = AtmAcct(i,0)
        accounts.append(account)
    while True:
        id  = int(input("\nEnter Account Pin:"))

        while id < 1000 or id > 9999:
            id = int(input("\nInvalid Pin Re-enter:"))

        while True:
            print("\n[1] View balance \t [2] Withdraw \t [3] Deposit \t [4] Exit")

            option = int(input("\nEnter your option: "))

            for acc in accounts:
                if acc.getId() == id:
                    AtmAcctObj = acc
                    break
            if option == 1:
                print(AtmAcctObj.getbal2())
            elif option == 2:
                amt = float(input("\nEnter amount to Withdraw:"))
                WithAns = input("Is the entry Correct Yes or No ?"+str(amt)+" ")
                if WithAns == "Yes":
                    print("Verified Withdraw")
                else:
                    break
                if amt < AtmAcctObj.getbal2():
                    AtmAcctObj.withdraw(amt)
                    print("\nUpdated balance:" + str(AtmAcctObj.getbal2()) +"\n")
                else:
                    print("\nYou have insufficient balance:"+str(AtmAcctObj.getbal2())+"\1233n")
            elif option == 3:
                amt = float(input("\nEnter amount to deposit:"))
                depoAns = input("Is the entry Correct, Yes, or No ?"+str(amt)+" ")
                if depoAns == "Yes":
                    AtmAcctObj.deposit(amt)
                    print("\nUpdated balance:"+str(AtmAcctObj.getbal2())+"n")
                else:
                    break
            elif option == 4:
                print("Transaction successfull.")
                print("Transaction no :",random.randint(10000, 1000000))
                print("Current Interest Rate:",AtmAcctObj.annualIntRate)
                print("Monthly Interest Rate:",AtmAcctObj.annualIntRate / 12)
                exit()
            else:
                print("Invalid option.")
main()









