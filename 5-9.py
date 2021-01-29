class bank:
    def __init__(self):
        self.__balance = 0
        
    def withdraw(self, amount):
        self.__balance -=amount
        print("통장에",amount,"가 출금되었습니다.",self.__balance)
        return self.__balance
    
    def deposit(self,amount):
        self.__balance +=amount
        print("통장에",amount,"가 입금되었습니다.",self.__balance)
        return self.__balance
    
a = bank()
a.deposit(100)
a.withdraw(10)

b= bank()
b.deposit(50)
a.withdraw(30)