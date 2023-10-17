# Initialize an empty list to store grades
grades = []

# Ask the user to enter grades for each module
module1 = float(input("Enter the grade for Module 1: "))
grades.append(module1)

module2 = float(input("Enter the grade for Module 2: "))
grades.append(module2)

module3 = float(input("Enter the grade for Module 3: "))
grades.append(module3)

module4 = float(input("Enter the grade for Module 4: "))
grades.append(module4)

module5 = float(input("Enter the grade for Module 5: "))
grades.append(module5)

module6 = float(input("Enter the grade for Module 6: "))
grades.append(module6)

# Calculate the lowest grade, highest grade, sum, and average
lowest_grade = min(grades)
highest_grade = max(grades)
total_grades = sum(grades)
average_grade = total_grades / len(grades)

# Display the results
print("\nResults:")
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {total_grades}")
print(f"Average Grade: {average_grade:.2f}")
