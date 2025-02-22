Q1. What is Abstraction in OOps? Explain with an example.

Ans1.  Absraction hides irrelevant details from the user and show the details that are 
relevant to the users. 

Data abstraction in Python is a programming concept that hides complex 
implementation details while exposing only essential information and functionalities to users. 
In Python, we can achieve data abstraction by using abstract classes and abstract classes 
can be created using abc (abstract base class) module and abstractmethod of abc module.

Ex-->
import abc

class abstract:
  
  @abc.abstractmethod
  def abs_method(self):
    pass
  
class demo(abstract):
  def abs_method(self):
    print("Demo for abstract class and method")
    
obj= demo()
obj.abs_method()

Q2. Differentiate between Abstraction and Encapsulation. Explain with an example.
Ans2. Encapsulation is the practice of bundling data and methods into a class, while 
abstraction is the practice of hiding implementation details.  Abstraction is used to simplify 
the complex program, the encapsulation is used to hide the data and functions inside the 
class for data security.
 
 
 
Q3. What is abc module in python? Why is it used?
Ans3. The abc module in Python stands for Abstract Base Classes. It's a module that 
allows to define abstract classes and methods. Whenever we want to create abstract method or
classes, we import this module.  By using abc module, we enforce that certain methods must be 
implemented in subclasses. Abstract classes act as a blueprint for other classes, 
ensuring that subclasses implement specific methods without having to rewrite common functionality.


Q4. How can we achieve data abstraction?
Ans4. Data abstraction can be achieved with the help of encapsulation. In order to achieve it,
we will declare the varaibles of the class as private so that it cannot be accessed outside the class
and will create getter() and setter() methods to acess or manipulate the values of those variables.
In this way it will not be possible for anyone to directly access the data variables of the class.

Exmaple-->

class employee:
  def __init__(self,name,id):
    self.__name=name 
    self.__id=id
    
  def get_data(self):
    return self.__name, self.__id
    
  def set_data(self,name,id):
    self.__name=name 
    self.__id=id  
    
obj=employee("alok",3003)
print(obj.get_data())
obj.set_data("karan",6006)
print(obj.get_data())

Here in the clas employee, we have declared the variables name and id as private. Due to which 
these variable can neither be accessed outside the class nor it`s value can be changed without
the functions set for accessing or change the values (get_data() and set_data()).


Q5. Can we create an instance of an abstract class? Explain your answer.
Ans5. No, we cannot create an instance of abstract class in python because an abstract class 
is incomplete class. It simply provides blueprint for other classes to inherit from. The purpose
of an abstract class is only to provide a template for the child classes.















