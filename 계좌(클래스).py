class Transfer:
    def __init__(self, name, account):
        self.name = name
        self.account = account 
        self.balance = 10000
    
    def get_deposit(self, deposit):
        self.balance = self.balance + deposit
        return f'계좌번호: {self.account} / 입금액: {deposit} / 잔액: {self.balance} / {self.name} 고객님 감사합니다.'
    
    def get_withdrawal(self, withdrawal):
        if withdrawal > self.balance:
            return f'{self.name} 고객님 잔액이 부족합니다. 남은 잔액: {self.balance}원'
        else:
            self.balance = self.balance - withdrawal
            return f'계좌번호: {self.account} / 출금액: {withdrawal} / 잔액: {self.balance} / {self.name} 고객님 감사합니다.'

    def __str__(self):
        return f'고객명: {self.name} 계좌명: {self.account} 보유 금액 : {self.balance}'

class Check(Transfer):
    def __init__(self, name, account):
        Transfer.__init__(self, name, account)
    def get_name_cha(self):
        return f'고객명은 {len(self.name)}글자 입니다.'
    def get_balance(self):
        return f'남은 금액: {self.balance}' 


jisun = Check('최지선','110-11')
print(jisun)
print(jisun.get_name_cha())
print(jisun.get_deposit(1000))
print(jisun.get_withdrawal(2000))
print(jisun.get_withdrawal(12000))
print(jisun.get_balance())

