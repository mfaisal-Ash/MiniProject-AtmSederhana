from atm_card import ATMCard

class customer:
    def init(self, id, custPin=1234, custBalance=10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance
    
    def checkId(self):
        return self.id
    def checkPin(self):
        return self.pin
    def checkBalance(self):
        return self.balance
   
    def withdramBalance(self, nominal):
        self.balance -= nominal
    def depositBalance(self, nominal):
        self.balance += nominal

    