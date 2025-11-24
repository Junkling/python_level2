# 메서드

# 클래스 구조
class CarDetail:
    """
    CarDetail class
    Author : Kim Jun Hyuk
    Date : 2025.11.24
    Description : Class, Static, Instance Method
    """
    _color:str
    _horsepower:int
    _price:int
    def __init__(self, color:str, horsepower:int, price:int):
        self._color = color
        self._horsepower = horsepower
        self._price = price

    @property
    def price(self):
        return self._price


class Car:
    """
    Car class
    Author : Kim Jun Hyuk
    Date : 2025.11.24
    """

    price_per_rise = 1.0

    _company :str
    _car_detail :CarDetail

    # self를 받는 메서드는 인스턴스 메서드
    def __init__(self, company:str, car_detail:CarDetail):
        self._company = company
        self._car_detail = car_detail

    def __str__(self):
        return f'str = \'company\' : {self.company} , {self.car_detail.__dict__}'

    def __repr__(self):
        return f'repr = \'company\' : {self.company} , {self.car_detail.__dict__}'

    def __reduce__(self):
        pass

    def detail_info(self):
        print(f'car_id : {id(self)}')
        print(f'detail_id : {id(self._car_detail)}\ncar_detail_info : {self._car_detail.__dict__}')

    def get_price(self)-> int:
        return self._car_detail._price

    def get_price_car(self):
        return self._car_detail._price * Car.price_per_rise

    # def change_price_rise(rise:float):
    #     Car.price_per_rise = rise

    # 클레스 메서드 (클레스 인스턴스에 접근할때 씀)
    @classmethod
    def change_price_rise(cls ,rise:float):
        print(f'price rate changed : {cls.price_per_rise} -> {rise}')
        cls.price_per_rise = rise

    # 스태틱 메서드 (빌더 페턴 등에서 쓸 듯)
    @staticmethod
    def is_bmw(inst):
        return inst._company == 'Bmw'

# Self의 의미
car_cl_1 = Car('Ferrari', CarDetail('White', 400, 8000))
car_cl_2 = Car('Bmw', CarDetail('Black' , 200 ,6000))
car_cl_3 = Car('Audi', CarDetail('Silver' , 300 ,5000))

print(car_cl_1.get_price_car())
print(car_cl_3.get_price_car())

# Car.price_per_rise = 1.05
Car.change_price_rise(1.05)

print(car_cl_1.get_price_car())
print(car_cl_3.get_price_car())

Car.change_price_rise(1.11)

print(car_cl_1.get_price_car())
print(car_cl_3.get_price_car())

print(car_cl_2.is_bmw(car_cl_2))
print(car_cl_1.is_bmw(car_cl_1))

print(Car.is_bmw(car_cl_2))
print(Car.is_bmw(car_cl_1))