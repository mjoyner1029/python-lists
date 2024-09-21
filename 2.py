# Assignment 2: Advanced List Methods and Identity Operators

# Given lists
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Task 1: Check if Alice submitted and attended
if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted her assignment and attended class.")
else:
    print("Alice either did not submit her assignment or did not attend class.")

# Task 2: Check if the two lists are identical
if submitted == attended:
    print("The two lists are identical.")
else:
    print("The two lists are not identical.")
