# Find the result of the expression

# Arithmetic Operators
a=10
b=20
c=a+b
print(c)               #30
print("Addition",a+b)     # 13
print("subtraction",a-b)       #7
print("multiplication",a*b)      #30
print("division",a/b)            #3.3333
print("floor Division",a//b)     #3
print("modulus",a%b)            #1
print("Exponentiation", a**b)   #1000

# comparison (Relational) Operators

x=5
y=8
print("x == y:", x == y)      # False
print("x != y:", x != y)      # True
print("x > y:", x > y)        # False
print("x <= y:", x <= y)      # True

# Logical Operators
a = True
b = False

print("a and b:", a and b)    # False
print("a or b:", a or b)      # True
print("not a:", not a)        # False

# Assignment Operators
a = 5
a += 2
print("a += 2:", a)   # 7
a *= 3
print("a *= 3:", a)   # 21
a -= 4
print("a -= 4:", a)   # 17

# Bitwise Operators
s=6
r=8
print("s & r:", s & r)    # 4
print("s | r:", s | r)    # 5
print("s ^ r:", s ^ r)    # 1

# Membership Operators (in, not in)
# Used to check if a value exists in a sequence (like a list, string, tuple, etc.)

fruits = ['apple', 'banana', 'cherry']

print('apple' in fruits)      # True
print('mango' not in fruits)  # True

#  Identity Operators (is, is not)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)     # True (values are equal)
print(x is y)     # False (different memory location)
print(x is z)     # True (same object)
