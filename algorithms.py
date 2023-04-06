# Task 1: Even or Odd
# Given a numeric value, determine if it is even or odd.
# The function should take the value in as a parameter and return a boolean value (True if even, False if odd).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

user_number = int(input(" Enter a number to find if it's even or odd: "))


e_or_o = user_number%2

if e_or_o == 0:
    print(f' The number {user_number} is EVEN!')
else:
    print(f' The number {user_number} is ODD')
