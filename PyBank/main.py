# importing the csv file
import os
import csv

csvpath = os.path.join('', 'Resources', 'budget_data.csv')

with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)

    csv_header = next(csvreader)
    total = 0
    print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        data = list(csvreader)
        TotalMonths = len(data)
        print("Total Months: " + " "+ str(TotalMonths))
        Total += sum(int(row[1])
        print(Total)