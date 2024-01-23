a decorator is a special type of function that is used to modify the behavior of another function or method.
Decorators provide a convenient syntax for applying transformations or 
adding functionality to functions without modifying their actual code
decorator is a function that take anouther function as an argument and return a function.


   ((( def decorator(printer):# we are creating the decoartor and passing the existing functionality as arugment 
    def inner():# adding other function which want to modify some using eisting functionality
        printer() #just we are calling the existing function
        print('second name vikash')# just after the calling existing function we are adding the additional functionality
    return inner


@decorator   #it behave as printer=decorator(printer) so if we declaring using @ we can ignore this and we are not so we can declare this
def printer():
    print('first name golu')
# printer=decorator(printer)
printer() #calling decorated function in always important 
# printer()    )))



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

      
     

