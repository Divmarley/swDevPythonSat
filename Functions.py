"""
A function is a block of code 
which only runs when it is called.


You can pass data into a function through a parameters,

A function can return data as a result. 
""" 

# Creating a Function
# In Python a function is defined using the def keyword 
# followed by the  name of the function
# followed by the round bracket ()
# then a :
# indentation a write yur logic
 
# def my_function_name():
#     print("hello")

# my_function_name()

 
# name = "ama"
# print(name)
# print("ehsrhdfwieshdsfihdsi")


"""
Arguments
Information can be passed into functions as arguments. 
Arguments are specified after the function name, 
inside the parentheses. You can add as many arguments 
as you want, just separate them with a comma. 
The following example has a function with one argument
(fname). When the function is called, we pass along a 
first name, which is used inside the function to print 
the full name: 
Example
"""
# def country_name(Cname):
#     return Cname
# print(country_name("Ghana"))
# print(country_name("nigeria"))
# print(country_name("togoo")) 

# def my_name(name):
#     print('hello')
#     print(name)
    
# my_name("ama")   

# def winner_afcon(winner="not yet"):
#     return winner +' won the afcon'
 
# print(winner_afcon("mali"))


def my_informations(*info):
    return info[0]
print(my_informations("kofi",20,"niiit"))
print(my_informations(286754,"nana",30,"niiit","ama"))
print(my_informations("kojo",234678))

# info =('nana', 30, 'niiit', 'ama')
# print(info[0])




"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments 
that will be passed into your function, add two asterisk:
** before the parameter name in the function definition.

This way the function will receive
a dictionary of arguments, and can access the 
items accordingly
"""

