print("Hello World")
x = 60 #variable declaration
if x > 50: #conditional 
    print("bigger than 50")
    print("another line")
else:
    pass
print("Always going to print")

# these are comments!
"""
This can be used
as a multiline
comment if we want
"""
#naming convention! snake_case = all lower case, separate by underscore <--- 
#primitives
#booleans 
bool_one = True
bool_two = False

#numbers 
my_int = 7
my_float = 7.4
print(type(my_int))
print(type(my_float))
my_result = my_int + my_float
print(type(my_result), my_result)
# float() int()

#strings - a collection of characters!
my_string = "Here is a string!"
another_string = 'This is also a string!'
contraction = "I can't believe this!"
block_string = """
    This is a string
    that goes on multiple lines
    isn't that neat?
"""
str_length = len(my_string)
print(str_length)

# print(my_string + " " + another_string + contraction + my_int) #type error! can't add int to str
print(my_string + " " + another_string + contraction + str(my_int))
#f-string
print(f"This is a f-string {my_string} - {my_int}")

#composite data types
#lists
my_nums = [1,2,3,4,5]
#          0 1 2 3 4

my_strings = ["Hello", "World"]

my_mixed_list = [123, "Cool", False]
#                 0     1      2
print(my_mixed_list[1])
my_mixed_list[1] = "Not Cool"
print(my_mixed_list)

#adding to a list:
my_mixed_list.append("New Element")
print(my_mixed_list)

# #remove from a list:
# print(my_nums.pop()) #without any arguments, pop pops the last element
# print(my_nums.pop(2))
# print(my_nums)

# #min() max() will return the minimum / maximum
# print(max(my_nums))

#slicing list[starting_index:ending_index] start inclusive end exclusive, both are optional
print(my_nums[:])

#tuples - immutable collection -- it does not change after being declared
my_tuple_nums = (1,2,3,4,5)
print(my_tuple_nums[2])
# my_tuple_nums[2] = 77

#dictionaries -- KEY VALUE PAIRS (similar to objects in JS -- note, we will have Objects in Python that mean something else)

my_info = {
    'key': 'value',
    'name': 'Spencer',
    'age': 35
}

#access - name_of_dict['name_of_key']
print(my_info)
print(f"My age is: {my_info['age']}")

#adding or reassigning values
my_info['age'] += 1 #note: no ++ in python
my_info['brand_new_key'] = "brand new value"
print(my_info)

#removing from a dict
stored_value = my_info.pop('key') #pop by key
print("After pop", my_info, stored_value)
del my_info['brand_new_key'] #remove one key without storing value
print("After del", my_info)
my_info.clear() #remove all keys and values from the dict
print("After clear", my_info)


"""
Py        Js
==        ===
None      Null
not       !
or        ||
and       &&
is <-- is is used to check if both operands are the same object

"""

y = 9
if y != 7:
    print("not seven")
if not y == 7:
    print("not seven")


