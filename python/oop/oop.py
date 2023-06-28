#OOP

#Classes and Instances / Objects

#What is a class? blueprint  -- it defines the methods and attributes we can expect from our Objects (Instances)
# classes create a custom data type

#object/instance -- the actual thing we create with a blueprint (class)

#class methods 
"""
no access to any instance variables
operate on the class level only
no reference to self
call it from the class itself
can access class attributes
"""

#static methods
"""
unchanging -- doesn't mutate anything in the class
utility function that relates to class
often used to validate data coming into our class
"""

dog_data_1 = {
    'name': 'Fido',
    'age': 2,
    'color': 'brown'
}

dog_data_2 = {
    'name': 'Spot',
    'age': 4,
    'color': 'white with a brown spot'
}

#self is a reference to the current instance of this class

# class Dog: #notice the capital letter! 
#     def __init__(self,name,age,param_color):
#         self.name = name
#         self.age = age
#         self.color = param_color

# dog_1 = Dog("Fido",2,"brown")
# dog_2 = Dog("Spot",4,"white with a spot")
# dog_1.name = "Bob"
# # dog_1.name = "Fido" we can add attributes to an instance/object any time we want

class Dog: #notice the capital letter! 
    is_cute = True
    all_dogs = []
    def __init__(self,data_dict, human=None):
        self.name = data_dict['name'] #attributes
        self.age =  data_dict['age']
        self.color =  data_dict['color']
        self.roommate = human
        Dog.all_dogs.append(self)
    
    #method - just a function that belongs to a class
    #instance methods have access to one object, the one they are called from
    def bark(self):
        print(f"{self.name} lets out a bark!")
        return self

    def have_birthday(self):
        self.age += 1
        print(f"{self.name} is older and wiser! They are now {self.age} years old")
        return self

    @classmethod
    def bark_party(cls):
        print(f"The bark party has started! There are {len(cls.all_dogs)} dogs barking")
        for ea_dog in cls.all_dogs:
            ea_dog.bark()

    def __repr__(self): #string representation of our object
        return f"Dog Object. Name {self.name} Age {self.age} Color {self.color}"
    
    @staticmethod
    def calculate_dog_years(years):
        return years * 7

class Human:
    def __init__(self,name) -> None:
        self.name = name
    
    def say_hello(self):
        print(f"{self.name} says hello")

    def __repr__(self) -> str:
        return self.name


spencer = Human("Spencer")
dog_1 = Dog(dog_data_1, spencer)
dog_2 = Dog(dog_data_2)
print(dog_1)
print(dog_2)

# dog_1.bark()
# dog_2.bark()
# dog_1.have_birthday()
# dog_2.have_birthday()
# print(Dog.is_cute)

dog_1.bark().bark().have_birthday().bark()
# print(Dog.all_dogs)
Dog.bark_party()

dog_1.roommate = spencer

print(dog_1.roommate)
dog_1.roommate.say_hello()
# print(Dog.calculate_dog_years(3))
if not dog_2.roommate == None:
    dog_2.roommate.say_hello()
else:
    print("This dog has no roommate")
