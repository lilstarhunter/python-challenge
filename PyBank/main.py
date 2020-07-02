#PyBank: Financial Analysis
#Import dependent modules
import os
import csv

#set path for input and output csv file
csvpath = os.path.join("python-challenge/PyBank/Resources/budget_data.csv")

#Create file for the text output to be saved in the Analysis folder
f = open("python-challenge/PyBank/Analysis/PyBank_Analysis.txt", 'w')

#open the csv file for analysis
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
    #Set variables
    month_counter = 0
    net = 0
    max = 0
    max_month = " "
    min = 0
    min_month = " "

    for row in csvreader:
        #Count number of months in file
        month_counter +=1
        
        #Sum values 
        net += int(row[1])
        
        #Find greatest increase and month
        if int(row[1]) > max:
            max = int(row[1])
            max_month = row[0]
        
        #Find greatest decrease and month
        if int(row[1]) < min:
            min = int(row[1])
            min_month = row[0]
    
    #calculate average monthly change
    avg_change = round(net/month_counter,2)
    
    #Print report to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_counter}")
    print(f"Total: ${net}")
    print(f"Greatest Increase in Profits: {max_month} (${max})")
    print(f"Greatest Decreases: {min_month} (${min})")

     #Print report to new file
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f"Total Months: {month_counter}", file=f)
    print(f"Total: ${net}", file=f)
    print(f"Greatest Increase in Profits: {max_month} (${max})", file=f)
    print(f"Greatest Decreases: {min_month} (${min})", file=f)
