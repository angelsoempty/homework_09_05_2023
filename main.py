class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}")

car = Car('Mercedes', 'W223','2020')
car.info()