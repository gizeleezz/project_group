from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd() / "Cash_on_Hand.csv"

# Open CSV file    
csv_folder_path=Path.cwd()/ "csv_reports"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

 # create an empty lists to store the values for all 90 days
    cash_on_hand = []

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        cash_on_hand.append([row[0], float(row[1])])

is_increasing=True
cash_deficits = []

previous_cash = cash_on_hand[0][1]  # Cash-on-Hand on the first day
highest_increment = 0  # Initialize the highest increment to 0

for day, cash in cash_on_hand[1:]:  # Starting from the second day
    if cash > previous_cash:
        increment = cash - previous_cash
        if increment > highest_increment:
            highest_increment = increment
    
    else:
          is_increasing = False
    deficit = previous_cash - cash  
    cash_deficits.append([day, deficit])
    previous_cash = cash

# Print the cash deficits and the days of cash deficits
if is_increasing:
    print("Cash on each day is higher than the previous day.")
    print(f"Highest Increment: USD{round(highest_increment, 2)}")
else:
    print("Cash-on-Hand is not always increasing.")
    print("Cash Deficits:")
    for day, deficit in cash_deficits:
        deficit_rounded = round(deficit, 2)
        print(f"Day {day}, Cash Deficit AMOUNT: USD{deficit_rounded}")