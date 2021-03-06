# -*- coding: utf-8 -*-
"""ProblemsOfPython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v6sg5Jc6GnEsfSWWOfRRbdHH9yB79hGl

1.string=" I AM INDIAN									3
 Now, (i) replace "D" with "t"
          (ii)reverse string
          (iii) convert string in lower case
"""

string="I AM INDIAN"
print(string.replace("t", "D"))
print(string[:: -1])
print(string.lower())

"""2. Write a program to append and extendtwo lists and also find new list’s length.		2
  list1= [1,2,3,4,5]
  list2= [55,223,56,76,87]

"""

lst1=[1,2,3,4,5]
lst2=[55,223,56,76,87]
lst2.append(lst1)
print(lst2)
print(len(lst2))
lst2.extend(lst1)
print(lst2)

"""3. Write a program to count total characters in a string using for loop."""

str=input()
sum=0
for i in str:
  sum=sum+1
print(sum)

"""4. Write a Python program to check character is lowercase or uppercase"""

chr=input()[0]
if chr.islower():
  print("\n"+chr,"has lowercase")
elif chr.isupper:
  print("\n"+chr,"has uppercase")  
else:
  print("\n"+chr,"not a character")

"""5. Write a program to find average of n numbers"""

print("Enter the Value of n: ")
n = int(input())
print("Enter " +n+ " Numbers: ")
nums = []
for i in range(n):
    nums.insert(i, int(input()))

sum = 0
for i in range(n):
    sum = sum+nums[i]

avg = sum/n
print("\nAverage = ", avg)

num = int(input('How many numbers: '))
total_sum = 0
for n in range(num):
  numbers = float(input('Enter number : '))
  total_sum += numbers
avg = total_sum/num
5print('Average of ', num, ' numbers is :', avg)

"""6. Write a program to find square root of the input given by user."""

a=int(input())
print(a*a)

"""7. Write a program to find factorial of n number"""

num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)

"""8. Write a programto find the Last Digit in a number."""

num = int(input("Please Enter any Number: "))
last_digit = num % 10
print("The Last Digit in a Given Number %d = %d" %(num, last_digit))

"""9.Write a program to sort the given List in Ascending Order.
	list = [56,37,85,13,06,93,103]		

"""

lst="[56,37,85,13,06,93,103]"
lst.sort()
print(lst)

"""10. Write a program to remove numbers greater than 50 from the given list.
[10,30,20,40,60,90,15,45,75]

"""

lst=[10,30,20,40,60,90,15,45,75]
for i, x in enumerate(lst):
    if x > 50:
        lst.pop(i)
print(lst)

"""11 Write a Python Program to Create Dictionary of keys and values are square of keys. ( such as { 1:1, 2:4, 3:9, _ _ _ _ }  )	"""

y=dict()
for x in range(1,n):
    y[x]=x**2
print(y)

"""12. Write a program to find the sum of Arithmetic Progression Series in general.  """

a=int(input( enter first term of A.P.))
d=int(input(enter common difference))
n=int(input(number of terms))
sum=n(a+(n-1)d)/2
print(sum)

"""13.Write a program to check is a number palindrome or not """

num=int(input("Enter number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

"""14. Write a Program to print the following pattern.						5

* 
   * * 
  * * * 
 * * * * 
* * * * * 


"""

print("Print  Pyramid using asterisk symbol ")

space=3
star=2
print("*")
for d in range(4):
  for i in range(space,-1,-1):
    print("",end="")
  space=1
  for j in range(0,star):
    print("*",end="")
  star+1=1
  print()

"""15. Write a program to find Strong Number.
 (Strong number is a number whose sum of the factorial of digits is equal to the original number. Such as 145 is strong number. 145 = 1!+4!+5!)	

"""

num = int(input(" Enter the Number:"))  
sum = 0  
temp = num  
  
while(temp > 0):  
    fact = 1  
    rem = temp % 10  
  
    for i in range(1, rem + 1):  
        fact = fact * i  
  
    print("Factorial of %d = %d" %(rem, fact))  
    sum = sum + fact  
    temp = temp // 10  
  
print("\n Sum of Factorials of a Given Number %d = %d" %(num, sum))  
      
if (sum == num):  
    print(" The given number is a Strong Number")  
else:  
    print(" The given number is not a Strong Number")