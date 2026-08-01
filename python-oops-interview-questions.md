# Python OOP Interview Questions & Answers - Study Guide

## Table of Contents
1. [Basic OOP Interview Questions](#basic-oop-interview-questions)
2. [Intermediate Python OOP Interview Questions](#intermediate-python-oop-interview-questions)
3. [Advanced Python OOP Interview Questions](#advanced-python-oop-interview-questions)


(#https://chatgpt.com/share/6873f1ef-9880-8011-b800-dabc210eef86)
---

## Basic OOP Interview Questions

### 1. What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a fundamental paradigm in Python which is designed to model real-world entities through classes and objects. It offers features like **encapsulation, inheritance, polymorphism, and abstraction** enabling developers to write reusable, modular, and maintainable code.

### 2. What are the key features of OOP?

The key features of OOP are:

- **Encapsulation**: Bundles data and methods within a class, hiding internal details from outside access.
- **Abstraction**: Hides complex implementation details and exposes only necessary functionality.
- **Inheritance**: Allows a new class to inherit properties and methods from an existing class.
- **Polymorphism**: Enables a single interface to represent different behaviors.

### 3. What is a class and an object in Python?

- **Class**: A blueprint for creating objects, defining their properties and methods.
- **Object**: An instance of a class.

**Example:**
```python
class Dog:
    species = "Canis lupus"  # Class variable

    def __init__(self, name, breed):
        self.name = name     # Instance variables
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

# Create objects (instances)
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.speak())  # Buddy says Woof!
print(dog1.species)  # Canis lupus
```

### 4. What is the difference between a class and an instance?

- **Class**: Defines the structure and behavior (attributes and methods).
- **Instance**: A concrete occurrence of a class with actual data.

### 5. What is the `__init__` method in Python?

The `__init__` method is a constructor used to initialize an object's attributes when it is created and it is also known as constructor. The `__init__` method is part of Python's object-oriented programming (OOP) mechanism and is used to set up the initial state of the object when it is instantiated.

**Example:**
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
```

### 6. What is `self` in Python classes?

`self` is a reference to the current instance of the class. It is used to access attributes and methods of the class. When you define a method inside a class, the first parameter of the method is always `self`, which allows the method to refer to the object (or instance) on which the method was called.

### 7. What is the difference between instance variables and class variables?

- **Instance variables**: Instance variables unique to each object.
- **Class variables**: Shared among all objects of a class.

**Example:**
```python
class Car:
    wheels = 4          # Class variable (shared by all cars)

    def __init__(self, color):
        self.color = color   # Instance variable (unique to each car)

c1 = Car("Red")
c2 = Car("Blue")

print(c1.wheels)  # 4
print(c2.color)   # Red
print(c2.wheels)  # 4
print(c2.color)   # Blue
```

### 8. What is inheritance in Python?

Inheritance allows a class to inherit attributes and methods from another class. Inheritance enables the child class to inherit the properties (attributes) and behaviors (methods) of the parent class, and it can also define its own additional attributes and methods or override existing ones.

**Example:**
```python
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):         # Dog inherits from Animal
    def speak(self):       # Method overriding
        return "Dog barks!"

a = Animal()
print(a.speak())   # Animal makes a sound

d = Dog()
print(d.speak())   # Dog barks!
```

### 9. What is method overloading in Python?

**Method overloading** in Python refers to the ability to define multiple methods with the same name but with different **parameters** (different numbers or types of arguments).

**Example:**
class Calculator:
    def add(self, a, b=0, c=0):  # Method overloading via default parameters
        return a + b + c

calc = Calculator()
print(calc.add(5))        # Output: 5
print(calc.add(5, 3))     # Output: 8
print(calc.add(5, 3, 2))  # Output: 10
```

### 10. What is method overriding in Python?

Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This means that the subclass can "override" the behavior of the method inherited from the parent class, providing a different version that is more suitable for the subclass.

**Example:**
```python
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):  # Overrides parent speak()
        return "Dog barks!"

a = Animal()
print(a.speak())  # Output: Animal makes a sound

d = Dog()
print(d.speak())  # Output: Dog barks!
```

---

## Intermediate Python OOP Interview Questions

### 11. What is polymorphism in Python?

Polymorphism allows objects to be treated as instances of their parent class, enabling different implementations for the same interface. It enables a single function, method, or operator to work with different types of objects in a way that is determined at runtime, allowing code to be more flexible and reusable.

**Example:**
class Cat:
    def sound(self): return "Meow"

class Dog:
    def sound(self): return "Woof"

# A function that accepts any object with a 'sound' method (Polymorphism)
def make_sound(animal):
    print(animal.sound())

make_sound(Cat())  # Output: Meow
make_sound(Dog())  # Output: Woof
```

### 12. What is encapsulation, and how does Python achieve it?

Encapsulation is one of the fundamental principles of OOP. It allows the internal representation of an object to be hidden from the outside world and exposes only what is necessary through a controlled interface.

**Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self.public_name = "Savings"      # Public attribute
        self._protected_id = 12345        # Protected attribute (convention)
        self.__balance = balance          # Private attribute (name mangled)

    def get_balance(self):                # Public getter method
        return self.__balance

acc = BankAccount(1000)
print(acc.public_name)        # Output: Savings
print(acc._protected_id)      # Output: 12345
print(acc.get_balance())      # Output: 1000
# print(acc.__balance)        # Raises AttributeError (private)
print(acc._BankAccount__balance)  # Output: 1000 (access via name mangling)
```

### 13. What is the `super()` function in Python?

`super()` allows access to methods of the parent class and it's often used to call the parent class's constructor.

**Example:**
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls parent constructor to initialize 'name'
        self.age = age

c = Child("Alice", 20)
print(c.name, c.age)  # Output: Alice 20
```

### 14. What are abstract classes in Python?

Abstract class is a class that serves as a blueprint for other classes. It defines a structure that derived classes must follow but does not provide full implementation, abstract classes cannot be instantiated directly which means they are meant to be subclassed.

**Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

s = Square(4)
print(s.area())  # Output: 16
# Shape()  # Raises TypeError: Can't instantiate abstract class Shape
```

### 15. What is the difference between `is` and `==`?

- `is` checks if two objects are the same instance (identity)
- `==` checks if the two objects have the same value (equality)

### 16. What is multiple inheritance in Python?

Multiple inheritance allows a subclass to inherit features from multiple parent classes, making it more versatile and capable of combining behaviors from different sources.

```python
class ChildClass(ParentClass1, ParentClass2, ...):
    # Class body
```

### 17. What is the diamond problem in multiple inheritance? How does Python handle it?

The **Diamond Problem** in multiple inheritance is a classic issue that arises when a class inherits from two classes that both inherit from a common ancestor. The problem occurs because, in such a scenario, it's unclear which version of the inherited method should be invoked when the method is called on the subclass.

Python handles this using Method Resolution Order (MRO).

### 18. What are class methods in Python?

Class methods are methods bound to the class rather than its instances. They are defined with the `@classmethod` decorator and accept `cls` as the first argument, allowing them to access and modify class-level state.

**Example:**
```python
class Student:
    school = "High School"  # Class variable

    @classmethod
    def get_school(cls):
        return cls.school  # Accesses class variable

print(Student.get_school())  # Output: High School
```

### 19. What is the difference between `staticmethod` and `classmethod`?

- **`classmethod`**: Bound to the class. It receives the class (`cls`) as an implicit first argument. It can access and modify class variables.
- **`staticmethod`**: Not bound to the class or instance. It behaves like a regular function grouped inside the class namespace. It cannot access or modify class/instance state.

**Comparison Example:**
```python
class MyClass:
    class_var = "Class Level"

    def __init__(self, val):
        self.instance_var = val

    # 1. Instance Method (default)
    def inst_method(self):
        return f"Instance variable: {self.instance_var}, Class variable: {self.class_var}"

    # 2. Class Method
    @classmethod
    def cls_method(cls):
        return f"Accesses class variable: {cls.class_var}"

    # 3. Static Method
    @staticmethod
    def static_method():
        return "Utility function: no access to class/instance data"

obj = MyClass("Instance Level")
print(obj.inst_method())      # Output: Instance variable: Instance Level, Class variable: Class Level
print(MyClass.cls_method())   # Output: Accesses class variable: Class Level
print(MyClass.static_method())# Output: Utility function: no access to class/instance data
```

### 20. What are magic methods in Python?

Magic methods (dunder methods) start and end with double underscores providing operator overloading and custom behaviors.

**Examples:** `__str__`, `__len__`, `__init__`, etc.

---

## Advanced Python OOP Interview Questions

### 21. How does Python handle garbage collection?

Python uses automatic garbage collection to manage memory by identifying and removing unused objects and it employs reference counting and a cyclic garbage collector.

### 22. What is metaclass in Python?

A metaclass is a class of a class that defines how classes behave and classes are instances of metaclasses. Essentially, metaclasses define the "rules" for building classes, much like a class defines the rules for creating objects.

**Example:**
```python
class Meta(type):
    # This is an empty metaclass that inherits from 'type'
    pass
  
class Demo(metaclass=Meta):
    # The 'metaclass=Meta' instructs Python to use the 'Meta' metaclass
    pass
```

### 23. How is data hiding implemented in Python?

Data hiding is implemented using private attributes (`__attribute`) and even though it is not completely hidden, it is still difficult to access without name mangling.

### 24. What is the purpose of `__slots__` in Python classes?

`__slots__` attribute limits the attributes that can be added to an instance improving memory usage.

**Example:**
```python
class Point:
    __slots__ = ['x', 'y']  # Restricts attributes to x and y only, saving memory

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x, p.y)  # Output: 1 2

# p.z = 3  # Raises AttributeError: 'Point' object has no attribute 'z'
```

### 25. What is the Global Interpreter Lock (GIL) and its impact on Python OOP?

The GIL ensures only one thread executes Python bytecode at a time affecting multithreaded programs. Its purpose is to prevent multiple native threads from executing Python bytecode at the same time, ensuring thread safety in Python's memory management system.

### 26. How do you achieve operator overloading in Python?

Operator overloading is achieved using magic methods like `__add__` and `__eq__`.

**Example:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloads the + operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)
```

### 27. What is the difference between shallow copy and deep copy in Python?

- **Shallow copy**: Creates a new object but does not copy the nested objects inside it
- **Deep copy**: Creates a new object and recursively copies all objects within it, including nested objects

### 28. What is the difference between composition and inheritance?

- **Inheritance**: "Is-a" relationship (e.g., a Car is-a Vehicle)
- **Composition**: "Has-a" relationship (e.g., a Car has-a Engine)

### 29. How do you implement design patterns like Singleton in Python?

Singleton ensures only one instance of a class exists. It's a design pattern that ensures a class has only one instance and provides a global point of access to it.

**Example:**
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True (both point to the same instance)
```

### 30. Explain Python's MRO with an example.

Python's Method Resolution Order (MRO) determines the order in which classes are searched when calling a method or accessing an attribute. It is crucial in object-oriented programming, especially when dealing with multiple inheritance.

**Example:**
```python
class A:
    def show(self): print("Show from A")

class B(A):
    def show(self): print("Show from B")

class C(A):
    def show(self): print("Show from C")

class D(B, C):
    pass

d = D()
d.show()          # Output: Show from B (follows MRO: D -> B -> C -> A -> object)
print(D.mro())    # Output list of class resolution order
```

### 31. How would you identify the MRO of a class programmatically?

We can identify the Method Resolution Order (MRO) of a class programmatically in Python using:

1. **Using the `mro()` method**: Returns a list of classes in the order they are checked for method resolution
2. **Using the `__mro__` attribute**: Directly provides the MRO as a tuple of classes

---

## Additional Practice Examples

### Complete OOP Example - Student Management System

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

student = Student("John Doe")
student.add_grade(80)
student.add_grade(90)
print(f"Student: {student.name}, Average: {student.get_average()}")  # Output: Student: John Doe, Average: 85.0
```

---



### 30. What are SOLID Principles in OOP?

**Answer:**
SOLID principles are five fundamental design principles in object-oriented programming that help create more maintainable, flexible, and scalable code.

### **1. Single Responsibility Principle (SRP)**
**Definition:** A class should have only one reason to change (one responsibility).

```python
# ❌ Bad: One class handles user data AND database operations
class User:
    def __init__(self, name):
        self.name = name
    def save(self):
        print(f"Saving {self.name} to Database")

# ✅ Good: Separated responsibilities
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to Database")
```

### **2. Open-Closed Principle (OCP)**
**Definition:** Classes should be open for extension but closed for modification.

```python
# ❌ Bad: Adding a new shape type requires modifying calculate_area
class AreaCalculator:
    def calculate(self, shape):
        if shape.type == "square": return shape.side ** 2
        elif shape.type == "circle": return 3.14 * shape.radius ** 2

# ✅ Good: New shapes can be added by extending the Shape class without changing existing code
class Shape:
    def area(self): pass

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14 * self.radius ** 2
```

### **3. Liskov Substitution Principle (LSP)**
**Definition:** Subclasses should be replaceable with their base classes without breaking the program.

```python
# ❌ Bad: Penguin inherits from Bird but crashes when flying (violating LSP)
class Bird:
    def fly(self): return "Flying"

class Penguin(Bird):
    def fly(self): raise Exception("Cannot fly")

# ✅ Good: Refactored hierarchy to ensure safe substitution
class Bird:
    def move(self): return "Walking"

class FlyingBird(Bird):
    def move(self): return "Flying"
```

### **4. Interface Segregation Principle (ISP)**
**Definition:** Clients should not be forced to implement interfaces/methods they do not use.

```python
# ❌ Bad: Robot is forced to implement eat()
class Worker:
    def work(self): pass
    def eat(self): pass

class Robot(Worker):
    def work(self): return "Working"
    def eat(self): raise NotImplementedError()

# ✅ Good: Split into smaller interfaces
class Workable:
    def work(self): pass

class Eatable:
    def eat(self): pass

class Robot(Workable):
    def work(self): return "Working"
```

### **5. Dependency Inversion Principle (DIP)**
**Definition:** Depend on abstractions, not concrete implementations (loose coupling).

```python
# ❌ Bad: Service is tightly coupled to MySQL database class
class MySQL:
    def save(self): return "Saving to MySQL"

class Service:
    def __init__(self):
        self.db = MySQL()

# ✅ Good: Service depends on Database abstraction
class DBConnection:
    def save(self): pass

class MySQL(DBConnection):
    def save(self): return "Saving to MySQL"

class Service:
    def __init__(self, db: DBConnection):
        self.db = db
```

### **Summary of SOLID Benefits:**

1. **Maintainability**: Code is easier to modify and extend
2. **Testability**: Each component can be tested in isolation
3. **Flexibility**: Easy to adapt to changing requirements
4. **Scalability**: System can grow without becoming unwieldy
5. **Reusability**: Components can be reused in different contexts
6. **Readability**: Code is more organized and easier to understand

### **When to Apply SOLID Principles:**

- **During Design Phase**: Plan your architecture with SOLID in mind
- **Code Reviews**: Check if code violates any SOLID principles
- **Refactoring**: Use SOLID principles to improve existing code
- **Team Development**: Establish SOLID as coding standards
- **Complex Systems**: Especially important for large, complex applications

**Remember:** SOLID principles are guidelines, not rigid rules. Apply them judiciously based on your specific context and requirements. Over-engineering simple solutions can sometimes be counterproductive.

---


## Key Takeaways for Interviews

1. **Understand the four pillars**: Encapsulation, Inheritance, Polymorphism, and Abstraction
2. **Know the difference between class and instance variables**
3. **Understand method overriding vs overloading**
4. **Be familiar with special methods (magic methods)**
5. **Know about inheritance types and MRO**
6. **Understand composition vs inheritance**
7. **Be able to implement design patterns like Singleton**
8. **Know about abstract classes and interfaces**
9. **Understand memory management and garbage collection**
10. **Practice implementing complete OOP examples**

This study guide covers all the essential Python OOP concepts commonly asked in interviews. Practice implementing these concepts with real-world examples to solidify your understanding.

---

## 🟢 Simple OOP Examples (Quick Reference)

> These are short, easy-to-remember programs for each OOP concept. Great for last-minute revision!

---

### ✅ 1. Class & Object (Simplest Form)

```python
class Dog:
    def __init__(self, name):
        self.name = name          # instance variable

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Tommy")
d.bark()   # Tommy says Woof!
```

---

### ✅ 2. `__init__` Constructor

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Alice", 20)
print(s.name, s.age)   # Alice 20
```

---

### ✅ 3. Class Variable vs Instance Variable

```python
class Car:
    wheels = 4          # class variable (shared by all)

    def __init__(self, color):
        self.color = color   # instance variable (unique to each)

c1 = Car("Red")
c2 = Car("Blue")

print(c1.wheels)   # 4
print(c2.color)    # Blue
print(Car.wheels)  # 4  (access via class name)
```

---

### ✅ 4. Inheritance (Parent → Child)

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):         # Dog inherits from Animal
    def speak(self):       # method overriding
        print("Dog barks!")

a = Animal()
a.speak()   # Animal makes a sound

d = Dog()
d.speak()   # Dog barks!
```

---

### ✅ 5. `super()` — Calling Parent Constructor

```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)    # call parent __init__
        self.emp_id = emp_id

e = Employee("Bob", 101)
print(e.name, e.emp_id)   # Bob 101
```

---

### ✅ 6. Encapsulation (Private Variables)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def get_balance(self):
        return self.__balance       # controlled access

    def deposit(self, amount):
        self.__balance += amount

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())   # 1500
# print(acc.__balance)     # ❌ AttributeError
```

---

### ✅ 7. Polymorphism (Same method, different classes)

```python
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

class Cow:
    def sound(self):
        return "Moo"

animals = [Cat(), Dog(), Cow()]

for animal in animals:
    print(animal.sound())   # Meow, Woof, Moo
```

---

### ✅ 8. Abstraction (Using ABC)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

c = Circle(5)
print(c.area())   # 78.5

# Shape()  # ❌ Can't instantiate abstract class
```

---

### ✅ 9. Method Overriding

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):               # overrides parent method
        print("Hello from Child")

p = Parent()
p.greet()   # Hello from Parent

c = Child()
c.greet()   # Hello from Child
```

---

### ✅ 10. Method Overloading (Using default args)

```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))        # 5
print(calc.add(5, 3))     # 8
print(calc.add(5, 3, 2))  # 10
```

---

### ✅ 11. `@classmethod` vs `@staticmethod`

```python
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):          # has access to class
        return cls.count

    @staticmethod
    def greet():                 # no access to class or instance
        return "Hello!"

obj1 = MyClass()
obj2 = MyClass()

print(MyClass.get_count())  # 2
print(MyClass.greet())      # Hello!
```

---

### ✅ 12. Magic / Dunder Methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):           # called by print()
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):    # called by +
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)         # Point(1, 2)
print(p1 + p2)    # Point(4, 6)
```

---

### ✅ 13. Multiple Inheritance

```python
class A:
    def hello(self):
        print("Hello from A")

class B:
    def world(self):
        print("World from B")

class C(A, B):    # inherits from both A and B
    pass

obj = C()
obj.hello()   # Hello from A
obj.world()   # World from B
```

---

### ✅ 14. MRO — Method Resolution Order

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):   # Diamond problem
    pass

d = D()
d.show()                          # B  (follows MRO)
print(D.__mro__)                  # D -> B -> C -> A -> object
```

---

### ✅ 15. Composition ("has-a" relationship)

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()    # Car HAS-A Engine

    def drive(self):
        return self.engine.start() + " → Car moving"

my_car = Car()
print(my_car.drive())   # Engine started → Car moving
```

---

### ✅ 16. Property Decorator (Getter & Setter)

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):              # getter
        return self._name

    @name.setter
    def name(self, value):       # setter
        if value:
            self._name = value

p = Person("Alice")
print(p.name)     # Alice
p.name = "Bob"
print(p.name)     # Bob
```

---

### ✅ 17. Singleton Design Pattern (Simplest)

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()

print(a is b)   # True  (both point to same object)
```

---

### ✅ 18. `__slots__` (Memory Optimization)

```python
class Point:
    __slots__ = ['x', 'y']   # only these attributes allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x, p.y)   # 1 2
# p.z = 3         # ❌ AttributeError (not in __slots__)
```

---

### ✅ 19. Data Hiding (Name Mangling)

```python
class Secret:
    def __init__(self):
        self.public = "visible"
        self._protected = "semi-hidden"
        self.__private = "hidden"   # name mangling

s = Secret()
print(s.public)              # visible
print(s._protected)          # semi-hidden  (accessible but not recommended)
# print(s.__private)         # ❌ AttributeError
print(s._Secret__private)    # hidden  (name mangling workaround)
```

---

### ✅ 20. Simple SOLID — Single Responsibility

```python
# ❌ BAD: One class doing everything
class Report:
    def generate(self): pass
    def save_to_db(self): pass    # should not be here
    def send_email(self): pass    # should not be here

# ✅ GOOD: Each class has one job
class Report:
    def generate(self):
        return "Report data"

class ReportSaver:
    def save(self, report):
        print("Saved:", report)

class EmailSender:
    def send(self, report):
        print("Emailed:", report)

r = Report()
data = r.generate()
ReportSaver().save(data)
EmailSender().send(data)
```

---

> 💡 **Tip:** These simple examples are enough to explain any OOP concept in 2-3 sentences during an interview. Always mention the concept name → definition → quick code example.