import math as mt

"""
1.

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]


input=[12,35,9,56,24]
length=len(input)

def swapelements():
    '''temp=input[0]
    input[0]=input[length-1]
    input[length-1]=temp
    '''
    #alter logic
    input[0],input[-1]=input[-1],input[0]
    
swapelements()
print(input)
"""


"""
2.

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]

List = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

def swapPos():
    List[pos1-1],List[pos2-1]=List[pos2-1],List[pos1-1]

swapPos()
print(List)
"""



"""
3.

Max of two numebers
Input: a = 2, b = 4
Output: 4

Input: a = -1, b = -4
Output: -1



a = 2
b = 4
def maxofTwo(a,b):
    if a>b:
        return a
    else:
        return b
output=(maxofTwo(a,b))
print(output)
#alter Logic
print(max(a,b))

"""

"""
4.

Python program to check whether the string is Symmetrical or Palindrome
Given a string. the task is to check if the string is symmetrical and palindrome or not.
A string is said to be symmetrical if both the halves of the string are the same and
a string is said to be a palindrome string if one half of the string is the reverse of the other half or
if a string appears same when read forward or backward.

Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome   12321

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome


input="khokho"

def symmetrical(input):
    length=len(input)-1
    half=mt.ceil(length/2)
    output,output1=input[0:half],input[half:]
    if output==output1:
        return "The entered string is symmetrical"
    else:
        return "The entered string is not symmetrical"

def palindrome(input):
    output=input[::-1]
    if output==input:
        return "The entered string is palindrome"
    else:
        return "The entered string is not palindrome"


result=palindrome(input)
print(result)

result=symmetrical(input)
print(result)
"""

"""
5.

Reverse words in a given String in Python
Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks  
Input : str = "my name is laxmi"
output : str= laxmi is name my


Input = " my name is laxmi"

def Reverse(Input):
    s1=""
    s2=""
    for i in Input:
        if i!=" ":
            s1=s1+i
        else:
            s2=s1+" "+s2
            s1=""
    s2=s1+" "+s2
    print(s2)
    

Reverse(Input)
"""

"""
6.

Ways to remove i’th character from string in Python


test_str = "GeeksForGeeks"
 
# Removing char at pos 3
pos=3

def removechar(test_str):
    new_string=""
    for i in range(len(test_str)):
        if i!=pos-1:
            new_string=new_string+test_str[i]
    return new_string
new_string=removechar(test_str)
print(new_string)
"""

"""
7.

Python program to print even length words in a string

Input: s = "This is a python language"
Output: This is python language

Input: s = "i am laxmi"
Output: am

s = "This is a python language"
def evenLength(s):
    s1=""
    s=s.split()
    print(s)
    for i in s:
        if len(i)%2==0:
            s1=s1+i+" "
    print(s1)

evenLength(s)
"""

"""
8.

Find the size of a Tuple in Python


tup=(2,4,5,6,7,"anshul","jakhal",5.6,8.9,True)
print(str(tup.__sizeof__())+" bytes")
"""

"""
9.

Python – Maximum and Minimum K elements in Tuple










