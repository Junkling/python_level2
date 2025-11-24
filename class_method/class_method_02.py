
# 클래스 구조
class CarDetail:
    """
    CarDetail class
    Author : Kim Jun Hyuk
    Date : 2025.11.24
    """
    _color:str
    _horsepower:int
    _price:int
    def __init__(self, color:str, horsepower:int, price:int):
        self._color = color
        self._horsepower = horsepower
        self._price = price

class Car:
    """
    Car class
    Author : Kim Jun Hyuk
    Date : 2025.11.24
    """
    # 클래스 변수
    car_count = 0

    _company :str
    _car_detail :CarDetail
    def __init__(self, company:str, car_detail:CarDetail):
        self._company = company
        self._car_detail = car_detail
        self.car_count = 100
        Car.car_count += 1

    def __str__(self):
        return f'str = \'company\' : {self.company} , {self.car_detail.__dict__}'

    def __repr__(self):
        return f'repr = \'company\' : {self.company} , {self.car_detail.__dict__}'

    def __reduce__(self):
        pass

    def __del__(self):
        Car.car_count -= 1
    def detail_info(self):
        print(f'car_id : {id(self)}')
        print(f'detail_id : {id(self._car_detail)}\ncar_detail_info : {self._car_detail.__dict__}')

print('car_count = ' , Car.car_count)

# Self의 의미
car_cl_1 = Car('Ferrari', CarDetail('White', 400, 8000))
car_cl_2 = Car('Bmw', CarDetail('Black' , 200 ,6000))
car_cl_3 = Car('Audi', CarDetail('Silver' , 300 ,5000))

print(id(car_cl_1))
print(id(car_cl_2))
print(id(car_cl_3))

print(car_cl_1._company == car_cl_2._company)

print(car_cl_1 is car_cl_2)

print(dir(car_cl_1))
print(dir(car_cl_2))

# 클래스 변수는 self.dict에서 안나옴
print(car_cl_1.__dict__)
# 클래스 dict에선 확인 가능
print(Car.__dict__)

print(Car.__doc__)


print(car_cl_1.__class__ , car_cl_2.__class__)
print(id(car_cl_1.__class__) , id(car_cl_2.__class__))
# print(id(car_cl_1.__class__) is id(car_cl_2.__class__))
print(car_cl_1.__class__ is car_cl_2.__class__)
print(id(car_cl_1.__class__) == id(car_cl_2.__class__))

# 에러 (self) 인자가 없다고 에러남
# Car.detail_info()
# 이건 됨
car_cl_1.detail_info()
Car.detail_info(car_cl_1)

# 클래스 변수는 클래스와 인스턴스 모두에서 접근 가능
# 인스턴스 변수를 먼저 찾고 없다면 클래스 변수에서 한번 더 찾는다.
print('car_count = ' , car_cl_1.car_count)
print('car_count = ' , Car.car_count)
car_cl_1.__del__()
car_cl_2.__del__()
print('car_count = ' , car_cl_1.car_count)
print('car_count = ' , Car.car_count)