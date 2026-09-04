#Write a Python program to show method overriding using a parent class Animal and a child class Dog.
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565010")
print("Practical-21")
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
a = Animal()
d = Dog()
a.sound()
d.sound()
