# Importing Modules to use
import os
import csv

# Input and output files
inp = "budget_data.csv"
out = "PyBank_Analysis.txt"

# declaring date and revneue lists as placeholders
date = list()
revenue = list()

# Initiating file path
csvpath = os.path.join('', 'Resources', inp)
output_path = os.path.join('', "Resources", out)

# Initiating csv reading
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Identify firs row as header
    headerline = next(csvfile)

    # identify the list for date and revenue
    for line in csvfile:
        date = list()
        revenue = list()
    
    # Initiate csv file read as 
    with open(os.path.join('Resources',inp),'r') as data:
        csvdata = csv.reader(data)

        # identify the header
        header = next(csvdata)

        # Splitting the columns within dataset by comma into date and revenue
        for col in data:
            split_col = str.split(col,',')
            date.append(split_col[0])
            revenue.append(int(split_col[1]))

    # calculate the total number of months and summary of revnue
    num_months = len(revenue)
    total_revenue = sum(revenue)

    # Declaring revenue changes as list of values
    revenue_changes = list()

    # For every element X in range of revenue explore changes and minimum and maximum values
    for x in range(len(revenue)-1):
        revenue_changes.append(revenue[x+1]-revenue[x])
        avg_revenue_change = sum(revenue_changes)/len(revenue_changes)
        max_revenue_change = max(revenue_changes)
        min_revenue_change = min(revenue_changes)
        max_date = date[revenue_changes.index(max_revenue_change)+1]
        min_date = date[revenue_changes.index(min_revenue_change)+1]

    # Printing values in console
    print("```text")
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: " + str(num_months))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Revenue Change: $" + str(round(avg_revenue_change,2)))
    print("Greatest Increase in Revenue: " + " " + str(max_date)  + " " + "($" + str(max_revenue_change)+ ")")
    print("Greatest Decrease in Revenue: " + " " + str(min_date)  + " " + "($" + str(min_revenue_change)+ ")")

    # Writting data to a file using text.write
    with open(out,"w") as text_file:
        text_file.write("Financial Analysis"+"\n")
        text_file.write("Total Months: " + str(num_months)+"\n")
        text_file.write("Total Revenue: $" + str(total_revenue))
        text_file.write("Average Revenue Change: $" + str(round(avg_revenue_change,2))+"\n")
        text_file.write("Greatest Increase in Revenue: " + " " + str(max_date)  + " " + "($" + str(max_revenue_change) + ")" + "\n")
        text_file.write("Greatest Decrease in Revenue: " + " " + str(min_date)  + " " + "($" + str(min_revenue_change)+ ")" + "\n")
        text_file.close()