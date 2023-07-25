import calendar

companies = []
sales = []
with open("carSale.csv") as file:
    while True:
        line = file.readline().strip()
        if line == '' : break
        companies.append(line)
        data = file.readline().strip().split(',')
        sales.append(list(map(int,data)))

grandTotal=0

for col in range(len(sales[0])):
    total = 0
    for row in range(len(companies)):
        total +=  sales[row][col]
    print("{:15}:".format(calendar.month_name[col+1]),total)
    grandTotal += total

print("Grand total: " , grandTotal)