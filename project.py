# print ("Hello World")
# nummer1 = 5
# nummer2 = 3
# total = nummer1 + nummer2
# print (total)

# name = input ("what your name?")
# print (f"Hello, {name}!")

# length = float (input ("enter the length"))
# width = float (input ("enter the width"))

# perimeter = 2* (length + width)
# print (f"The perimeter of the rectangle is : {perimeter} ")

# # value = 42
# print (f"Value : {value}, Type : {type(value)} ")

# celsius = float (input ("Enter the temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print (f"{celsius}°C = {fahrenheit}°F")

# nummer = float(input("Enter a number: "))

# square = nummer ** 2
# print(f"The square of {nummer} is {square}.")

# a = float(input("Enter the first number; "))
# b = float(input("Enter the second number: "))
# a, b = b, a
# print(f"after swapping: a = {a}, b = {b}")

# kapital = float(input("Enter the capital amount: "))
# zinssatz = float(input("Enter the interest rate (%): "))
# laufzeit = float(input("Enter the duration (years): "))

# endkapital = kapital * (1 + zinssatz / 100) ** Laufzeit
# print (f"The final capital after {laufzeit}")

# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))

# if a > b:
#     print(f"{a} is greater than {b}")
# elif b > a:    
#     print(f"{b} is greater than {a}")
# else:
#     print(f"{a} is equal to {b}")

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if a == b == c:
#     print(f"All three numbers are equal: {a}")
# elif a >= b and a >= c: 
#     print(f"The largest number is: {a}")
#     if a == b or a == c:
#         print("some numbers are equal to the maximum")
# elif b >= a and b >= c:
#     print(f"The largest number is: {b}")
#     if b == a or b == c:
#         print("some numbers are equal to the maximum")
# else:
#     print(f"The largest number is: {c}")
#     if c == a or c == b:
#         print("some numbers are equal to the maximum")

# n = int(input("Enter a number:"))
# if n % 2 ==0:
#     print("Even")
# else :
#     print("Odd")

# score = float(input("Enter your score (0-100):"))
# if score >= 90:
#     print("very good")
# elif score >= 80:
#     print("good")
# elif score >= 70:
#     print("satisfactory")
# elif score >= 60:
#     print("sufficient")
# else:
#     print("not sufficient")

# n = float(input("Enter a number: "))
# if n > 0 :
#     print("Positiv")
# elif n < 0 :
#     print("Negativ")
# else:
#     print("Zero")

# for i in range (1 , 11):
#     print (1)

# total = 0 
# for i in range (1, 100):
#     total += i 
# print (f"Sum: {total}")

# password = ""
# while password == "john123":
#     password = input("Enter the password:")
# print ("Access granted")

# n = int(input("Enter a number"))
# for i in range(1, 11) :
#     print(f"{n} x {i} = {n * i}")
    
for i in range (1, 21):
    if i % 2 == 0:
        print(i)

import random

secret = random.randint(1, 100)
guess = None
while guess != secret:
    guess = int(input("Guess the number(1 , 100):"))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too High")

print("Correct! You found the number.")

def begruessung():
    print("Hello ,Welcome to Python!")

begruessung()

def addiere(a, b) :
    return a + b
print (addiere(5, 3))

def ist_gerade(zahl):
    return zahl % 2 == 0

print(ist_gerade(4))
print(ist_gerade(7))

