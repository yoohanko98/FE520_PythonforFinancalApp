#!/usr/bin/env python
# coding: utf-8

# # FE-520 Assignment 1
# #### Stevens Institute of Technology
# ### Author: Yoohan Ko
# ### "I pledge my honor I have abided by the Stevens Honor System"

# ### 1. Print (10pts)
#     - Define a string variable, and print it. 
#     - Define a string (I’m a student), print it.
#     - Define a string: (How do you think of this course? Describe your feeling of this course) print it in multiple line.

# In[1]:


#define a string variable
string1 = "Hello World"
print(string1 + "\n")

#define string "I'm a student"
string2 ="I'm a student"
print(string2 + "\n")

#define multiple line string
string3 = '''I think that this course serves as a good 
introduction to Python. I am excited to learn about
the advantages of Python over other coding languages.'''
print(string3)


# ### 2. Operator (15pts)
#     - Define a = 100, b = 9, calculate following problems,
#     - c=a+b, print c out.
#     - print the quotient of a/b.
#     - print the integer part of a/b.
#     - print the remainder part of a/b
#     - print the result of ’a’ to the power of b.
#     - Using logic operator to return a Boolean value for a unequal to b.
#     - Using logic operator to return a Boolean value for a greater than b.

# In[2]:


#defining variables
a = 100
b = 9

#store the sum of a and b in a new variable c, then print out c
c = a + b
print(c)

#calculate float division of a divided by b
quotient = a / b
print(quotient)

#calculate integer division a divided by b
integerdivide = a // b
print(integerdivide)

#calculate a modulo b
remainder = a % b
print(remainder)

#print the result of a to the power of b
power = a ** b
print(power)

#check if a is not equal to b
print(a != b) #print statement
a != b #boolean value

#check to see if a is greater than b
print(a > b) #print statement
a > b #boolean value


# ### 3. List Practice (30pts)
#     - Define a list Name it List A), whose items should include integer, float, and string. Please notice the length of the list should be greater than 5.
#     - Using extend and append to add another list(Name it List B) to List A. 
#     - Insert a string (’FE520’) to the second place of List A, and delete it after that. 
#     - Return and delete the last element in the List A, and print the new list. 
#     - Return a new list (Name is List C), slicing the List A from 3rd to the end. 
#     - Double size your List C.
#     - Reverse your sequence of List C.

# In[4]:


#define List_A, including an integer, float, and string
List_A = [15, 16.4, "a string"]

#define List_B
List_B = ["a string from List_B", 164,182.3]

#extend or append List_A with List_B
List_A.extend(List_B)
print(List_A)

#insert string to second place in List_A (This would be list index 1)
List_A.insert(1, "FE520")
print(List_A)

#removing this string from the list
List_A.remove("FE520")
print(List_A)

#return and delete the last element in List_A
List_A.pop()
print(List_A)

#return a ListC that slices List_A from 3rd to the end
List_C = List_A[2:]
print(List_C)

#double the size of List_C
List_C.extend(List_C)
print(List_C)

#reverse the sequence of List_C
List_C_negative = List_C[::-1]
print(List_C_negative)


# ### 4. Practice Dictionary (15 pts)
#     - Define a dictionary with 3 item (Name is Dict_A).
#     - Define another dictionary equal to Dict A, change the item value in new dictionary, but not hurt Dict A.

# In[5]:


#Defining a dictionary with 3 items
Dict_A = dict([('itemA', 100), ('itemB', 200), ('itemC', 300),])
print(hex(id(Dict_A)))

#Making a copy of Dict_A, not a reference to Dict_A
Dict_B = dict(Dict_A)
print(hex(id(Dict_B)))


# ### 5. Loop Condition Practice(30 pts)
#    Consider a sequenced list (or inversed sequence list, you need to consider an inversed sequence situation) and an inserted number. Define a function with two arguments, one is the sequenced list, another one is the inserted number. Please insert the number in the list with right place and output the new list. (Hint: you need to consider the special situation that the inserted number is smaller or greater than all numbers) 
# Example:
#     
#     Input:
#         List = [1, 2 , 4 , 9 , 17 , 25 , 63 ]
#         InsertNum = 13
#     Output:
#         NewList = [1, 2 , 4 , 9 , 13 , 17 , 25 , 63 ]

# In[44]:


# defining the insert function
def insert_list(list_prev, number):
    index = 0
    
    # first, check whether the list is normal or inverted
    if(list_prev[0] < list_prev[1]):
        print("list is a normal sequence")
        # iterate over the list using the length of the list
        for x in range(len(list_prev)):
            # print(list_prev[x])
            # figure out the index of the list item before which to insert number
            if list_prev[x] < number:
                index = x + 1
                # print("up to index: " + str(index))
    else:
        # logic is reversed for inverted lists
        print("list is a inversed sequence")
        for x in range(len(list_prev)):
            # print(list_prev[x])
            if list_prev[x] > number:
                index = x + 1
                # print("up to index: " + str(index))
            
    list_new = list_prev.copy()
    list_new.insert(index, number)
    print(list_new)
    

# list going in positive sequence
List1 = [1, 2 , 4 , 9 , 17 , 25 , 63]
# default test case
insert_list(List1, 13)
# testing use case: at the very front of the list 
insert_list(List1, 0)
# testing use case: at the very rear of the list
insert_list(List1, 100)

# list going in negative sequence
List2 = [63, 25, 17, 9, 3, 2, 1]
# default test case
insert_list(List2, 13)
# testing use case: at the very last of the list 
insert_list(List2, 0)
# testing use case: at the very front of the list
insert_list(List2, 100)

        
    


# In[ ]:




