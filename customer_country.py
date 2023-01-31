import csv
customers = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')
outfile.write('Full Name   Country'+'\r')
customer_file = csv.reader(customers, delimiter=',')
next(customer_file)
acc = 0
for i in customer_file:
    outfile.write(i[1]+' '+i[2]+' ' + i[4]+'\n')
    acc += 1
outfile.write('Total Customers:'+str(acc))
outfile.close()
