# I was supposed to put a comment here
# Adams


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
print("Lowest Grade: ", low)
high = max(grades)
print("Highest grade: ",high)
Sum = sum(grades)
print("Sum of Grades: ", Sum)
average = Sum/len(grades)
print("Average: ",average)
# determine letter grade for average


if average >= 90:
    print('Your grade is: A')
else:
    if average > 80:
        print('Your grade is: B')
    else:
        if average > 70:
            print('your grade is :C')
        else:
            if average > 60:
                print('your grade is : D')
            else:
                if average < 60:
                    print('Your grade is: F') # TO DO: finish this





