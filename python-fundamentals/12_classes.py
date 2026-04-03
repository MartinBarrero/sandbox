# ============================================================
# Python Fundamentals - 12: Classes
# ============================================================

# --- Empty Class ---
print("\n--- Empty Class ---")

class MyEmptyPerson:
    pass                    # pass allows defining an empty class body

print(MyEmptyPerson)        # <class '__main__.MyEmptyPerson'>
print(MyEmptyPerson())      # <__main__.MyEmptyPerson object at 0x...>

# --- Constructor, Methods and Access Modifiers ---
print("\n--- Constructor, Methods and Access Modifiers ---")

class Person:
    def __init__(self, name, lastname):
        self.full_name = f"{name} {lastname}"   # Public attribute
        self._name = name                        # Protected attribute (convention: single underscore)
        self.__id = "123"                        # Private attribute (convention: double underscore)

    def get_name(self):
        return self._name

    def get_id(self):
        return self.__id

    def walk(self):
        print(f"{self.full_name} is walking")

    def __str__(self):                           # String representation of the object
        return f"Person: {self.full_name}"

my_person = Person("Martin", "Barrero")
print(my_person.full_name)          # Public - accessible directly
print(my_person.get_name())         # Protected - accessed via method
print(my_person.get_id())           # Private - accessed via method
print(my_person)                    # Calls __str__
my_person.walk()

my_person.full_name = "Juan Miguel Herrera"     # Public attribute can be modified directly
print(my_person.full_name)
print(my_person.get_name())         # _name remains unchanged - protected from direct access
my_person.walk()

# --- Class Attributes vs Instance Attributes ---
print("\n--- Class Attributes vs Instance Attributes ---")

class Counter:
    count = 0                   # Class attribute - shared across all instances

    def __init__(self, name):
        Counter.count += 1
        self.name = name        # Instance attribute - unique to each instance

c1 = Counter("First")
c2 = Counter("Second")
c3 = Counter("Third")

print(c1.name)                  # First
print(Counter.count)            # 3 - shared by all instances

# --- Instance, Class and Static Methods ---
print("\n--- Instance, Class and Static Methods ---")

class Circle:
    pi = 3.14159                # Class attribute

    def __init__(self, radius):
        self.radius = radius    # Instance attribute

    def area(self):             # Instance method - accesses instance via self
        return self.pi * self.radius ** 2

    def perimeter(self):        # Instance method
        return 2 * self.pi * self.radius

    @classmethod
    def from_diameter(cls, diameter):   # Alternative constructor via class method
        return cls(diameter / 2)        # cls refers to Circle

    @classmethod
    def get_pi(cls):                    # Class method - accesses class attribute
        return cls.pi

    @staticmethod
    def is_valid_radius(radius):        # Static method - no access to instance or class
        return radius > 0

c1 = Circle(5)
print(c1.area())                        # 78.53975
print(c1.perimeter())                   # 31.4159

c2 = Circle.from_diameter(10)           # Alternative constructor
print(c2.radius)                        # 5.0

print(Circle.get_pi())                  # 3.14159 - called on the class, not the instance
print(Circle.is_valid_radius(5))        # True
print(Circle.is_valid_radius(-1))       # False

# --- Inheritance ---
print("\n--- Inheritance ---")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):              # Dog inherits from Animal
    def speak(self):            # Method overriding
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

my_dog = Dog("Rex")
my_cat = Cat("Whiskers")

my_dog.speak()
my_cat.speak()

print(isinstance(my_dog, Dog))      # True
print(isinstance(my_dog, Animal))   # True - Dog is a subclass of Animal

# --- super() ---
print("\n--- super() ---")

class Employee(Person):
    def __init__(self, name, lastname, company):
        super().__init__(name, lastname)    # Calls Person's __init__
        self.company = company

    def walk(self):                         # Method overriding
        super().walk()                      # Calls Person's walk
        print(f"Going to work at {self.company}")

my_employee = Employee("Martin", "Barrero", "Anthropic")
my_employee.walk()
print(my_employee.full_name)