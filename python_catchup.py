print("hello owlrd")
print("1")
print("2")
print("3")
print("4")
print("5")

# single line comments in python are with '#'
"""multiline commnents are with 
with 3x " or ' on either side

with the Python Indent extension installed:
    best to just write the 3x "'s
    then write the comment and add line breaks as go along,
    don't line break before even writing the comment
"""

"""
remember unlike c++, python doesn't care about variable type at point of initalisation
nor do I need to end each line with ';' anymore
var names can't start with number, either letter or underscore
"""
test_var = 4+5
print (test_var)
print(type(test_var))

print("2")
print("3")
print("4")
print("---------------")

# strings & arrays---------------------------
w = "Hello, Python!"
print(w)
print(type(w))
print(len(w))

# add strings together into one longer string----------------
new_string = "abc" + "def"
print(new_string)
print(type(new_string))

# cant subtract / divide / multiple two strings together
#   but can multiple str by int (but not a float)------------
newest_string = "abc" * 3
print(newest_string)
print(type(newest_string))

# convert between datatypes-------------------------
#   str & int to float
my_num = "1.12321"
print(my_num)
print(type(my_num))

my_num_to_smth_else = float(my_num)
print(my_num_to_smth_else)
print(type(my_num_to_smth_else))

# Conditions and Conditional Statements---------------------------------
#   if statement syntax----------------------------------------
def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp >= 38:
        message = "Fever!" 
    return message

print("37C = ", evaluate_temp(37))
print("38C = ", evaluate_temp(38))
print("39C = ", evaluate_temp(39))

#   if else statement syntax----------------------------------------
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

print(evaluate_temp_with_else(37)) # does the same really

#   if elif else syntax----------------------------------------
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

print("18C = ", evaluate_temp_with_elif(18))
print("35C = ", evaluate_temp_with_elif(35))
print("36C = ", evaluate_temp_with_elif(36))
print("37C = ", evaluate_temp_with_elif(37))
print("38C = ", evaluate_temp_with_elif(38))
print("39C = ", evaluate_temp_with_elif(39))

# intro to lists & arrays---------------------------------
#   lists ig----------------------------------------
#       lists used to represent large category of individual items
#       python lists use [] with each element separated by commas
#           elems in lists have to be of a datatype, eg each in ""
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)
print(len(flowers_list)) #  using len in python means actually getting
#                           the number of elems in a list, instead of
#                           the total bytes afforded to it like in c++

#   getting stuff outta a list via Slicing-----------------------
#       can pull a segment of a list: put the `:` on front/back of list
#           eg  first x entries:    `[:x]`
#               last y entries:     `[-y:]`
print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

#   removing items from list-------------------------------------------
flowers_list.remove("globe thistle")
print(flowers_list)

#   add items at end of list---------------------------------------------
flowers_list.append("snapdragon")
print(flowers_list)

#   other datatypes in lists---------------------------------------------
#       list of elements that are int
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
print("Total books sold in one week:", sum(hardcover_sales))
print("Average books sold in first 5 days:", sum(hardcover_sales[:5])/5)
print("Average books sold in last 3 days:", sum(hardcover_sales[-3:])/3)