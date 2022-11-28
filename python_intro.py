first_name = 'Kathleen'
last_name = "Malone"
full_name = first_name + ' ' + last_name
print(full_name)
repeat = "repeat" * 5
print(repeat)

# A string is a list of characters that can be accessed using an index place
first_letter = first_name[0]
print((first_letter))

# Python has a short cut to access elements starting from the end of the list using negative index places
# This works with any list not just strings
last_letter = first_name[-1]
print(last_letter)
second_last = first_name[-2]
print(second_last)

# Slice a string
# string[start_index:end_index-1]
first_two_chars = first_name[0:2]
print(first_two_chars)
last_two_chars = first_name[-2:]
print(last_two_chars)

# Use in operator to find an element in a list
if 'K' in first_name:
    # Notice here the single quotes are also printed
    # Use double quotes for a string if a single quote is embedded in string
    # Use single quotes for a string if a double quote is embedded
    print("There is a 'K' in first name")

# You can also search a string or list using a for loop
# You can use either syntax for a for loop
# if only one argument is passed to the range function, the range starts at 0
#for i in range(0,len(first_name)):
for i in range(len(first_name)):
    print(i)
    if first_name[i] == 'e':
        print("found an e")

# Comparing strings
str1 = 'platform'
str2 = 'platf0rm'
# Use == to compare strings
if str1 == str2:
    print('strings are equal')
else:
    print('strings are not equal')

# Python has many built in methods for the string
# to convert a string to all upper case use the upper method
print(str1.upper())
# Remember the method returns a new string
# str1 is still lower case 'platform'
print(str1)
# Save the string to a new variable to store it
str1_upper = str1.upper()
print(str1_upper)

# See python documentation for string methods. They may come in handy on the homework
# https://docs.python.org/2.5/lib/string-methods.html

# create a list with elements
lst1 = [2, 3, 4, 5]

# create an empty list
lst2 = []
# add elements to the list
lst2.append(10)
lst2.append(20)
lst2.append(30)
print(lst2)

# remove element 20
lst2.remove(20)
print(lst2)
# use pop to remove the last element in the list
lst2.pop()
print(lst2)

# Sum all elements in lst1
# Use for loop
sum = 0
for num in lst1:
    sum += num
print(sum)

# Use range and index place
sum = 0
for i in range(0, len(lst1)):
    sum += lst1[i]
print(sum)


# Define a function
def hello(name):
    print("Hello ", name)


hello("Joe")


# Use a default argument
def hello_default_arg(name="To whom it may concern"):
    print("Hello ", name)


# You can call it with an argument
hello_default_arg("Joe")
# Or without and it will use the default argument
hello_default_arg()


# Create a function that returns a value
def sum_list(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum


a_list = [1, 2, 3]
print(sum_list(a_list))


def return_two():
    return 1, 5


x, y = return_two()
print(x,y)
