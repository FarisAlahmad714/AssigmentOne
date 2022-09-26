num1 = 42 #variable declaration , initialize int
num2 = 2.3 #variable declaration , initialize float
boolean = True #data type check
string = 'Hello World' #variable declaration , initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')#initialize tuples
print(type(fruit)) #typecheck
print(pizza_toppings[1]) # Sausage , access LIST value 
pizza_toppings.append('Mushrooms') #['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives','Mushrooms'] ,
#ADD/APPEND VALUE in LISTS
print(person['name']) # Johm , access DICTIONARY value
person['name'] = 'George' #John -> George , change DICTIONARY value
person['eye_color'] = 'blue' #John -> George , add DICTIONARY value
print(fruit[2]) # banana , # Johm , access TUPLES  value

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
"""

Conditional , if statement 

"""

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

"""
Conditional , if,else if .else statement 

"""

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

"""
for loop  

"""
pizza_toppings.pop() ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
"""
['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese']

DECREASE LAST/POP VALUE in LIST

"""
pizza_toppings.pop(1)
"""
['Pepperoni','Jalepenos', 'Cheese']

DECREASE ITEM(1) IN LIST /POP VALUE
"""

print(person) 
"""
{'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False , 'eye_color' = 'blue'}

"""
person.pop('eye_color')
"""
{'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

POP ('EYE_COLOR') object VALUE in DICTIONARY

"""
print(person)
"""
{'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False , 'eye_color' = 'blue'}

"""

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break   
'''   
After 1st if statement
After 1st if statement
After 1st if statement

for loop , break , continue 
'''

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
'''
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello

function , forloop
'''
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
'''
Hello
Hello
Hello
Hello

function , for loop
'''

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
'''
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello

function , for loop
'''

"""
Bonus section
"""

# print(num3) //NameError: name <variable name> is not defined , variable must be defined before 
# num3 = 72 //string variable declaration
# fruit[0] = 'cranberry' // TypeError: 'tuple' object does not support item assignment because tuples are IMMUTABLE like the blockchain ;)
# print(person['favorite_team']) // - KeyError: 'favorite_team' , value favorite_team isnt present in the dictionary
# print(pizza_toppings[7]) IndexError: list index out of range because it doesnt exis in the index of the LIST 
#   print(boolean) - IndentationError: unexpected indent 
# fruit.append('raspberry') AttributeError: 'tuple' object has no attribute 'append
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'