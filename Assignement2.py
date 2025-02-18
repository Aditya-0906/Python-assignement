Q1. Create a python program to sort the given list of tuples based on integer value using a
lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

Ans1. l1= [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

d1=dict(l1)
d2 = {k: v for k, v in sorted(d1.items(), key=lambda item: item[1])}

l2=[]
for i in d2.items():
  l2.append(i)
  
print(l2)

Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Ans2. l=[1,2,3,4,5,6,7,8,9,10]

l1=list(map(lambda x: x**2,l))
print(l1)


Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

Ans3. l1=[1,2,3,4,5,6,7,8,9,10]

l2=(tuple(map(lambda x: str(x),l1)))
print(l2)


Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.

Ans4. from functools import reduce
l1=[]
for i in range(1,26):
  l1.append(i)
  
z=reduce(lambda x,y:x*y,l1)
print(z)


Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

Ans5. l1= [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

l2=list(filter(lambda x:x%2==0 and x%3==0 ,l1))
print(l2)


Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
function.
['python', 'php', 'aba', 'radar', 'level']

Ans6. l1=['python', 'php', 'aba', 'radar', 'level']

l2=list(filter(lambda x: x== x[::-1],l1))
print(l2)



























