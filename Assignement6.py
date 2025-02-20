Q1. You are writing code for a company. The requirement of the company is that you create a python
function that will check whether the password entered by the user is correct or not. The function should
take the password as input and return the string “Valid Password” if the entered password follows the
below-given password guidelines else it should return “Invalid Password”.

Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
2. The Password should contain at least a number and three special characters.
3. The length of the password should be 10 characters long.


Ans1:
  
import string
pw=input("Please enter the password\n")

def length(s):
  return len(s)
  
def char(s):
  up=0
  low=0
  for i in s:
    if i.isupper()==True:
      up=up+1  
    elif i.islower()==True:
      low=low+1 
      
  if up >=2 and low >=2:
    return True
  else:
      return False
    
def num_ch(s):
  num=0
  ch=0
  for i in s:
    if i.isnumeric()==True:
      num=num+1 
  
  for i in s:
    if i in string.punctuation:
      ch=ch+1 
        
  if num>=1 and ch>=3:
    return True
  else:
    return False
    
if length(pw)>=10 and char(pw)==True and num_ch(pw)==True:
  print("The password is valid")
else:
  print("The password is invalid")
  
  
  
Q2. Solve the below-given questions using at least one of the following:
1. Lambda function
2. Filter function
3. Map function
4. List ComprehensioI


(i) Check if the string starts with a particular letter.
Ans(i). Lets assume that particular letter is 'Y'.
str=input("Please enter the string\n")
letter= input("Please enter the letter\n")

result=lambda str1 : True if str1[0] ==letter  else False

if result(str)==True:
  print("Given string starts with the letter ",letter)
else:
  print("Given string does not start with the letter", letter)
  
  
(ii) Check if the string is numeric.
Ans(ii):
  str1=input("Enter the string\n")

c=lambda s: s.isnumeric()

if c(str1)==True:
  print("Given string is Numeric")
else:
  print("Given string is not Numeric")

(iii)Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)]
Ans(iii):
l1=[("mango",99),("orange",80), ("grapes", 1000)]

s1=dict(l1)
s2= {k:v for k,v in sorted(s1.items())}
print(s2)

(iv)Find the squares of numbers from 1 to 10.
Ans(iv): print([i**2 for i in range(1,11)])   #Using list comprehension

(v) Find the cube root of numbers from 1 to 10.
Ans(v): print([i**(1/3) for i in range(1,11)])

(vi) Check if a given number is even.
Ans(vi): 
num= int(input("Enter the number\n"))

c= lambda i: True if i%2==0 else False

if(c(num))==True:
  print("Given number is even")
else:
  print("Given number is not even")

(vii)Filter odd numbers from the given list.
[1,2,3,4,5,6,7,8,9,10]

Ans(vii): 
l1=[1,2,3,4,5,6,7,8,9,10]

l2= list(filter(lambda x:x%2!=0, l1))
print(l2)

(viii) Sort a list of integers into positive and negative integers lists.
[1,2,3,4,5,6,-1,-2,-3,-4,-5,0]

Ans(viii):
l1=[1,2,3,4,5,6,-1,-2,-3,-4,-5,0]

l2=list(filter(lambda x: x>=0,l1))
print(l2)

l3=list(filter(lambda x: x<0, l1))
print(l3)
  
  
  