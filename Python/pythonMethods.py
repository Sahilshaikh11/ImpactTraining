# ============================================================================================================================================

# # SPLIT Method
# a = input().split("2")
# print(a)
# print(type(a))

# ============================================================================================================================================

# # Evaluate Method
# a = eval(input())
# print(a)

# ============================================================================================================================================

# # Typecasting of lists element
# a = [int(i) for i in input().split()]
# print(type(a[1]))

# ============================================================================================================================================

# # Keywords in Python
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# ============================================================================================================================================

# # Slicing [start_index : stop_index : step_count]
# s = "Happy Coding & avoid 69"
# print(s[1:20:1])
# print(s[::-1]) # Reversed Str will print

# ============================================================================================================================================

# # Pallindrome
# s = str(input())
# print("yes" if s == s[::-1] else "no")

# ============================================================================================================================================

# # Ternary Operations
# a, b=25, 35
# print(("NO","YES") [a+b<100]) # Method 1
# print((<False condition>, <True Condition> [<Condition>])) # Method 2
# print({True:"YES",False:"NO"} [100<200]) # Method 2 Ex.

# ============================================================================================================================================

# # Membership Operators(in, not in)
# print("a" in "shahil")

# ============================================================================================================================================

# # End method
# a=int(input())
# for i in range(1,11):
#     print(f"{i}*{a}=",i*a, end=" ")

# ============================================================================================================================================

# # len(), max() and min() - here max and min will return the element based on the ascii values
# a=input().split("1")
# print(a)
# print(len(max(a)))

# ============================================================================================================================================

# # create hollow box of hashes
# n=int(input())
# for i in range(n):
#     if (i==0 or i==n-1):
#         print(n*"# ")
#     else:
#         print("# "+"  "*(n-2)+" #")

# ===================================================================================================================================================

# # format() To format the output
# # Area of the circle

# pi=3.14
# r=12.5
# area = pi*r**2

# print("Area :",area)
# import math
# area1 = math.pi*r**2
# print("Area1 :{:.2f}".format(area1))  # that means the value in the variable (area1) will be stored in the :.2f telling that we want to print only 2 values after the decimal point.
# print("Area of the circle with radius {} is : {:.4f}".format(r,area1))  # Here the r will be stored in the {} and the (area1) will be stored in the :.4f
# print(math.pi)
                   
# a,b=100,200
# print("sum of {} + {} = {}".format(a,b,(a+b)))

# ====================================================================================================================================================

# # Built in string methods:
# a="hello python... happy new year"
# print(a.capitalize()) # Capitalize 0th index character of the string
# print(a.title()) # Capitalize every first char of words present in string

# ===============================================================================================================================================

# # center(width, fillchar) --> returns string with length width, padded with filllchar
# a="Python"
# print(a.center(12,'*')) # Keeps the string in center of the length width and fill the rest with fillchar
# print(a.ljust(12,"#")) # Keeps the string in left of the length width and fill the rest with fillchar
# print(a.rjust(12,'-')) # Keeps the string in right of the length width and fill the rest with fillchar
# print(a.zfill(12)) 

# ==============================================================================================================================================

# # Count(sub, start, end) --> returns count of sub string from start to end position
# a="This is Python, Py is VHLL"
# print(a.count("is"))
# print(a.count("is",2))
# print(a.count("is",2,10))

# ===============================================================================================================================================

# # endsWith(suffix, [start], [end]) --> checks if the string ends with the given suffix
# a= "Hello Python"
# print(a.endswith("on"))

# ===============================================================================================================================================

# # find(str, start, end) --> returns the index of the str if present else -1
# a="Hello Python"
# print(a.find('th'))

# ================================================================================================================================================
# # isalpha() --> checks if the strings is alphabets or not
# a="HappyNewYear"
# print(a.isalpha())

# # isdigit() --> checks if the string is digit or not
# a="354684654"
# print(a.isdigit())

# # isalmun() --> checks for either alpha or digit or both
# a="Happy190283109"
# print(a.isalnum())

# # isspace() --> checks for white space 
# a="        "
# print(a.isspace()) 

# # swapcase() --> swaps the cases of aphabets
# a="Happy New Year"
# print(a.swapcase())

# # join() --> Concatenates the string with given str
# a = ['p','y','t','h','o','n']
# print("".join(a))
# print("*".join(a))

# # strip() --> removes the extra spaces from the string
# a="   This is Python   "
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())

# =====================================================================================================================

# # enumerate() 
# s="sowbarnika"
# for i,ch in enumerate(s):
#     print(ch, "-->", i)

# =====================================================================================================================

# # Creation of empty list
# parul = []
# parul = list()
# print(parul, type(parul))
# parul= [12, 56.2, True, [10, 20, 30], 'Hello']
# print(parul[3][1])
# ----------------------------------------------------
# a=[1, 2, 3]
# print(a+[4, 5, 6])
# print(a.append([ 4, 5, 6]))
# print(a.extend([4, 5, 6]))
# print(a.insert(25, 100)) # at index 25 element 100 will be added, if index outof bound element will be inserted at last
# priny(a.pop()) # will remove last element of the list

# =====================================================================================================================

# # sort() --> to sort a list (can Modify the list), sorted() --> to sort anything (can't modify)
# li = [10,23,9,1,87,54,34]
# li.sort()
# print(sorted(li))
# print(li)
# # Reverse
# print(sorted(li, reverse = True))
# li.sort(reverse=True)
# res = list(reversed(li)) # will not modify the original list
# print(res)

# =====================================================================================================================

# # List Comprehension
# li=[i*i for i in range(11)]
# print(li)

# =====================================================================================================================

# # nested loop in List Comprehension
# n=int(input())
# li=[((i+j)*10) for i in range(1,n+1)  for j in range(1,n+1)]
# print(li)

# =====================================================================================================================

# # tuple() --> tuples are immutable
# tup = tuple() # Constructor
# tup = (29, 'python', 96.8)
# print(tup)
# a, b, c=tup # unpacking of tuples into variable
# print(a, b, c)
# # builtin fn of tuples
# .count(), .index(), max(tuple), min(tuple), sum(tuple), len(tuple)

# =====================================================================================================================

# # Set()-> It is Unordered and cant be accessed by index value as it is not stored in the contiguous manner
# '''Set is an unordered collection of values separated by commas and enclosed in {}
# Set does not contain any duplicate value, set is mutable and frozen set is immutable.
# set is not subscriptable.'''

# s= set()
# print(s,type(s))

# s={}
# print(s,type(s))

# s={100,200,"hai",True,1,0,False,100,20,"Hello"}
# print(s,type(s))

# ----------------------------------------------------------

# '''set methods'''
# s={100,200,"hai",True,1,0,False,100,20,"Hello"}

# s.add(100)
# print(s)
# s.add(50)
# print(s)
# s.add(10)
# print(s)
# s.update("hai","hello")
# s.update(["good","Hope"])
# print(s)
# s.remove(200) # removes the Item ,if the value is not found gives the error
# s.discard(200) # if value not found then Does not gives the error

# ----------------------------------------------------------

# [15:42, 02/01/2024] Pratik Patil PU: '''copy()'''
# x={11,22,33,44}
# y=x.copy()
# print(x)
# print(y)
# '''clear()'''
# y.clear() # Only clears the items but the object is still alive
# print(y)
# del y # this means the object or the Variable is also removed from the memory.

# '''difference() & difference_update() --> it'll update the var/obj after difference'''

# x={11,22,33,44}
# y={1,2,3,45,6}
# print("Difference x-y : ",x.difference(y) )
# print("Difference x-y :",x.difference(y) )
# x.difference_update(y)
# print(x)

# =====================================================================================================================

# # Union of sets
# lib1 = set(['apple', 'banana'])
# lib2 = set(['guava', 'strawberyy'])
# lib3 = lib1 | lib2
# lib3 = lib1.union(lib2)
# print(lib3)

# # Symmetric Difference
# lib3 = lib1 ^ lib2
# print(lib3) # will remove simlilar ele
# # difference
# lib3 = lib1 - lib2 # will subtract lib2 elements from ib1 if present

# # issubset and issuperset

# lib1=set(["Numpy","teli"])
# lib2=set(["pandas","Numpy"])
# lib3=set(["pandas"])
# issubset=lib1<=lib2
# print(issubset)

# issuperset=lib1>=lib2
# print(issuperset)
# issubset=lib3<=lib2
# print(issubset)
# issuperset=lib2>=lib3
# print(issuperset)

# # isdisjoint() and difference()
# x=frozenset([1,2,3,4,5])
# y=frozenset([3,4,5,6,7])

# print(x.isdisjoint(y))  # return true if the set has no  element in common
# print(x.difference(y)) #

# # Set comprehension

# square={i*i for i in range(1,6)}
# print(square)


# # Same program by set

# square =set()
# for i in range(1,6):
#     square.add(i*i)
# print(square)

# =====================================================================================================================

# # Dictionaries
# parul={1: "CSE", (2,): "IT", 'Mech': 10, 'CIVIL':20}
# print(parul)
# parul[5]='Aviation' # dict[<key>]=<value>
# print(parul)
# print(parul.keys()) # will print keys
# print(*parul.keys())
# print(parul.values()) # will print values
# print(*parul.values())
# print(parul.items()) # will print items of the dict
# print(*parul.items())
# for k,v in parul.items():
#     print(f"{k} --> {v}")

# -------------------------------------------------------------------------------    

# # heapq package
# parul={10: 'Ten', 100: 'Hundred',1000:'Thousand'}
# import heapq
# print(heapq.nlargest(2,parul))
# print(heapq.nsmallest(2,parul))

# --------------------------------------------------------------------------------

# # Dynamic input to dictionary
# student={}
# n=int(input("enter no. of students: "))
# for i in range(n):
#     rollNo = int(input())
#     name = input()
#     student[rollNo]=name
#     #or
#     # student.update({rollNo : name})
# print(student)  

# =====================================================================================================================

# ### Python Object Oriented Programming ###

# '''Classes and Objects : '''


# Classes and Objects are the fundamental components of OOPs
# A class is a prototype that defines the variable and the functinos(methods) common  to all objects.
# variables(characteristics/attributes) and functionalities (actions they perform ) defined inside the class are accessed through Objects.

# EG:
# class -> Email
# Data Members -> properties
# Methods -> (actions) - sending email,receiving email,adding attachments.
# Objects are Instantiation of the Class
# class in python is defined using the class keyword ,followed by the class name.
# Syntax : class className(object):
#             ..............Statement


# from IPython.display import Image
# Image(filename = "C:\Users\PratikPatil\OneDrive\Desktop\amazon-png-logo-vector-1.png",width=1000,height=1000)

# ---------------------------------------------------------------

# #EG :

# class Email:
#     recipient="tana@gmail.com" 
#     subject_line="Invitation"

#     def sending(self):
#         print("Email sent Successfully ")
     
#     def attachment(self):
#         print("File attached Successfully ")   
# Email.sending(0)
# Email.attachment(1)
# print(Email.recipient)
# print(Email.subject_line)

# --------------------------------------------------------------

# #EG :
# class Training:
#     college="Parul University"
#     location="Vadodara"
#     no_of_dept=100
#     tech="Python"


#     def Placement_And_Training():
#         print("Python traing Going on")
#         print("Triggered by sowbarnika")
    
# Training.college
# Training.location

# ------------------------------------------------------------------------

#  # object Creation
# objectName = className()
# objectName.methodName() # calling methods using objects

# class myname:
#     name=""

#     def my_self(self):
#         print("My name is "+self.name)
# m1,m2,m3=myname(),myname(),myname()
# m1.name,m2.name,m3.name='Shahil','Sumit','Patil'
# m1.my_self()
# m2.my_self()
# m3.my_self()

# -------------------------------------------------------------------------
# # Constructor
# class traing:
#     # init is a constructor funstion for initializing var
#     # when we create objects, constructors are automatically invoked(called)
#     # only class functions are called explicitly, but init methods dont
#     technology=""
#     def __init__(self, tech_name):
#         self.tech_name = tech_name
#         self.technology = tech_name

# t1 = traing("Python") #t1, t2 --> object of training class)
# t2 = traing("Java")
# print(t1.tech_name)
# print(t2.tech_name)

# ------------------------------------------------------------------------

# # Inheritance

# # 1.Inheritance is a mechanism that allow a new class to inherit properties and methods of anexisting class.
# # 2.The existing class a referred to as the base class or parent class and the new class is called the derived class or child class
# # 3.This concept promotes code reusability and hepls in origanizing and structure code

# # Eg

# class Billing:
    
#     def init(self, name, floors):
#         self.name = name
#         self.floors = floors

#     def display_info(self):
#         return f"{self.name} has {self.floors} floors"

# # Derived class or child class
# class House(Billing):
#     def init(self, name, floors, bedrooms):
#         super().init(name, floors)
#         self.bedrooms = bedrooms
        
#     def display_info(self):
#         base_info = super().display_info()
#         return f"{base_info} it's a house with {self.bedrooms} bedrooms."

# b = Billing("Barath villa ", 1)
# h = House("Sasi villa", 1, 2)
# print(b.display_info())
# print(h.display_info())

# -----------------------------------------------------------------------------

# # parent class
# class bird:
#     def _init_(self):
#         print("Bird is ready")
    
#     def whoisthis(self):
#         print("bird")

#     def swim(self):
#         print("Swim faster")

# # child class
# class penguin(bird):
#     def _init_(self):
#         # cll super() function
#         super()._init_() # super() will call parent class constructor / methods
#         print("Penguin is ready")

#     def whoisthis(self):
#         print("Penguin")

#     def run(self):
#         print("Run faster")

# peggy = penguin()#child class
# peggy.whoisthis()
# peggy.swim() # parent class function accessd by child class object
# peggy.run()

# # 1. Data abstraction in python refers to the concept of hiring the complex reality while exposing only the esential parts. It involves showing only what is necessary and relevant.
# # 2. this is often achieved through the use og abstract class and method.
# from abc import ABC, abstractmethod

# #Abstarct class with abstract methods
# class Television(ABC):#ABC = Abstract Class
#     def _init_(self, brand):
#         self.brand = brand
#         self.powered_on = False
    
#     @abstractmethod
#     def turn_on(self):
#         pass
    
#     @abstractmethod
#     def turn_off(self):
#         pass
    
#     @abstractmethod
#     def change_channel(self,channel):
#         pass
    
# #concrete class implementing the abstract class
# class SmartTV(Television):
#     def turn_on(self):  #turn_on is abstract func
#         self.powered_on = True
#         print(f"{self.brand} smart Tv is ON.")
        
#     def turn_off(self):  #turn_off is abstract func
#         self.powered_on = False
#         print(f"{self.brand} smart Tv is OFF.")
     
#     def change_channel(self,channel):  #change_channel is abstract func
#         if self.powered_on:
#             print(f"{self.brand} smart TV is now on channel {channel}.")
#         else:
#             print("Cannot change channel because TV is off.")

# smart_tv = SmartTV(brand = "Sony")
# smart_tv.turn_on()
# smart_tv.change_channel(5)
# smart_tv.turn_off()

# ---------------------------------------------------------------------------

# def feedback(*rating):
#     for i in rating:
#         print(i, end = "")
#     print()
    
# feedback(6)
# feedback(1,2,4,7,8,10)
# feedback(10,2,8,9,10,10,10,10,10, "good","VG","Bad")

# ====================================================================================================================

# #polymorphism - single func multiple forms
# class MessagingService:
#     def send_message(self, to, message, cc=None, bcc=None):
#         '''send message.
#         Args:
#             to (str): Recepient's email address.
#             message(str): Message content.
#             cc (str or list,optional): Email address or list of addresses
#             bcc(str or list,optional): Email address or list of addresses'''
        
#         recepient = [to]
#         if cc:
#             if isinstance(cc,list):
#                 recepient.extend(cc)
#             else:
#                 recepient.append(cc)
                
#         if bcc:
#             if isinstance(bcc,list):
#                 recepient.extend(bcc)
#             else:
#                 recepient.append(bcc)
            
#         print(f"Message sent to: {','.join(recepient)}\nContent: {message}")
        
# MessagingService.send_message

# =========================================================================================================

# # Python Array
# # 1. Datatype
# # 2. Memory allocation
# # 3. Performance
# import array as arr
# # creating an array of integers
# a = arr.array('i',[1,2,3,4,5])
# print(a,id(a))
# # creating an array of floating - point numbers
# b = arr.array('f',[0.1,0.2,0.3,0.4,0.5])
# print(b) # collections of string is not possible in python arrays
# # typebyte                  # values
# # b                     Integer with size 1 byte/td
# # B                     Unsigned integer of size 1 byte
# # c                     A character with a size of 1 byte
# # i                     A signed integer with a size of 2 bytes
# # I                     the size of the unsigned integer is 2 bytes
# # f                     this is a floating point representation of size 4 bytes
# # d                     A floating point value of 8 bytes in size
# # array.itemsize Vs len()
# import array as arr
# a = arr.array('i',[11,22,33,44,55])
# print(a.itemsize) # each integer in array is 4 bytes
# print(len(a)) # len() gives total items in array ....5 elements in the array

# ===========================================================================================================================

# # Basic array operations
# # Traverse - the elements are printed one by one
# # Insertion - adds elements at the specified index
# # Deletion - deletes the specified index of an element
# # Search - using an index or values it searches for an element
# # Update - this method updates for index of an element
# import array as arr
# a = arr.array('i',[11,22,33,44,55])
# a.insert(1,20) #insert insert values at particular index position
# print(a)
# a.append(100) #append insert value at last index
# print(a)

# ===========================================================================================================================

# class Node(object):
#     #each node has its data and a pointer that points to next node in the Linked list
#     def _init_(self,data,next = None):
#         self.data = data
#         self.next = next

#     def setData(self,data): # function to set data
#         self.data = data

#     def getData(self): # function to get data of a particular node
#         return self.data
    
#     def setNext(self,next): # function to set next node
#         self.next = next

#     def getNext(self): # function to get the next node
#         return self.next
    
# class LinkedList(object):
#     #Defining the head of the linked list
#     def _init_(self):
#         self.head = None

#     def printLinkedList(self):
#         temp = self.head
#         while(temp.next):
#             print(temp.data, end = '->')
#             temp = temp.next
#         print(temp.data)

#     #inserting the node at the beginning 
#     def insertAtStart(self,data):
#         if self.head is None: # Empty Linked List
#             newNode = Node(data)
#             self.head = newNode
#         else:
#             newNode = Node(data)
#             newNode.next = self.head
#             self.head = newNode

# li = LinkedList()
# li.head = Node(1) # Create the Head node
# li.printLinkedList()
# N = int(input("How many nodes to insert"))
# for i in range(N):
#     val = int(input("Enter the value"))
#     li.insertAtStart(val)
# li.printLinkedList()

# ==============================================================================================================

# Decorators                                                                               (10-1-24) Wednesday
# def super_function(f):
#     return f

# @super_function
# def my_function():
#     print("This is a super function")

# # @super_function will simply represent "my_function=super_function(my_function())"
# 
# ================================================================================================
# 
# def out_func():
#     def inner():
#         print("Inner Function")
#     return inner
# test1= out_func()
# print(test1)

# ==============================================================================================
# def t1():
#     n=10
#     print('Inner function',dir()) # dir() will show the local variables present in function
# print(t1())

# ==============================================================================================
# x=10
# def test():
#     x = 4
#     print(x)
# test()
# print(x) # This will throw error "UnboundLocalError: local variable 'x' referenced before assignment" and x won't be modified

# =======================================================================================================
# x=10
# def test2():
#     global x
#     x= x+1
#     print(x)
# test2()
# print(x) # here x is globally declared hence it'll be modified
# ========================================================================================================
# z=100
# def outer():
#     z=15
#     print()
#     def inner():
#         y = 10
#         nonlocal z # it'll search for variable in a local function
#         # z=55
#         # print("y=",y)
#         # print("Inside inner function: ",z)
#         # z+=10
#         print(z)
#     return inner()
# outer()
# print(z)
# ======================================================================================
# Generator function for cube of number (power 3)
# def gencubes(n):
#     for num in range(n):
#         yield num**3
# for x in gencubes(10):
#     print(x)

# ======================================================================================
# def genAlpha(start,end,skip):
#     if(start.isupper() and end.isupper()):
#         for i in range(ord(start),int(ord(end))+1,skip):
#             yield chr(i)
#     elif (start.islower() and end.islower()):
#         for i in range(ord(start),int(ord(end))+1,skip):
#             yield chr(i)
# start=input("Enter Start Value: ")
# end=input("Enter End Value: ")
# skip=int(input("Enter skipping value: "))
# for i in genAlpha(start,end,skip):
#     print(i)

# OR

# def genAlpha(start=0,end=0,update=1):
#     if start and not end:
#         start, end = end, start
#     elif not start:
#         print("No yield")
#     # if (type(start) != type(str())):
#     #     start = str(start)
#     if (type(end)==type(str())):
#         if end.isupper():
#             start = 'A'
#         else:
#             start = 'a'
#     while (start<end):
#         yield start
#         if (type(start) == type(str())):
#             t = ord(start)+update
#             start = chr(t)
#         else:
#             start+=update
# # s=input("Enter Start Value: ")
# # e=input("Enter End Value: ")
# # u=int(input("Enter Update Value: "))
# for i in genAlpha('A','Z',1):
#     print(i)

# ==========================================================================================
# import random
# def rand_num(low,high,n):
#     for i in range(0,n):
#         yield random.randint(low,high)

# for num in rand_num(1,10,12):
#     print(num)