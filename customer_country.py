import csv
customers = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')
customer_file = csv.reader(customers, delimiter=',')
next(customer_file)
for i in customer_file:
    outfile.write(i[1]+' '+i[2]+' ' + i[4]+'\n')
outfile.close()
