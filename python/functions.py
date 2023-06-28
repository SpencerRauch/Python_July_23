#functions - block of reusable code, may take input, will have output

def say_hello(name,times=1):
    # print("Hello")
    return f"Hello {name}, how are you? \n" * times
    
print(say_hello("Spencer", 10))
print(say_hello("Bob"))
# print(say_hello(10, "Spencer")) these arguments are not in the right order

#function calls are replaced by what that function returns

#default parameter
#when you supply a default value to use if a parameter is not passed an argument
#note that parameters fill up left to right by default
#defaulted parameters must come at the end of your parameter list

#named arguments
#when you specify which parameter the argument is for
#named arguments must come after positional arguments
print(say_hello("Steve",times=3))