#Josh A
#CTI110
#P3HW2
num_employees=0
total=0

employee_name = input("Enter the name of the employee: ")

hours_worked = float(input("Enter the number of hours the employee worked this week: "))

pay_rate = float(input("Enter the employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

overtime_pay = overtime_hours * 1.5 * pay_rate

regular_pay = regular_hours * pay_rate

gross_pay = regular_pay + overtime_pay

print("Employee Name:", employee_name)
print("Pay Rate:", pay_rate)
print("Number of Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay:", overtime_pay)
print("Pay for Regular Hours:", regular_pay)
print("Gross Pay:", gross_pay)

