Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25.

Ans1. The keyword used to create a function in python is def.

def odd():
  l=[]
  for i in range(1,26):
    if i%2!=0:
      l.append(i)
  return l
  
print(odd())


Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
to demonstrate their use.

Ans2. *args parameter is used for dynamic allocation of parameter values in function, when we use *args then we do not 
need to mention the number of parametres in the function definition, we can pass any number of arugments in the *args. In the *args the 
parametres are stored in the form of tuple.

Ex--> def test(*args):
  return args

print(test(1,2,"python"))

**kwargs is used when we want to parametres in the key value pair like:
  
def test1(**kwargs):
  return kwargs

print(test1(a=[1,2,3,4], b="python",c= 23.45))


Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
16, 18, 20].

Ans3. iterator is an object that allows efficient access to elements in a sequence one at a time. The method to initialize the 
iterator object is iter() and the method that is used for iteration is next().

Program-->
l= [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

l1=iter(l)
for i in range(5):
  print(next(l1))
  
  
Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
function.

Ans4. Generator function is used to generate a sequence of values in an efficient and optimized manner.
Ex--> Writting a program to create a generator for printing all the even numbers between 1 to 10.
  
def gen():
  for i in range(1,11):
    if i%2==0:
      yield i 
      
k=1 
e=gen()
while k<=5:
  print(next(e))
  k=k+1
  
Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
first 20 prime numbers. 
  
Ans5. def prime(n):
  for j in range(2,n):
    if n%j==0:
      return False
  return True
      
      
def gen():
  for i in range(2,1000):
    if prime(i)==True:
       yield i 
    
  
l1=iter(gen())
for k in range(20):
  print(next(l1))
  

Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.

Ans6. 

a=0
b=1 
count=1  

while count<=10:
  print(a)
  c=a+b 
  a=b 
  b=c 
  count= count+1
  
  
Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']
  
Ans7. s="pwskills"

l=[i for i in s]
print(l)


Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

Ans. original= int(input("enter your number"))

def pal(n):
  reverse=0 
  while n!=0:
    remainder=n%10
    reverse=reverse*10+ remainder
    n=int(n/10)
  return reverse
  
if original== pal(original):
  print("given number is palindrome")
else:
   print("given number is not palindrome")
   
   
   
Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
Ans9. l1=[i for i in range(1,101) if i%2!=0]
print(l1)
  
  
  
  
  
  
  
  