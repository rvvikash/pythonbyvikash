Imagine you have different shapes: a circle, a square, and a triangle. Each shape has its own unique way of calculating its area. Now, let's say you want to write a program that calculates the area of any shape without knowing in advance which shape it will be.

Polymorphism is like having a single calculator that can work with any of these shapes without needing to know the specific details of each shape. It's the ability for different objects to be treated as if they are all the same type, as long as they share a common way of doing something.

In our example, polymorphism means that regardless of whether you're dealing with a circle, a square, or a triangle, you can use the same method, like calculate_area(), to find its area. Each shape class implements this method differently, but they all share the same name and purpose.

So, when you ask the program to calculate the area of a shape, it doesn't matter if it's a circle, a square, or a triangle – as long as it has the calculate_area() method, the program can use it to get the area. This flexibility and ability to treat different objects in a uniform way is what polymorphism is all about

import math

class Shape:
    def calculate_area(self):
        pass  # This method will be overridden by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Now, let's use polymorphism
shapes = [Circle(5), Square(4), Triangle(3, 6)]

for shape in shapes:
    print("Area:", shape.calculate_area())
In this code:

We define a base class Shape with a method calculate_area(). This method is left undefined (with pass) as it will be overridden by subclasses.
We define three subclasses Circle, Square, and Triangle, each implementing their own calculate_area() method.
We create instances of these shapes and store them in a list shapes.
We iterate over each shape in the list and call the calculate_area() method. Even though each shape calculates its area differently, we can treat them uniformly because they all share the same method name and purpose.
This code demonstrates polymorphism in action, where different objects are treated as if they are of the same type (Shape), allowing us to work with them in a uniform way without knowing their specific details.


Here we also override the concept to implement poly morphism :
n Python, method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. When a method is overridden in a subclass,
the subclass version of the method is called instead of the superclass version when the method is invoked on an object of the subclass.

class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Creating instances of subclasses
dog = Dog()
cat = Cat()

# Calling the overridden method
dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!

We have a base class Animal with a method make_sound(), which prints a generic animal sound.
We define two subclasses, Dog and Cat, which override the make_sound() method with their own specific sound implementations.
When we create instances of Dog and Cat and call the make_sound() method on them, the overridden version of the method in each subclass is executed, producing the specific sound associated with each animal.
