a decorator is a special type of function that is used to modify the behavior of another function or method.
Decorators provide a convenient syntax for applying transformations or 
adding functionality to existing functions without modifying their actual code
decorator is a function that take anouther function as an argument and return a function.


def decorator(addition):
    def multiply(a,b):
        d=a*b
        print(d)
        addition(a,b)
    return multiply   

@decorator
def addition(a,b):
    c=a+b
    print(c)
# addition=decorator(addition)    
addition(4,6)    


   ((( def decorator(printer):# we are creating the decoartor and passing the existing functionality as arugment 
    def inner():# adding other function which want to modify some using eisting functionality
        printer() #just we are calling the existing function
        print('second name vikash')# just after the calling existing function we are adding the additional functionality
    return inner


@decorator   #it behave as printer=decorator(printer) so if we declaring using @ we can ignore this and if we are not so we can declare this
def printer():
    print('first name golu')
# printer=decorator(printer)
printer() #calling decorated function in always important 
# printer()    )))

*****************************************************************************************************
# Decorator function
def update_marks_decorator(func):
    def wrapper(student_name, original_marks):
        print(f"Updating marks for {student_name}:")
        updated_marks = func(student_name, original_marks)
        updated_marks += 5  # Adding 5 marks
        print(f"Updated marks: {updated_marks}")
        return updated_marks
    return wrapper

# Function with decorator
# @update_marks_decorator
def student_exam_result(student_name, marks):
    print(f"{student_name}'s original marks: {marks}")
    return marks

# Example usage
student_name = "John"
original_marks = 80
student_exam_result=update_marks_decorator(student_exam_result) #we can use this or this @update_marks_decorator both are same
updated_marks = student_exam_result(student_name, original_marks)# this we are using to call main function

output :---Updating marks for John:
           John's original marks: 80
            Updated marks: 85



********************************************************************************************************************




# Applying the decorator using the @ syntax


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

      
     

