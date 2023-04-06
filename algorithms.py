# Task 1: Even or Odd
# Given a numeric value, determine if it is even or odd.
# The function should take the value in as a parameter and return a boolean value (True if even, False if odd).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

# TIME COMPLEXITY =>  O(1)

def is_even(user_number):
    
    e_or_o = user_number%2

    if e_or_o == 0:
        return True
    else:
        return False

user_number = int(input(" \n Enter a number to find if it's even: \n"))
if is_even(user_number):
    print(f' The number {user_number} is EVEN!\n')
else:
    print(f' The number {user_number} is ODD\n')


# Task 2: Less than 100
# Given a list of numbers, determine if each item in the list is lower than 100.
# The function should take in the list as a parameter and return a boolean value (False if there are any numbers greater than or equal to 100, True if all numbers are less than 100).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

# 