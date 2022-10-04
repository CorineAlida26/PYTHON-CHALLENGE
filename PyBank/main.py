#Dependencies 
import os
import csv

#Variables
months = []
P_loss_change = []
c_months = 0
net_profit_loss = 0
P_month_PL = 0
C_month_PL = 0
PL_change = 0
Previous_month = 0

#create path
budget_data = os.path.join("Resources", "budget_data.csv")

#open & read cvs

with open(budget_data, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")


#Read first row

    csv_header = (next(csvreader))

    print(f"Header: {csv_header}")  #prints Date, Profit/Losses
    print(type(csvreader))
    
    csvreader_2 = list(csvreader)
    print(csvreader_2)

#  start reading after header
    for row in csvreader_2:

#number of months

        c_months += 1

# Net Total of Profit/losses 

        C_month_PL = int(row[1])
      

        net_profit_loss += C_month_PL
        

        #Previous month profit loss is equal Current month proit/loss
        if Previous_month != 0: 
            PL_change = C_month_PL - Previous_month

        #Append each month to month []

            months.append(row[0])
        

        Previous_month = C_month_PL
        P_loss_change.append(PL_change)
        print(c_months)
        print(P_loss_change)
        print(net_profit_loss)
        #average of the changes in Profit/Losses 
    

    average_revenue = round(sum(P_loss_change)/(c_months - 1),2)
    print(average_revenue)

#Highest & Lowest changes in PL
greatest_increase_profits = max(P_loss_change)
greatest_decrease_profits = min(P_loss_change)

high_month =P_loss_change.index(greatest_increase_profits)
low_month = P_loss_change.index(greatest_decrease_profits)

greatest_month = months[high_month -1]
lowest_month = months[low_month -1]
print(greatest_month)
print(lowest_month)

#PRINT the analysis
print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months: {c_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_revenue}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase_profits})")
print(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease_profits})")


#export file

with open("budget_data.txt", 'w') as text:
    text.write("Financial Analysis\n")

    text.write("------------------------------------------------")

    text.write(f"Total Months: {c_months}\n")
    text.write(f"Total: ${net_profit_loss}\n")
    text.write(f"Average Change: ${average_revenue}\n")
    text.write(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase_profits})\n")
    text.write(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease_profits})\n")