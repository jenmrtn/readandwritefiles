import csv
sales = open('sales.csv', 'r')
sales_file = csv.reader(sales, delimiter=',')
salesreport = open('salesreport.csv', 'w')
next(sales_file)
salesreport.write('Customer ID'+" "+'Total'+'\n')
acc = 0
customer_ID = ''

for i in sales_file:
    if i[0] != customer_ID:
        if customer_ID:
            salesreport.write('\t'+customer_ID + ' ' +
                              format(acc, '.2f')+'\n')
        acc = 0
        customer_ID = i[0]

    total = ((float(i[3])+float(i[4])+float(i[5])))
    acc += total
salesreport.write('\t'+customer_ID+' ' + str(format(acc, '.2f')) + '\n')
salesreport.close()
sales.close()
