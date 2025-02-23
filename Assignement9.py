Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
and average_of_vehicle.

Ans1. class vehicle:
  def __init__(self,name_of_vehicle, max_speed, average_of_vehicle):
    self.name_of_vehicle=name_of_vehicle
    self.max_speed=max_speed
    self.average_of_vehicle=average_of_vehicle
    

Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
Create a method named seating_capacity which takes capacity as an argument and returns the name of
the vehicle and its seating capacity.

Ans2. class vehicle:
  def __init__(self,name_of_vehicle, max_speed, average_of_vehicle):
    self.name_of_vehicle=name_of_vehicle
    self.max_speed=max_speed
    self.average_of_vehicle=average_of_vehicle
    
class car(vehicle):
  def seating_capacity(self, capacity):
    self.capacity=capacity
    return self.capacity, self.name_of_vehicle
    
obj=car("Honda",120,20)
print(obj.seating_capacity(9))


Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.
Ans3. When a child class has more than 1 parent class that means when a single class inherits
 the properties of multiple classes then it is known as multiple inheritance.

Programming example:
class class1:
  def meth_class1(self):
    print("Class1 method")
    
class class2:
  def meth_class2(self):
    print("class2 method")
  
  
class class3(class1, class2):
  pass

obj=class3()
obj.meth_class1()
obj.meth_class2()



Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
class.

Ans4: Getter and setter are functions that are used to access and update the values of private 
variable of the class. Since private variable cannot be accessed directly outside the class with 
object to ensure the data security, so we use getter and setter functions when we need to access 
or update the values of those variables.

class student:
  def __init__(self,name,roll_no):
    self.__name=name
    self.__roll_no=roll_no 
    
  def setter(self, name, roll_no):
    self.__name=name
    self.__roll_no=roll_no
    
  def getter(self):
    return self.__name, self.__roll_no
    
std=student("abhinav",303)
print(std.getter())
std.setter("abhi",101)
print(std.getter())

Here in this program, we have used getter function to access the value of variables 
name and roll_no and to set/update the values of these variable we use setter function.


Q5.What is method overriding in python? Write a python code to demonstrate method overriding.
Ans5. Method overriding is the ability of a subclass to provide a specific/different implementation 
of a method that is already defined in its superclass. This allows the subclass to modify 
or extend the behavior of the method without changing the original method in the superclass.
When we override a method, the method in the subclass must have the same name and signature 
as the method in the superclass.


class parent:
  def method(self):
    print("this is parent class method")
    
class child(parent):
  def method(self):
    print("This is child class method")
    
    
obj1=child()
obj1.method()

obj2=parent()
obj2.method()

Here the function method() of parent class is overriden in the child class













