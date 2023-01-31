import csv
employee = open('EmployeePay.csv', 'r')
employee_file = csv.reader(employee, delimiter=',')
next(employee)
for i in employee_file:
    print('first name:', i[1])
    print('last name:', i[2])
    print('Total Pay:', format(float(i[3])*float(i[4]), '.2f'))
    print('Press any key to see the next employee.')
    input()
employee.close()
