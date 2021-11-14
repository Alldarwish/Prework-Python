# Task 3 - Coding Questions
# Question 5
print("\nTask 3 - Question 5")
#
def is_consecutive(a_list):
    
    # Sorting the given list.
    a_list = sorted(a_list)
    
    # First condition returns a boolean expression True or False.
    # Second condition returns a message when list is empty.
    if a_list:
        return a_list == list(range(a_list[0], a_list[-1] + 1))
    else:
        return "\nList is Empty."
    #
"""For testing purposes, uncomment one of the lists below to see the results."""
a_list = [0, 1, 3, 4, 6, 7, 8, 9, 11]   # False test.
#a_list = [1,5,2,4,3]                   # Positive test.
#a_list = []                            # Empty list test.

print(is_consecutive(a_list))

# End of file!