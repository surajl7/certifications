class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)  # Correct method call

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
        
    __update = update  # Alias for the update method

class MappingSubclass(Mapping):
    def update(self, keys, values):
        print(keys)
    
    def print_something(self):
        print("Printing something")

    __update = print_something  # This method is separate due to name mangling

# Creating an instance of MappingSubclass
MappingSubclass([1, 2, 3])
