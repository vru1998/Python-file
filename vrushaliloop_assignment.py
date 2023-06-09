# -*- coding: utf-8 -*-
"""vrushaliLoop_Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DgzWt31r8hT9PHLQsvwkb8J__POzcWRi
"""

#1. WAP to print even numbers from 121 to 229 using for loop.
for i in range(121,230):
    if i%2==0:
        print(i)

#2. WAP to print odd numbers from 521 to 229 using while loop.
n=521
while n>=229:
    if n%2!=0:
        print(n)
    n=n-1

#3. WAP to show the use of break statement ( in for loop).
for i in range(0,11):
    i=i+1
    if i%2==0 and i%3==0:
        break
    else:
        print(i)

#4. WAP to find GCD and LCM of given number.
num1=int(input("Enter the number:- "))
num2=int(input("Enter the number:- "))
i=1
while i<=num1 and i<=num2:
    if num1%i==0 and num2%i==0:
        gcd=i
    i=i+1
print("The G.C.D. of",num1,"and",num2,"is",gcd)

#5. Write a Python program to print all alphabets from a to z using for loop.
import string
print("Alphabets from a-z->")
for i in string.ascii_lowercase:
    print(i,end=" ")

#6. Write a Python program to find sum of all even numbers between 1 to n.
n=int(input("Enter the range:- "))
sum=0
for i in range(n):
    if i%2==0:
        sum=sum+i
print("Sum of 1 to",n,"even numbers is:-",sum)

#7. Write a Python program to find sum of all odd numbers between 1 to n.
n=int(input("Enter the range:- "))
sum=0
for i in range(n):
    if i%2!=0:
        sum=sum+i
print("Sum of 1 to",n,"odd numbers is:-",sum)

#8. Write a Python program to count number of digits in any number.
num=int(input("Enter the number:- "))
count=0
while num>0:
    n=num%10
    num=num//10
    count+=1
print("Total count of digits in given no.:- ",count)

#9. Write a Python program to calculate product of digits of any number.
num=int(input("Enter the number:- "))
prod=1
while num>0:
    n=num%10
    num=num//10
    prod=prod*n
print("Total product of digits in given no.:- ",prod)

#10. Write a Python program to find frequency of each digit in a given integer.
num=int(input("Enter the number:- "))
print("Digit\tFrequency")
for i in range(0,10):
    count=0;
    temp=num;
    while temp>0:
        digit=temp%10
        if digit==i:
            count+=1
        temp=temp//10;
    if count>0:
        print(i,"\t",count)

#11. Find all prime number between 400 to 300.
for i in range(400,300,-1):
    j=2
    flag=1
    while j<i:
        if i%j==0:
            flag=0
            break
        j=j+1
    if flag==1:
        print(i,"is prime number")

#12. WAP to print table of given no.
num=int(input("Enter the no:- "))
for i in range(1,11):
    print(num*i)

#13. WAP to print squares from 1 to 20.
print("No --> Square")
for i in range(1,21):
    print(i,"-->",i**i)

#14. WAP to accept base and index from user and calculates power.
base=int(input("Enter the base:- "))
index=int(input("Enter the index:- "))
power=base**index
print(power)

# 15. 1!+2!+3!.........+n! find s.
sum=1
i=1
num=int(input("Enter the no:- "))
while i<=num:
    sum=sum*i
    i=i+1
print("Sum of factorials of 1 to",num,"numbers is :-:",sum)

#15.WAP to check given no is armstrong or not.
rem=0
sum=0
num=int(input("Enter the no:-"))
a=num
while num>0:
    rem=num%10
    sum=sum+(rem**3)
    num=num//10
print(sum)
if sum==a:
    print("The given number is armstrong")
else:
    print("The given number is not armstrong")

#17. WAP to check given no is palindrome or not. Original =Reverse
num=int(input("Enter the number:-"))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if temp==rev:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")

#18. WAP to check given no is automorphic or not
#input n=25 output Automorphic as 25*25=625
num=int(input("Enter the number:- "))
digits=len(str(num))
square=num**2
last_digits=square%pow(10,digits)
if last_digits==num:
    print("The",num,"is automorphic number")
else:
    print("The",num,"is not automorphic number")

#19. WAP to find given number is Harshad/Niven number or not
#An harshad number is an integer number divisible by sum of its digit
#Eg 18 sum=9 and 18 is divisible by 9
num=int(input("Enter the number:-"))
temp=num
digit=sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit
    temp=temp//10
if num%sum==0:
    print(num,"is harshad number")
else:
    print(num,"is not harshad number")

#20. Print all palindrome numbers from 100 to 500.
for num in range(100,501,1):
    temp=num
    rev=0
    while temp>0:
        dig=temp%10
        rev=rev*10+dig
        temp=temp//10
    if num==rev:
        print(num,"is palindrome number")