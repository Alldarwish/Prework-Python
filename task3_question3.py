# Task 3 - Coding Questions
# Question 3
print("\nTask 3 - Question 3")
#
"""Display the maximum number of given list."""

def max_num_in_list(a_list):
    """Return the max number in a_list."""
    max_number = max(a_list, default = '"The first list is empty"')
    return max_number

print(f"\nThe maximum number in the first list is:")
print(max_num_in_list([]))
print(f"\nThe maximum number in the second list is:")
print(max_num_in_list([102, 222, 15, 87, 16, 99, 1502, 2345, 11, 17]))

# End of File!