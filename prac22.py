#Write a python program to show single inheritance using classes Animal and Dog.
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565005")
print("Practical-22")
class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.eat()
d.bark()
