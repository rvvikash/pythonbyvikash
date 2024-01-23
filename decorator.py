a decorator is a special type of function that is used to modify the behavior of another function or method.
Decorators provide a convenient syntax for applying transformations or 
adding functionality to functions without modifying their actual code
decorator is a function that take anouther function as an argument and return a function.



# Simple decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator using the @ syntax
# @my_decorator

def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)
# Calling the decorated function
say_hello()

// Something is happening before the function is called.
// Hello!
// Something is happening after the function is called.

*************

      # Simple decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator using the @ syntax
@my_decorator

def say_hello():
    print("Hello!")
# say_hello = my_decorator(say_hello)
# Calling the decorated function
say_hello()

//       Something is happening before the function is called.
// Hello!
// Something is happening after the function is called.

# Simple decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator using the @ syntax
# @my_decorator

def say_hello():
    print("Hello!")
# say_hello = my_decorator(say_hello)
# Calling the decorated function
say_hello()

      // Hello!

      
     

