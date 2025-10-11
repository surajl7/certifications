class Car:
    def __init__(self, x):
        self.speed = x
        self.price_per_speed = 3

    def price(self):
        self.__carPrice = self.speed * self.price_per_speed
        return self
    
obj = Car(100)
print(obj.price().__carPrice)  # Atrribute Error

# print(obj.price()._Car__carPrice)

