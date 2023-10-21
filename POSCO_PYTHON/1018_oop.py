# 객체 지향 프로그래밍
# 특수 메서드 : 가장 대표적인 특수 메서드 "__init__"

class Sample:
    def __init__(self):
        
        return None
    
a = Sample() #자동으로 init 메서드 호출 

class Building:
    #생성자(Constructer)
    def __init__(self, name = "공학1동", h=3, elev = True):
        #값을 업데이트 하고 싶을 때 self를 적어줌
        self.name = name
        self.h = h
        self.elev = elev
        
    def get_info(self):
        print("건물이름=", self.name)
        print("건물층수=", self.h)
        print("엘레베이터 유무=", self.elev)

a = Building()
b = Building("공학2동", 10, True)

a.get_info()
print()
b.get_info()

#건물이름= 공학1동
#건물층수= 3
#엘레베이터 유무= True

#건물이름= 공학2동
#건물층수= 10
#엘레베이터 유무= True

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def get_info(self):
        print("이름: ", self.name)
        print("나이: ",self.age)
        print("키: ",self.height)
        print("몸무게: ", self.weight)
        print()

    def get_age(self):
        self.age += 1
        
    def delta_height(self, new_h):
        self.height = new_h
    
    def delta_weight(self, new_w):
        self.weight = new_w

person1 = Person("홍길동", 25, 180, 70)
person2 = Person("홍길순", 23, 165, 50)

person1.get_info()

#이름:  홍길동
#나이:  25
#키:  180
#몸무게:  70

person1.get_age()
person1.delta_height(188)
person1.delta_weight(75)

person1.get_info()
person2.get_info()

#이름:  홍길동
#나이:  26
#키:  188
#몸무게:  75

#이름:  홍길순
#나이:  23
#키:  165
#몸무게:  50

class BankAccount:
    def __init__(self, balance=0, name="none"):
        self.balance = balance
        self.name = name
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance < amount: #출금 금액이 더 큰 경우
            print("잔액 부족")
            return False
        else:
            self.balance -= amount
            return True
        
    def get_info(self):
        print("이름:", self.name)
        print("잔액:", self.balance)
    
    def transfer(self, other, amount):
        if self.withdraw(amount):
            other.deposit(amount)
        
acc1 = BankAccount(1000, "고길동")
acc2 = BankAccount(200, "고영희")

acc1.transfer(acc2, 300)
acc1.get_info()
acc2.get_info()

#이름: 고길동
#잔액: 700
#이름: 고영희
#잔액: 500

acc1 = BankAccount(1000, "고길동")
acc2 = BankAccount(0, "고희동")

acc1.transfer(acc2, 2000)
acc1.get_info()
acc2.get_info()

#잔액 부족
#이름: 고길동
#잔액: 1000
#이름: 고희동
#잔액: 0

a = BankAccount(100, "kkm")

a.deposit(400)
a.withdraw(600)

#잔액 부족

b = BankAccount()
b.deposit(1000)
b.withdraw(900)
b.get_info()

#이름: none
#잔액: 100

#상속
class MinimumBalanceAccount(BankAccount):
    
    def __init__(self, balance=0, name='none', min_bal=0):
       # self.balance = balance
       # self.name = name
        super().__init__(balance, name)
        self.min_bal = min_bal
        
    def withdraw(self, amount):
        if self.balance - amount < self.min_bal:
            print("최소 잔액을 유지해야 합니다.")
        
        else:
            super().withdraw(amount)

acc = MinimumBalanceAccount(500, "kim", 1000)
acc.deposit(1000)
acc.withdraw(600)

#최소 잔액을 유지해야 합니다.

acc1 = MinimumBalanceAccount(1000, "kim", 500)
acc1.withdraw(100)
acc1.get_info() #상속받은 BankAccount에 있는 메서드(부모 클래스)

#이름: kim
#잔액: 900