# ─── Inheritance Example ───────────────────────────────────────────────────────

class Animal:
    """Parent / Base class"""

    def __init__(self, name):
        self.name = name          # shared attribute, accessible in child too

    def speak(self):
        print(f"{self.name} makes a sound.")

    def breathe(self):
        print(f"{self.name} breathes air.")   # inherited by ALL children


# Dog inherits everything from Animal
class Dog(Animal):
    def speak(self):              # ← override parent method
        print(f"{self.name} says: Woof!")


# Cat inherits everything from Animal
class Cat(Animal):
    def speak(self):              # ← override parent method
        print(f"{self.name} says: Meow!")

    def purr(self):               # ← new method only in Cat
        print(f"{self.name} purrs...")


# ─── Usage ─────────────────────────────────────────────────────────────────────

d = Dog("Bruno")
d.speak()        # Dog's own method  → Bruno says: Woof!
d.breathe()      # Inherited method  → Bruno breathes air.

print()

c = Cat("Kitty")
c.speak()        # Cat's own method  → Kitty says: Meow!
c.breathe()      # Inherited method  → Kitty breathes air.
c.purr()         # Cat-only method   → Kitty purrs...

print()

# isinstance() — checks inheritance chain
print(isinstance(d, Dog))     # True
print(isinstance(d, Animal))  # True  ← Dog IS-A Animal
print(isinstance(d, Cat))     # False

print()

# ─── MRO (Method Resolution Order) ────────────────────────────────────────────
# Python uses C3 Linearization algorithm to decide the lookup order.
# Rule: Child → Parent(s) left-to-right → object (base of all classes)

print(Dog.__mro__)       # tuple form
print(Dog.mro())         # list form  → [Dog, Animal, object]

print()

# ─── Multiple Inheritance + MRO (Diamond Problem) ──────────────────────────────
#
#         A
#        / \
#       B   C
#        \ /
#         D
#
# Without MRO, calling D().hello() could call A.hello() TWICE.
# Python's C3 algo ensures A is called only once, in the right order.

class A:
    def hello(self):
        print("A.hello")

class B(A):
    def hello(self):
        print("B.hello")
        super().hello()   # delegates up the MRO chain

class C(A):
    def hello(self):
        print("C.hello")
        super().hello()

class D(B, C):            # MRO: D → B → C → A → object
    pass

print(D.mro())            # [D, B, C, A, object]
print()
D().hello()
# Output:
#   B.hello   ← D inherits from B first
#   C.hello   ← super() in B goes to C (not A!) — MRO at work
#   A.hello   ← super() in C finally reaches A