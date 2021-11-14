# Task 3 - Coding Questions
# Question 4
print("\nTask 3 - Question 4")
#
"""The user given year is a leap year. True / False?"""

def is_leap_year(a_year):
    
    """Verify if a_year is a leap year."""
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False

#leap_year = 1999    # Not a leap year. Expected outcome = False
#leap_year = 2004    # Leap year. Expected outcome = True
leap_year = 2000    # Leap year that is diviseable by 100 and by 400.

print(f"\n{leap_year} is a leap year...")
print(is_leap_year(leap_year))

# End of file!