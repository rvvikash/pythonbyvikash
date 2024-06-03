A Generator in Python is a function that returns an iterator using the Yield keyword.

def function_name():
    yield statement

def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value)
