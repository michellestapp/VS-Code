# Task 1: Even or Odd
# Given a numeric value, determine if it is even or odd.
# The function should take the value in as a parameter and return a boolean value (True if even, False if odd).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

# # TIME COMPLEXITY =>  O(1)

# def is_even(user_number):
    
#     e_or_o = user_number%2

#     if e_or_o == 0:
#         return True
#     else:
#         return False

# user_number = int(input(" \n Enter a number to find if it's even: \n"))
# if is_even(user_number):
#     print(f' The number {user_number} is EVEN!\n')
# else:
#     print(f' The number {user_number} is ODD\n')


# Task 2: Less than 100
# Given a list of numbers, determine if each item in the list is lower than 100.
# The function should take in the list as a parameter and return a boolean value (False if there are any numbers greater than or equal to 100, True if all numbers are less than 100).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

# TIME COMPLEXITY =>  O(n) 

# def less_than_100(list):
#     all_lt100 = True
#     for num in list :
#         if num >= 100:
#            all_lt100 = False
#            break
#     return all_lt100
# my_list = [10,54, 57, 75, 2]

# if less_than_100(my_list) == True:
#     print('\n All numbers under 100\n')
# else:
#     print('\n You have at least one number that is greater than or equal to 100\n')


# Task 3: Repeated Names
# Given a list of names, determine if any names are contained in the list more than once.
# The function should take in the list as a parameter and return a boolean value (True if there are any repeated names, False if there are no repeats).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.
    # counter_a = 0
    # counter_b = 1
    # num_names = len(list)
    # for counter_a in range(num_names -1):
    #     for counter_b in range(counter_a+1,num_names -1):
    #         if list[counter_a] == list[counter_b]:
    #             return True
    #             break
    #         else:
    #             counter_b += 1
    #     counter_a += 1
    #     counter_b = counter_a +1
    # return False


# # TIME COMPLEXITY =>  O(n) Two loops that cycle through the list

def repeated_names(list):

    list_2 = []
    for name_one in list:
        if name_one in list_2:
            return True
            break
        else:
            list_2.append(name_one)
    return False

list = ['Brian','Brian','Michelle','David']

if repeated_names(list) == True:
    print('\n There are duplicated names in the list\n')
else:
    print('\n There are NO duplicated names in the list\n')


#    Task 4: Sort List
# Given a list of numbers, manually sort the list into ascending order (may not use built in .sort() method).
# Suggested strategy:
# Starting with the first two numbers, compare them to see which is larger. 
# Place the lower number to the left and the higher number to the right.
# Iterate through the list, checking each pair of numbers one at a time.
# Repeat from the start until the entire list is sorted.
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

# # TIME COMPLEXITY =>  n^2 : a loop within a loop
     
def sort_list(list):
    i = 0
    j = 1

    num_indexes = len(list) - 1

    for i in range(0,num_indexes):
        for j in range(i, num_indexes+1):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                print()
                print(list)


my_list = [24,5,61,0.5,19,0,1002, 2]

sort_list(my_list)





