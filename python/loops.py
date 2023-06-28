#Loops -- code that repeats a set amount of times based on a condition

# for (let i = 0; i<29;i++){
#    console.log("hello")
#}

"""
for ___ in ___ :
    code to execute
"""

#first blank -- iterative variable, will represent one item from the collection

#second blank -- the collection we are iterating over

#range(start,stop,step) --
#start -- optional, default 0 -- this number we will start our sequence at INCLUSIVE
#stop -- required EXCLUSIVE -- the number we will end BEFORE
#step -- optional increment/decrement, defaults to 1
# for i in range(100,10):
#     print(i)

# for x in range(100,50,-5):
#     print(x)

# for y in range(10):
#     print(y)

string = "What will be our iterative variable for this?"
#when iterating over a string, our iterative variable will represent each character in turn
# for char in string:
#     print(char)

desserts = ['cake','pie','cookies','ice cream']
#when iterating over a list, our iterative variable will represent each element of the list
for one_dessert in desserts:
    one_dessert = "Pineapple" #why doesn't this work??? 
    # print(one_dessert) 

#getting indices from a list
for i in range(len(desserts)):
    desserts[i] = "Pineapple"
# print(desserts)

pet_one = {
    'name': 'Teddy',
    'type': 'dog'
}

pet_two = {
    'name': 'Jax',
    'type': 'fish'
}

#when iterating over a dictionary, the iterative variable is the keys
for key in pet_one:
    print(f"{key}: {pet_one[key]}")

all_pets = [pet_one,pet_two]

print(all_pets[1]['name'])

for one_pet in all_pets:
    for key in one_pet:
        print(f"{key}: {one_pet[key]}")


#while
x = 5
while x > 0:
    print(x)
    x -= 1



