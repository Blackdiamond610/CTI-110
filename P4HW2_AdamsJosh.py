#Josh A
#CTI110
#P4HW2

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

while True:
    employee_name = input("Enter employee name (or 'Done' to finish): ")
    
    if employee_name.lower() == 'done':
        break  
    pay_rate = float(input("Enter pay rate for {}: $".format(employee_name)))
    hours_worked = float(input("Enter hours worked for {}: ".format(employee_name)))
 
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked
    
    overtime_pay = overtime_hours * 1.5 * pay_rate
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay
 
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    num_employees += 1
    print("\nEmployee Name:", employee_name)
    print("Overtime Pay:", overtime_pay)
    print("Regular Pay:", regular_pay)
    print("Gross Pay:", gross_pay)

print("\nTotal Overtime Pay:", total_overtime_pay)
print("Total Regular Pay:", total_regular_pay)
print("Total Gross Pay:", total_gross_pay)
print("Number of Employees Entered:", num_employees)

