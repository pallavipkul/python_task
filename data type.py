# 1. Create and Print Variables

# Create variables of different types:

    #  python
# name = "John"
# print(name, type(name))
# age = 25
# print(age, type(age))
# height = 5.9
# print(height, type(height))
# is_student = True
# print(is_student, type(is_student))
     
#  Ask students to print each variable and its type using type().

# 2. Change Value and Type

#Assign a number to a variable, then change it to a string. Print the value and type before and after.

    #  python
a = 10
print(a, type(a))  # Before change
a = "ten"
print(a, type(a))  # After change
     

# 3. Guess the Type

#     Give a list of values and ask students to guess the datatype before using type() to check:

    #  python
10, 3.14, "hello", True
a=[10, 3.14, "hello", True]
print(a)
     

# 4. Variable Naming Practice

#     Ask students to create variables with meaningful names:

    #   A variable for a student’s name
students_name= "Alice"  # Valid
print(students_name, type(students_name))

    #   A variable for exam marks
exam_marks = 85
print(exam_marks, type(exam_marks))
    #   A variable for pass/fail status
is_passed = True
print(is_passed, type(is_passed))
 
# 5. Identify Errors

#     Give wrong variable assignments and ask them to correct:

    #  python
name="Alice"          # Valid
# my-age = 20          # Invalid
my_age=20          # Valid
# print(Name)          # case sensitive NameError
     

# 6. Simple Story with Variables

#     Ask students to write a mini-story using variables:

    #  python
hero = "Spider-Man"
villain = "Green Goblin"
city = "New York"
print(hero, "saved", city, "from", villain)
     

# 7. Swap Values

#     Create two variables and swap their values:

    #  python
a = 5
b = 10
print(a)
print(b)
a,b=b,a
print("a:",a)
print("b:",b)
 # After swapping: a = 10, b = 5

