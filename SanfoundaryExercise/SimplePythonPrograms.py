"""Python Program to Check if a Number is a Palindrome """
# 1234321
# number = int(input())
# num = number
# y = 0
# while (num):
#     x = num % 10
#     y = y * 10 + x
#     num = num // 10
# if y == number:
#     print("number: ", number)
#------------------------------

"""Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3 """

# limitstart=int(input("lower limitstart: "))
# endlimit=int(input("End limitstart: "))
#
# for i in range(limitstart,endlimit+1):
#     if (i%2!=0 and i%3!=0):
#         print(i,end=" ")
#----------------------------------

"""Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range"""

# limitstart=int(input("lower limitstart: "))
# endlimit=int(input("End limitstart: "))
#
# for i in range(limitstart,endlimit+1):
#     if (i%7==0 and i%5==0):
#         print(i,end=" ")

#-----------------------

"""Sum of Digits Program in Python"""

# num = int(input("Enter num: "))
# num1=num
# sum=0
# for i in range(0,len(str(num))):
#     a=num%10
#     sum=sum+a
#     num=num//10
# print("Sum of digits:",sum)

#---------------------------------
"""Python Program to Count the Number of Digits in a Number"""
# number = int(input("Enter the number: "))
# num = number
# count = 0
# while (num):
#     x = num % 10
#     count = count +1
#     num = num // 10
# print("Number of Digits in a Number %d"%(count))
#--------------------------------------

"""Python Program to Find All the Divisors of an Integer"""
# number = int(input("Enter the number: "))
# for i in range(1,number+1):
#     if (number%i==0):
#         print(i,end=" ")

#------------------------------

'''Python Program to Find the Smallest Divisor of an Integer'''
# number = int(input("Enter the number: "))
# templist = []
# for i in range(2,number+1):
#     if (number % i == 0):
#         templist.append(i)
# templist.sort()
# print("Smallest Divisor",templist[0])

#---------------------
'''Python Program to Print Binary Equivalent of a Number without Using Recursion'''
# number = int(input("Enter the number: "))
# templist = []
# for i in range(1,number+1):
#     i=bin(i)
#     templist.append(i)
# templist.sort(reverse=True)
# print(templist)
# n=int(input("Enter a number: "))
# a=[]
# while(n>0):
#     dig=n%2
#     a.append(dig)
#     n=n//2
# a.reverse()
# print("Binary Equivalent is: ")
# for i in a:
#     print(i,end=" ")
#----------------------------------

"""Python Program to Print Table of a Given Number"""
# num=int(input("Enter number: "))
# for i in range(1,11):
#     print(i*num,end=" ")

#------------------------------------------
'''Python Program to Read a Number n and Compute n+nn+nnn'''
num=int(input("Enter number: "))
temp=str(num)+str(num)
temp2=str(num)+str(num)+str(num)
out=int(num)+int(temp)+int(temp2)
print(out)
