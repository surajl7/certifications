class Car:
    def __init__(self):
        self.__speed = 'Initialized'

    def set_speed(self, x):
        self.__speed = x
    
    def get_speed(self):
        return self.__speed

obj = Car()
obj.set_speed(100)
print(obj.get_speed())