# 클래스 메서드 심화
# 객체 지향 프로그래밍

# 객체 X 코딩 예시

# 차 1
car_com_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]
# 차 2
car_com_2 = 'Bmw'
car_detail_2 = [
    {'color': 'black'},
    {'horsepower': 300},
    {'price': 5000}
]
# 차 3
car_com_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': 400},
    {'price': 6000}
]

# 리스트 구조 -> 관리가 어려움 -> 인덱스 접근시 내부 값에 대한 검증 처리가 힘듬 + 삭제에 불리함
car_com_list = ['Ferrari', 'Bmw', 'Audi']

car_detail_list = [
    {'color': 'White',
     'horsepower': 400,
     'price': 8000},

    {'color': 'black',
     'horsepower': 300,
     'price': 5000},

    {'color': 'Silver',
     'horsepower': 400,
     'price': 6000}
]

del car_com_list[1]
del car_detail_list[1]

print(car_com_list)
print(car_detail_list)

print()
print()

# dict 형태로 구성 시
car_1 = {'company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}}
car_2 = {'company': 'Bmw', 'car_detail': {'color': 'Black', 'horsepower': 200, 'price': 6000}}
car_3 = {'company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower': 300, 'price': 5000}}
print(list(d.get('company') for d in [car_1, car_2, car_3]))
print(list(d.get('car_detail') for d in [car_1, car_2, car_3]))
print()

# 클래스 구조
class CarDetail:
    color:str
    horsepower:int
    price:int
    def __init__(self, color:str, horsepower:int, price:int):
        self.color = color
        self.horsepower = horsepower
        self.price = price

class Car:
    company :str
    car_detail :CarDetail
    def __init__(self, company:str, car_detail:CarDetail):
        self.company = company
        self.car_detail = car_detail

    def __str__(self):
        return f'str = \'company\' : {self.company} , {self.car_detail.__dict__}'

    def __repr__(self):
        return f'repr = \'company\' : {self.company} , {self.car_detail.__dict__}'

    def __reduce__(self):
        pass


car_cl_1 = Car('Ferrari', CarDetail('White', 400, 8000))
car_cl_2 = Car('Bmw', CarDetail('Black' , 200 ,6000))
car_cl_3 = Car('Audi', CarDetail('Silver' , 300 ,5000))
print(car_cl_1)
print(car_cl_2)
print(car_cl_3)
# str 구현이 없고 repr만 구현되어 있으면 str대신 repr 가 반환됨
print(repr(car_cl_1))
print(repr(car_cl_2))
print(repr(car_cl_3))



print()
