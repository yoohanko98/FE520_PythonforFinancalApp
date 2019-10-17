#!/usr/bin/env python
# coding: utf-8

# # FE-520 Assignment 2
# #### Stevens Institute of Technology
# ### Author: Yoohan Ko
# ### "I pledge my honor I have abided by the Stevens Honor System"

# ### 1. Loop Condition Practice (10pts)
#     - A ball falls freely from a certain height. After each landing, it bounces back to 1/4 of its original height, then it falls again. Define a function with two arguments, one is the original height, another one is the number of landing (Set this is a default value with 5). 
#     - Print how many total distance the ball traveled. Return the meters it bounces after the number of specific landing.

# In[17]:


# define a function to calculate ball drop total distance

def balldrop(height, bounces = 5):
    total_dist = 0
    
    for x in range(bounces):
        total_dist += height # measuring distance on the way down
        height = height / 4 # 1/4 of the previous height
        total_dist += height # measuring distance on the way up
        
    return total_dist
        
print("The total distance travelled is:", balldrop(10), "meters")


# ### 2. String Practice (35pts)
#     - Define a function to clean text:
#     1. Convert the string to single words as list.
#     2. if a token starts with or ends with a punctuation, remove the punctuation, e.g. ”world!” to ”world”, ”’hello’”to ”hello”. However, if there is a punctuation in the middle of word, e.g. It’s, we don’t remove it. (Hint: you may need to use string.punctuation method by importing string)
#     3. Replace \n to space
#     4. Convert all chars to low case.
#     5. creates a dictionary (Name: Token) containing the count of every unique token, e.g. ’it’s:5, ’hello’:1,...
#     6. print the most frequent word and its frequency by string formatting, e.g. ”The most frequent word is ”the”, its frequency is 3”.

# In[80]:


import string

def clean_text(input):
    
    # changing to lowercase
    input1 = input.lower()
    print("After changing to lowercase:\n\n" + input1)
    
    # replacing \n with space
    input2 = input1.replace('\n',' ')
    print("After replacing line breaks with space:\n\n" + input2 + "\n")
    
    # string to single word list
    input3 = input2.split()
    print("After splitting up the string into a single word list\n")
    print(input3)
    
    # removing punctuation
    input4 = []
    for item in input3:
        temp = item.strip(string.punctuation)
        input4.append(temp)
    print("\nAfter removing punctuation:\n")
    print(input4)
    
    wordfreq = []
    for w in input4:
        wordfreq.append(input4.count(w))
        
    print("Frequencies\n" + str(wordfreq) + "\n")
    
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))
    
    
# test string:
mystring = '''
This course is designed for those students have no experience or
limited experience on Python. This course will cover the basis
syntax rules, modules, importing packages (Numpy, pandas), data
visualization, and Intro for machine learning on Python. You will
need to implement what you learn from this course to do a finance
related project. This course aims to get you familiar with Python
language, and can finish a simple project with Python.
'''


clean_text(mystring)


# ### 3. Find Zero of Function (40pts)
#     - Definition: Here we define if we could find a x∗, let f(x∗) = 0, we say x∗ is the zero point of this function.
#     - In this question, we are going to use Euler method to find the zero point of function.

# ### 3.1 (20 pts)
#     Consider the function f
#         f(x) = 2x + 4
#     1. Define a lambda function with f(x) = 2x + 4
#     2. define a function to find the zero point of f(x). Be careful that in this function, your parameters with this function need to at least contain lambda function f(x), initial value of x0, constant δ, and ε.
#     Hint: The stop condition of this function should be |wn+1 − wn| < ε.
#     3. Test your function with x0 = −5 and x0 = 0

# In[ ]:





# ### 3.2 (20 pts)
#     Consider another function g:
#         g(x) = x · sin(x) − 1
#     1. Use the function you define in question 3.1, try to find the zero point of g(x), with x ∈ [−4; 4].
#     2. Plot this function g(x) in google, and see how many zero point you can find in x ∈ [−4; 4]. Think about why you cannot get all zero points with Euler method.
#     3. Modify your Euler method, and try other zero point in g(x), with x ∈ [−4; 4].

# In[ ]:




