1. Who developed Python Programming Language? 
Ans1. Python Programming Language was developed by Guido van Rossum. First version of python was released in 1991 as Python 0.9.0

2. Which type of Programming does Python support? 
Ans2. Python supports multiple programming paradigms, including object-oriented, structured, procedural, functional, and dynamically typed programming

3. Is Python case sensitive when dealing with identifiers? 
Ans3. Yes, Python is case-sensitive when dealing with identifiers, meaning that variables, functions, and class names with the same spelling but different capitalization will be treated as different entities. 

4. What is the correct extension of the Python file? 
Ans4. The correct extension for a Python file is .py. 

5. Is Python code compiled or interpreted? 
Ans5. Python code is interpreted; that means it is executed directly by the Python interpreter line by line, without a separate compilation step beforehand.

6. Name a few blocks of code used to define in Python language?
Ans6. The following are blocks that are used to define in python language: a module, a function body, and a class definition.

For ex--> function definition:

def sum(a,b):   # function returning the sum of 2 numbers.
  return a+b
  
7. State a character used to give single-line comments in Python? 
Ans7: The character used to give single-line comment in python is '#'

8. Mention functions which can help us to find the version of python that we are currently working on?
Ans8. The functions we can use to find the version of python we are using are:
  
sys.version
sys.version_info

Both of these functions are part of sys module so before using these functions we need to import sys module in our program.

9. Python supports the creation of anonymous functions at runtime, using a construct called _________?
Ans9. lambda function.

10. What does pip stand for python? 
Ans10. In Python, pip stands for "pip installs packages". It is a tool that helps us to find, download, and install Python packages. 

11. Mention a few built-in functions in python? 
Ans11. In-built functions in python are:
  
1. print()--> used to print some text, output or the values of objects on the screen.
2. len()--> it is used to find the length of container data types like list, string and tuple.
It simply returns the number of items in a container.
3. type(): Returns the type of an object.
4. range():Returns a sequence of numbers, starting from 0 and increments by 1 (by default). However the 
increment value and starting point value can be changed by passing the parametres in it.
5. sum(): returns the sum of items of an iterator like tuple, list or set.

12. What is the maximum possible length of an identifier in Python? 
Ans12. Python itself technically allows identifiers of unlimited length, however the PEP 8 style guide recommends limiting identifiers to 79 characters to improve code readability.
So practically we cannot create an identifier of more than 79 characters in python.

13. What are the benefits of using Python? 
Ans13. There are a number of benefits of using python. 

1. Python is easy to learn and open source.
2. Python supports object oriented programming and supports core features like abstraction, encapsulation, polymorphism, and inheritance. 
3. Python is extensively used for data analysis, data cleaning and data visualization.
4. Python can also be used for building machiine learning models that can learn from data and make predictions.
5.  Python is highly portable, meaning it can run on many different types of systems.

14. How is memory managed in Python? 
Ans14. Memory management in Python is handled by the Python Memory Manager. Python uses a private heap space to store objects that are created during runtime. The Memory Manager handles all allocation and deallocation of heap memory for Python objects.

The Memory Manager in Python uses two techniques to manage memory: reference counting and garbage collection.
Reference Counting: Python uses reference counting to keep track of how many times an object is referenced in the code. Every time a new reference to an object is created, Python increments a reference counter for that object. Similarly, every time a reference is deleted, the counter is decremented. When the counter reaches zero, it means that no references to the object exist and the object can be safely deleted from memory.
Garbage Collection: Garbage collection is the process of freeing up memory that is no longer needed. Even with reference counting, there are situations where an object may have circular references, making it impossible to determine when the object is no longer needed. In such cases, Python uses a garbage collector to identify and remove objects that are no longer in use.
The garbage collector runs periodically, checking all objects in memory and identifying those that are no longer reachable. These unreachable objects are then marked for deletion and their memory is freed up.
In addition to reference counting and garbage collection, Python also uses other memory optimization techniques such as object re-use, object sharing, and memory pooling


15. How to install Python on Windows and set path variables?
Ans15. Here are the stpes to install python for Windows:

1. Download the latest version of Python for Windows. 
2. Once the installer is downloaded, run it.
Important: During installation, make sure to check the option that says "Add Python to PATH" at the bottom of the installation window. This ensures that Python is available globally in your command prompt, and you won’t need to manually set the path variables.
Select "Install Now" for a quick installation.

If you didn’t check the “Add Python to PATH” option during installation, or if you prefer to manually set the environment variables, follow these steps:
1.  Find the Python Installation Path.
2. Press Windows + X and select System-->On the left panel, click on Advanced system settings-->
In the System Properties window, click on the Environment Variables button.
3. Under System Variables, scroll down and select the Path variable, then click Edit.
4. In the Edit Environment Variable window, click New and add the path to your Python installation folder.


16. Is indentation required in python?
Ans16. Yes, indentation is required in Python; it is a crucial part of the syntax and is used to define code blocks.
Unlike many other languages, Python strictly enforces indentation. Indentation is used to indicate the start and end of a code block, like within loops or conditional statements. 
If you do not indent correctly, Python will throw an "IndentationError.







