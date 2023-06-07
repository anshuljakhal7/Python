'''Python Program to Find Prime Numbers in a Given Range'''
# lower_value = int(input("Please, Enter the Lowest Range Value: "))
# upper_value = int(input("Please, Enter the Upper Range Value: "))
#
# print("The Prime Numbers in the range are: ")
# for number in range(lower_value, upper_value + 1):
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 break
#         else:
#             print(number)
# -----------------------------------------------------------

'''Python Program to Check Prime Number'''
# num=int(input("Enter number: "))
#
# if num>2:
#     for i in range(2,num):
#         if num % i==0:
#
#             break
#     else:
#         print("Prime number ")
# else:
#     print(("Enter number > 2"))
# --------------------------------------------

'''Python Program to Check Whether a Given Number is Perfect Number'''
'''A perfect number is a positive integer that is equal to the sum of its positive divisors, 
excluding the number itself.123 For instance, 6 is a perfect number because its divisors are
1, 2, and 3.'''

# num=int(input("Enter number: "))
# temp=0
# for i in range(1,num):
#     if num % i==0:
#         temp+=i
# print("Given number is Perfect number") if temp==num  else print("Not Perfect number")

# ---------------------------------------------------
'''Python Program to Check Armstrong Number'''
'''The sum of the cubes of its digits is equal to the number itself'''
# num=int(input("Entr number: "))
# check=num
# result=0
# while num:
#     digit=num%10
#     result+=digit**3
#     num=num//10
# print("Given number is Armstrong number") if check==result else print("Not Armstrong")

# ---------------------------------------------------
'''Sum of First N Natural Numbers in Python'''

# num=int(input("Entr number: "))
# result=0
# for i in range(num+1):
#     result+=i
# print("sum of N natural number: ", result)
# ------------------------------------------------------

'''Python Program to Check if a Number is a Strong Number'''
'''Strong numbers are those numbers whose sum of factorial of each digits is equal to the original number.
Strong Number Examples, 1 is strong number because 1!=1, 2 is strong number
 i.e. 2! = 2, 145 is strong number i.e. 1! + 4! + 5! = 1 + 24 + 120 = 145 etc.'''

# num=int(input("Enter the number: "))
# check=num
# result=0
# while num:
#     a=num%10
#     f=1
#     for i in range(1,a+1):
#         f=f*a
#         a=a-1
#     result=result+f
#     print(result)
#     num=num//10
# if result==check:
#     print("Strong number")
#-----------------------------------------------------------------
'''Python Program to Print the Natural Numbers Summation Pattern'''
# num=int(input("Enter the number: "))
# num1=num
# for i in range(1,num+1):
#     a=0
#     for j in range(1,i+1):
#         print(j,sep=" ",end=" ")
#         if(j<i):
#             print("+",sep=" ",end=" ")
#         a += j
#     print("=",a)
