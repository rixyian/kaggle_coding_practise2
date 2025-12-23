'''print("hello owlrd")
print("1")
print("2")
print("3")
print("4")
print("5")'''

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

print("16C = ", evaluate_temp(16),", 38C = ", evaluate_temp(38),", 39C = ", evaluate_temp(39))

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

#python maths in the Kaggle Notebooks tutorial:
#True div:	a / b = quotient of a & b
#Floor div:	a // b = quotient of a & b, excl fractional parts
#modulus:	a % b = in remainder after division of a by b

#True div:
print("4/2 =", 4/2,", type =",type(4/2))# 2.0
print("3/2 =", 3/2,", type =",type(3/2))# 1.5
print("1823/100 =", 1823/100,", type =",type(1823/100),"\n")# 18.23

#floor div:
print("4//2 =", 4//2,", type =",type(4//2))# 2
print("3//2 =", 3//2,", type =",type(3//2))# 1
print("1823//100 =", 1823//100,", type =",type(1823//100),"\n")# 18

#modulus:
print("4%2 =", 4%2,", type =",type(4%2))# 0
print("3%2 =", 3%2,", type =",type(3%2))# 1
print("1823%100 =", 1823%100,", type =",type(1823%100),"\n")# 23

print("ergo, floor div ('//') and modulus ('%') are opposites:\nthe former gives only the number before the decimal,\nwhilst the latter gives only the number after\n")

'''a = [1, 2, 3]
b = [3, 2, 1]
c = a # store 'a' in another variable
print("c =",c)
a = b # now replace 'a' with smth else
print("c =",c) # c has remained the same, it doesnt change after 'a' changes
b = c
print("a =",a,"\nb =",b)'''

'''	a = [1, 2, 3]
	b = [3, 2, 1]'''
'''a, b = [1, 2, 3], [3, 2, 1]
a, b = b, a
print("a: ",a,"\nb: ",b,"\n")

print ("5-3//2 =",5-3//2) # is different if u stick brackets in it
print ("(5-3)//2 =",(5-3)//2)
print ("5-(3//2) =",5-(3//2),"\n") # but does this still work if the
# brackets aren't next to an operator ('//' in this case)?

print("8-3*2-1+1 =",8-3*2-1+1)
print("(8-3)*(2(-1+1)) =",(8-3)*(2-(1+1)))'''
# ok, not sure what was such a problem here: 

#-----------------learning docstrings & fstrings again:
#   use docstrings in custom funcs in massive programs to say vital stuff
def greet(name):
    '''this should be a docstring, explaining what this func does'''
    return f"Hello, no.{name}!" # think the only difference is that this
# cuts down on the number of '""' needed in normal str that uses varibles
print(greet("234"))

# looks like an fstring can be saved as an entire variable, converting
# the new stuff into chars since the whole things is considered a `str`
'''for x in range(4):
  print(x)
  #print("Greet is now:", greet(x))
  combined_str = f"x is now {x}"
  print(combined_str, type(combined_str))'''

#   however, the saved fstring will only take that variable as it was,
#   it wont notice any change to the included variable, ie if x becomes 2
'''x = 1
combined_str = f"x is now {x}"
print(combined_str)
x = 2
print(combined_str)'''

#------------can also use __doc__ to get the same info as help()
print(f"via `.__doc__`: {greet.__doc__}")
print(help(greet)) # apparently `help()` must be the only thing in the call
# as it displays it in a structured preset format

'''-syntax for docstrings:
    -it should start with a capital letter & end with a period
    -first line should be a short desc to summarise
    -if any more lines, then leave 2nd line blank to separate the summary
    from bulk of the text below
    -the lines that follow should be 1+ paragraphs that desc the object's
    calling conventions, side effects, etc (examples of func calls is nice)'''

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

def mod_7(x):
    """Return the remainder of x after dividing by 7"""
    return x % 7

def floor_div_3(x):
    """Return the remainder of x after dividing by 7"""
    return x // 3

#help(max) #if 2+ items are highest equally, it picks the first in the order

'''print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number has the biggest quotient after being divided by 3?',
    max(51, 100, 14, key=floor_div_3),
    sep='\n',
)'''

'''def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))'''

def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)
print(f"19 y/o citizen:{can_run_for_president(19, True)}")
print(f"55 y/o non-citizen: {can_run_for_president(55, False)}")
print(f"55 y/o citizen: {can_run_for_president(55, True)}")

#-----------------example of more ddvanced conditional using bools:
have_umbrella = False
rain_level = 0
have_hood = False
is_workday = False

prepared_for_weather = have_umbrella or ((rain_level < 5) and have_hood) or (not (rain_level > 0 and is_workday))