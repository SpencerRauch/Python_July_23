#for loops

# for i in range(10):
#     print(i)

desserts = ['tiramisu', 'chocolate ice cream', 'flan','ice cream cake','ice cream sandwiches']

person = {
    'name':'Spencer',
    'age': 35,
    'occupation': "Instructor"
}

# for iv in desserts:
#     print(iv)

# print(desserts)
print(f"Spencer's age is {person['age']}")
for key in person:
    print(f"{key} is {person[key]}")


pet_one = {
    'name': 'Teddy',
    'type': 'dog'
}

pet_two = {
    'name': 'Jax',
    'type': 'fish',
    'list': [1,2,3,56,7]
}

pets_list = [pet_one,pet_two]
#              0         1

print(pets_list[1]['list'][3])

class Topping:
    def __init__(self, name, savory, sweet, is_meat):
        self.name = name
        self.savory = savory
        self.sweet = sweet
        self.is_meat = is_meat
    
    def __repr__(self):
        return f"{self.name} Savory: {self.savory} Sweet {self.sweet} Meat? {self.is_meat}"

olives = Topping("olives",True,False,False)
mushroom = Topping("mushrooms",True,False,False)
bacon = Topping("bacon",True,False,True)
pineapple = Topping("pineapple",False,True,False)
cheese = Topping("cheese",True,False,False)


class Pizza:
    def __init__(self, crust, size) -> None:
        self.crust = crust
        self.size = size
        self.ingredients = []
        # self.special_ingredient = None

    def add_topping(self, new_topping):
        self.ingredients.append(new_topping)
        return self

    def __repr__(self):
        msg = f"{self.size} inch {self.crust} pizza with these ingredients : \n"
        for ingredient in self.ingredients:
            msg += f" - {ingredient}\n"
        return msg
    
pizza_one = Pizza("thin",10)
pizza_one.add_topping(olives).add_topping(mushroom).add_topping(bacon).add_topping(cheese)
# pizza_one.ordered_by = "Spencer"
pizza_one.special_ingredient = pineapple
print(pizza_one)
print(pizza_one.special_ingredient)