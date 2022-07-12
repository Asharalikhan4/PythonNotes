# loop is used to print the same line of code in repeat order.
# don't forget about the indentation.
#-------------------------------------------------


# fruits = ["Apple","Mango","Pear"];
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

#-------------------------------------------------

# wap to calculate avg height.

# student_heights = input("Input a list of the student height ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# total_height = 0
# num_of_students = 0
# for height in student_heights:
#     total_height += height
#     num_of_students += 1
# # we use the round function to round off the value.
# avg_height = round(total_height/num_of_students)
# print(avg_height)

# -------------------------------------------------

# wap to calculate the highest score from a list.
# there are func like max, min but we don't have to use it here.

# student_scores = input("Input the student score ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# highest_score = 0
# for score in student_scores:
#     if score>highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")

# -------------------------------------------------

# using range keyword with loops
# syntax - range(starting, ending, stepSize)

# for number in range(1, 10):
#     print(number)

# -------------------------------------------------

# wap to add number from 1 to 100
# sum = 0
# for number in range(1, 101):
#     sum += number
# print(sum)

# -------------------------------------------------

#wap to print the sum of all the even number from 1 to 100 including 1 to 100
# sum = 0
# for number in range(2, 101, 2):
#     sum += number
# print(sum)
# another approch
# for number in range(1,101):
#     if number%2 == 0:
#         sum+= number
# print(sum)

# -------------------------------------------------

# fizzBuzz problem
# for number in range(1, 101):
#     if number%3 == 0 and number%5== 0:
#         print("FizzBuzz")
#     elif number%5 == 0:
#         print("Buzz")
#     elif number%3 == 0:
#         print("Fizz")
#     else:
#         print(number)

# -------------------------------------------------

# final project - password generator.

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']
print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password:\n"))
nr_symbols = int(input("How many symbols would you like:\n"))
nr_numbers = int(input("How many numbers would you like:\n"))

# eazy level
password = ""
for char in range(1, nr_letters+1):
    random_char = random.choice(letters)
    password += random_char
for number in range(1, nr_numbers+1):
    random_number = random.choice(numbers)
    password += random_number
for symbol in range(1, nr_symbols+1):
    random_symbol = random.choice(symbols)
    password += random_symbol
print(password)


