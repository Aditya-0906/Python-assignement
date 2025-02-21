Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
Ans1. Class is a blueprint that defines the attribute and behaviour of an object. Class does not have 
a physical existence that means it does not occupy memory whereas objects do occupy memeory and have 
physical existence.

Example-->

class bank:
  def meth(self):
    print("Method of bank class")
    
b=bank()
b.meth()

Here, in this program bank is class whereas b is the object of class bank. With the object of class
bank, we can invoke functions of class and also access the public variable of the class.

Q2. Name the four pillars of OOPs.
Ans2. The four pillars of OOPs are:
1. Polymorphism.
2. Encapsulation.
3. Inheritance
4. Abstraction.

Q3. Explain why the __init__() function is used. Give a suitable example.
Ans3. __init__() is constructor method of class in python. Constructor method is the method which 
is used to initialize the object of the class. 

Example-->
class bank:
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance
    
  def get_data(self):
    return self.name, self.balance
    
b=bank("Mohan",45000)
print(b.get_data())

Here in this program our constructor function __init__() is being used to initialize the 
variable name and balance of the class.

Q4. Why self is used in OOPs?
Ans4. self is an internal pointer to the class in python. self seperates the class variables 
from the parametres that has been passed to the class while object initialization. If we take 
previous program as example then self is seperating the class variables name and balance from 
parametres that have been passed to it. self is always used to access the variables of the class 
inside the class.


Q5. What is inheritance? Give an example for each type of inheritance.
Ans5. When a class inherits the properties of other class, then this phenomenon is known as 
inheritance. The class which inherits the properties of other class is knows as child class and
the class whose properties are being inherited is called Parent class. In python there are 3 kinds of inheritance.
1. Single inheritance
2. Multilevel inheritance
3. Multiple inheritance

1. Single Inheritance: In single inheritnace there is single child class to the parent class.
For ex-->

class class1:
  def meth_class1(self):
    return "class1 method"
    
class class2(class1):
  pass 

obj=class2()
print(obj.meth_class1())

Here class1 is parent class and class2 is child class. With the help of object of class2 we 
invoke the method(meth_class1()) of class1, simple because class2 inherits the properties of
class1.

2. Multilevel Inheritance: In this inheritance there are multiple levels of inheritance. Let`s
understand with the help of a program.

class abc:
  def meth_abc(self):
    return("abc class method")
  
class xyz(abc):
  def meth_xyz(self):
    return("xyz class method")
    
class child(xyz):
  pass

obj=child()
print(obj.meth_xyz())
print(obj.meth_abc())

Here class names child is inheriting the class xyz and class xyz is inheriting the class abc.
So xyz will have the properties of class abc and the class "child" will have the properties of both the classes (xyz and abc). This is 
known as multilevel inheritance.


3. Multiple Inheritance: In this kind of inheritance there is single child class and 
multiple parent classes. That means one class inherits the properties of more than one classes.

class abc:
  def meth_abc(self):
    return("abc class method")
  
class xyz:
  def meth_xyz(self):
    return("xyz class method")
    
class child(abc,xyz):
  pass

obj=child()
print(obj.meth_xyz())
print(obj.meth_abc())

Here in this program class child is directly inheriting the porperties of abc and xyz via 
multiple inheritance.















