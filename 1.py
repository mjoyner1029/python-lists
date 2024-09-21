# Assignment 1: Python List Transformation

# Given grades
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Task 1: Replace grades below 80 with "Failed"
grades_transformed = ["Failed" if grade < 80 else grade for grade in grades]
print("Transformed grades:", grades_transformed)

# Task 2: Sort the grades in descending order
sorted_grades = sorted([grade for grade in grades if isinstance(grade, int)], reverse=True)
print("Sorted grades in descending order:", sorted_grades)

# Task 3: Calculate the average grade
average_grade = sum(grade for grade in grades if isinstance(grade, int)) / len([grade for grade in grades if isinstance(grade, int)])
print("Average grade:", average_grade)
