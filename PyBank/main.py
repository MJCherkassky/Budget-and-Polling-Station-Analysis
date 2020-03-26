# * Your task is to create a Python script that analyzes the records to calculate each of the following:
import os #import whatever modules you need
import csv

def analyze_budgets(file):
#Define variables
    allmonths = 0
    profitsum = 0
    greatestincrease = 0
    greatestincmonth = 0
    greatestdecrease = 0
    greatestdecmonth = 0
    previouschange = 0

    changes = [] 

    csvpath = os.path.join("..", "..", "..", "Classwork", "vu-nsh-data-pt-02-2020-u-c", "03-Python", "Homework", "Instructions", "PyBank", "Resources", "budget_data.csv") #set path where it reads CSV file
    with open(csvpath, encoding ="utf8") as csvfile: #open CSV file set delimiters
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)#skip your header row
        for row in csvreader:
            date = (row[0]) #assign variables for each row
            profit = int(row[1]) #make sure it's an integer so you can do maths  
            profitsum += profit #define a variable that has counted the length of your monts list
            allmonths +=1 #sum months as it runs through csv file
            change = profit - previouschange #calculate changes
            if allmonths != 1:
                changes.append(change)
            if change > greatestincrease: # The greatest increase in profits (date and amount) over the entire period - highest gain between two entries of column 2 and include month and amount
                greatestincrease = change
                greatestincmonth = date
            if change < greatestdecrease: # The greatest decrease in losses (date and amount) over the entire period - greatest losses between two entries in column 2 and include month and amount
                greatestdecrease = change
                greatestdecmonth = date
            previouschange = profit
        avgchg = round(sum(changes)/len(changes), 2) # The average of the changes in "Profit/Losses" over the entire period - Also sum of all values in column 2 / total number of rows

        analysis = f"""
        Total Profit: ${profitsum}
        Total Months: {allmonths}
        Average Monthly Change: ${avgchg}
        Greatest Increase: ${greatestincrease}, {greatestincmonth}
        Greatest Decrease: ${greatestdecrease}, {greatestdecmonth}
        """

        print(analysis)
    
        output_file = "output.txt"
        with open(output_file, "w") as doc:
            doc.write(analysis)
path = os.path.join("Resources", "budget_data.csv")
analyze_budgets(path)
