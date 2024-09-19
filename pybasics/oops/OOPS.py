# Encapsulation: Define a class with private and public attributes
class Person:
    def __init__(self, name, age):
        self.__name = name   # Private attribute
        self.__age = age     # Private attribute

    def get_name(self):
        return self.__name   # Public method to access private attribute

    def set_name(self, name):
        self.__name = name   # Public method to modify private attribute

    def get_age(self):
        return self.__age    # Public method to access private attribute

    def set_age(self, age):
        if age > 0:
            self.__age = age  # Public method to modify private attribute
        else:
            print("Age must be positive!")

    def display_info(self):
        return f"Name: {self.__name}, Age: {self.__age}"


# Inheritance: Define a subclass that inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the parent class constructor
        self.student_id = student_id  # Additional attribute for Student

    def display_info(self):
        # Polymorphism: Override the parent class method
        parent_info = super().display_info()
        return f"{parent_info}, Student ID: {self.student_id}"


# Polymorphism: Demonstrate method overriding and dynamic method resolution
def print_person_info(person):
    print(person.display_info())  # This will call the appropriate display_info method based on the object type


# Create objects
person = Person("Alice", 30)
student = Student("Bob", 22, "S12345")

# Demonstrate Encapsulation
print(person.get_name())  # Alice
person.set_name("Alicia")
print(person.get_name())  # Alicia

# Demonstrate Inheritance and Polymorphism
print_person_info(person)   # Name: Alicia, Age: 30
print_person_info(student)  # Name: Bob, Age: 22, Student ID: S12345

# Demonstrate Encapsulation in setting and getting values
person.set_age(-5)  # Invalid age
print(person.get_age())  # 30 (age not updated)

student.set_age(23)
print(student.get_age())  # 23
