1. Write a program to accept percentage from the user and display the grade according to the following criteria:
  
Marks              Grade 
>90                A 
>80 and < 90       B 
>=60 and <=80      C 
below 60           D 

Ans1. 

marks=int(input("Enter your marks\n"))

if marks>90:
  print ("A grade")
elif marks>80 and marks<=90:
  print("B grade")
elif marks>=60 and marks<=80:
  print("C grade")
else:
  print("D grade")
  
  
2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the 
following criteria: 
  
Tax                                  Cost price (in Rs).
15%                                  >100000
10%                                  >50000 and <=100000
5%                                   <=50000

Ans2. 

price=int(input("Enter the price of bike\n"))

if price>100000:
  print("Tax : 15%")
elif price >50000 and price <=100000:
  print("Tax : 10%")
elif price<=50000:
  print("Tax : 5%")
  

3. Accept any city from the user and display monuments of that city. 

City                 Monument

Delhi                Red Fort
Agra                 Taj Mahal
Jaipur               Jal Mahal

Ans3. 
city = input("Enter your city name\n")

if city=="Delhi" or city=="delhi" or city=="Delhi":
  print("Monument : Red Fort")
elif city=="Agra" or city=="AGRA" or city=="agra":
  print("Monument : Taj Mahal")
elif city=="Jaipur" or city=="JAIPUR" or city=="jaipur":
  print("Monument : Jal Mahal")
else:
  print("Pleae enter a valid city name")
  
4. Check how many times a given number can be divided by 3 before it is less than or equal to 10. 
Ans4.

num=int(input("Please enter the number"))
count=0
while num>10:
  num=num/3
  count= count+1 
  
print("the given number can be divided by 3 for", count, " times")


5. Why and When to Use while Loop in Python give a detailed description with example.

Ans5. while loop is used to execute a block of code until a certain condition is not met. 
It is particularly useful when the number of iterations needed is not known in advance.

Exmaple--> Suppose I want block of code to be executed until the value of a variable count=1 is <=5
and with each iteration the value of count will increase by 1.

count=1 

while count<=5:
  print(count)
  count= count+1
  
Here our while loop will keep getting executed until the value of count <=5, once the value of count is 
more than 5 then the iteration will stop.


6. Use nested while loop to print 3 different pattern. 
Ans6. 

i=0
while i<=2:
  i=i+1 
  j=0
  print("")
  while j<i:
    print('*',end="")
    j=j+1
    
7. Reverse a while loop to display numbers from 10 to 1. 
Ans7. 
num=10

while num>=1:
  print(num)
  num=num-1
  

8. Reverse a while loop to display numbers from 10 to 1 
Ans8. This question is same as the 7th one, so the same code will be applicable.















