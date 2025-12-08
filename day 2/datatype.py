# Datatype

# integer: whole number
# num = 10
# print(num)
# print(type(num))


# float- decimal number
# number = 10.15
# print(number)
# print(type(number))

# escape sequence
# \'
# \"
# \\
# \n
# \t

# string- alphabets, characters

# text = 'Hello, \tWorlds\'!'
# print(text)

# text = "Hello, \"Worlds\"!"   # # reassignment, Data overriding
# print(text)
# text = 1556    # reassignment, Data overriding

# print(text)

# # boolean
# is_true = True
# is_false = False

# print(is_true)
# print(is_false)

# # None
# a = None
# print(a)
# print(type(a))

# Group data type: we can store multiple data in a single variable

# list: [] is used to define list, can store multiple data, can store different datatype, mutable(changeable), ordered
# my_list = ['Ram','Shyam','Hari','Diya',50,96,25.5,True, False]
# print(my_list)
# print(type(my_list))
# my_list[1] = 10000
# my_list.append('5000')
# print(my_list)

# tuple: () is used to define tuple, can store multiple data, can store different datatype, immutable(not changeable), ordered
# my_tuple = ('Ram','Shyam','Hari',"['Diya',50,96,25.5]",True, False)
# print(my_tuple)
# print(type(my_tuple))


# set: {} is used to define set, no duplicate datas, unordered
# my_set = {'Ram','Diya','Hari','Diya',50,96,25.5,True, False,'Ram',50}
# print(my_set)

# dictionary: {} is used to define, key:value pair, no duplicate keys
my_dict = {
   2:"dia",
   1:"ram", 
   3:"ram",
   "age":50,
   2 : "shyam",
   "hobbies":["reading","coding","gaming"]
   }
print(f"I like { my_dict["hobbies"] }")




# todo:
# create a list of your hobbies and print it out as a proper sentance "I like hobby1. I like hobby2, hobby3"
# create a dictionary containing you information.print it out your info  
   # "Name: your_name(data from dictionary)
   # Age: your_age
   # Address: your_address, 
   # Hobbies: your_hobbies"

# assige a value to two variables
# a,b = 10,20
# # # swapp the datae . OUTPUT: a=20, b=10

# print("before", a ,b)
# a,b = b,a

# # a,b = "apple","ball"
# print("after",a, b)