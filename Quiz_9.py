class Beverage:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def calculate(self,quantity):
        total_price=self.price*int(quantity)
        print(self.name + str(quantity) + '잔의 총 가격은' + str(total_price) + '원 입니다.')

Coffee = Beverage('커피', 3000)
GreenTee = Beverage('녹차',2500)
IceTea = Beverage('아이스티', 3000)

selected_beverage=input('음료를 입력하세요 : 커피 3000원 녹차 2500원 아이스티 3000원')
quantity=input('수량을 입력하세요')

if selected_beverage == '커피':
    Coffee.calculate(quantity)
elif selected_beverage == '녹차':
    GreenTee.calculate(quantity)
elif selected_beverage == '아이스티':
    IceTea.calculate(quantity)
else:
    print('잘못된 음료입니다.')

