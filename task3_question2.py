# Task 3 - Coding Questions
# Question 2
print("\nTask 3 - Question 2")
#
"""Print the first 100 odd numbers."""

"""Setup a counter named current_number to zero."""
current_number = 0
while current_number < 100:
    current_number += 1
    """If the current_number is even check the next number."""
    if current_number % 2 == 0:
        continue
    print(current_number)
    
# End of File!