# The car service station caters to different types of cars – Hatchback, Sedan, SUV.
# It provides different types of services like Basic Service, Engine Fixing, Clutch Fixing, Gear Fixing and Brake Fixing.
# Each service has a service code associated with it and different prices for different types of cars.

class Car:
    def __init__(self, type_):
        self.type = type_

class Service:
    def __init__(self, code, price):
        self.code = code
        self.price = price

class CarServiceStation:
    def __init__(self):
        self.services = {
            "BS01": Service("BS01", 2000),
            "EF01": Service("EF01", 5000),
            "CF01": Service("CF01", 4500),
            "BF01": Service("BF01", 3000),
            "GF01": Service("GF01", 4000)
        }
        self.discount_threshold = 10000
        self.discount_price = 1000

    def generate_bill(self, car, service_codes):
        total_bill = 0
        for code in service_codes:
            service = self.services[code]
            if car.type == "Hatchback":
                total_bill += service.price
            elif car.type == "Sedan":
                total_bill += service.price * 1.2
            elif car.type == "SUV":
                total_bill += service.price * 1.5
        if total_bill > self.discount_threshold:
            total_bill -= self.discount_price
            print("Complimentary cleaning service applied!")
        return total_bill

station = CarServiceStation()
car = Car("Hatchback")
service_codes = ["BS01", "EF01"]
bill = station.generate_bill(car, service_codes)
print(f"Type of Car: {car.type}")
print(f"Service codes: {service_codes}")
print(f"Total bill: {bill}")
