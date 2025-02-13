Q1. Explain with an example each when to use a for loop and a while loop.

Ans1. for and while both loops are used when we want to execute certain statement/instructions multiple times in a loop until certain condition is met.
Ex: Printing numbers from 1 to 10:
  
i=1 
while i<=10:
  print (i)
  i=i+1
  
in this example the statement print(i) and i=i+1 will be executed till the value of i is less than or equal to 10 and as a result numbers from 1 to 10 will be printed.
  
Similar example with for loop:
  
  for i in range(10):
    print(i)
    
In the second program also the same this is happening. For is printing all values from 0 to 9. print() is being printed multiple times since all the values given by range() are retrieved.



Q2. Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.

Ans2. Printing sum of number (1-10) With while loop:
  i=1 
result=0

while i<=10:
  result=result + i
  i= i+1 

print(result)

# Printing product of first 10 natural numbers with While loop:

i=1
result=1 

while i<=10:
  result =result *i 
  i=i+1 
  
print(result)

# Performing same operations with for loop:
# for sum:
result =0
for i in range(11):
  result=result +i
  
print(result)

# for product:
result=1 
for i in range(11):
  if i==0:
    continue
  result=result*i
  
print(result)


Q3. Create a python program to compute the electricity bill for a household.

The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
You are required to take the units of electricity consumed in a month from the user as input.
Your program must pass this test case: when the unit of electricity consumed by the user in a month is
310, the total electricity bill should be 2250.

Ans3. 

unit= int(input("Enter the units of electicity"))

if unit>=300:
  a=unit-300
  bill=a*20
  bill= bill + 2050
  print("your electricity bill is :")
  print(bill)
  
elif unit>=200 and unit<300:
    a= unit-200
    bill= a*10
    bill= bill + 1050
    print("your electricity bill is :")
    print(bill)
    
elif unit >=100 and unit <200:
    a=unit-100
    bill=a*6
    bill=bill+ 450
    print("your electricity bill is :")
    print(bill)
    
elif unit < 100:
  bill =unit*4.5
  print("your electricity bill is :")
  print(bill)
  
  

Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
that list.

# Program with for loop:
l1= range(101)
l2=[]
for i in l1:
  if i==0:
    continue
  cube=i*i*i 
  if cube%4==0 or cube%5==0:
    l2.append(i)
print(l2)

#Program with while loop:

l1=range(101)
i=1 
l2=[]
while i<=100:
  cube= l1[i]*l1[i]*l1[i]

  if cube%4==0 or cube%5==0:
    l2.append(l1[i])
  i=i+1
print(l2)


Q5. Write a program to filter count vowels in the below-given string.

s="I want to become a data scientist"
count=0
for i in s:
  if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=="O" or i=="U":
    count=count+1
print(count)










































