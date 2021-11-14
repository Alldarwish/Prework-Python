# Task 3 - Coding Questions
# Question 1
print("\nTask 3 - Question 1")
#
"""Greeting a user after providing his/her full name."""

def hello_name(user_name):
    """Return a username as entered by the user."""
    username = {user_name}
    return username
while True:
    print("\nPlease tell me your full name:")
    print("(enter 'q' at any time to quit)")

    u_name = input("Full Name: ")
    if u_name == 'q':
        break

    print(f"\nHello, {u_name.title()}!")
    
# End of File!