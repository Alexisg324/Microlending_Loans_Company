# import CSV files (path) frompathlib using following code: 
import csv
from pathlib import Path

loan_costs = [500, 600, 200, 1000, 450]

# Calculate and print the amount of numbers in this "loan_costs" list:
number_of_loans_from_list = len(loan_costs)
print(f"This company provides {number_of_loans_from_list} different loan options.")

# Add all numbers in list together using following code:
total_value_of_loans = sum(loan_costs)
print(f"The sum amount of all loans provided by this company is ${total_value_of_loans} .")

# Calculate average loan amount using "sum" and "len".  Remember, average is the sum of all numbers divided by the number of  items.
average_loan_amount = sum(loan_costs) / len(loan_costs)
print(f"The average amount of all loans provided by this company is {average_loan_amount}.")

"""Part 2: Analyze Loan Data"""

# Calculate the present value of the loan by using present value equation: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Extract Future Value and Remaing Months from dictionary values by using get() 
x = loan.get("future_value")
print(f"Future value is {x}.")

y = loan.get("remaining_months")
print(f"There are {y} months remaining.")

# Calculate "fair value" by using the "Present value" formula: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
present_value = x / (1 + 0.20/12) ** y
print(f"The present value is ${present_value: .2f}.")

# Using a conditional statement, determine if it makes sense to buy the loan at it's current price.  Is it worth the buy, yes or no? 
present_value = 861.77
loan_price = 500

if present_value >= 500:
    print("This loan is worth the investment!  The loan is worth more than the cost to buy it.")

else: 
    print("Don't even bother!  This loan is too epensive and not worth the price.")


"""Part 3: Perform Financial Calculations"""

# Calculate present value for the loan based on the data 
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate the present value of this loan. Makre sure to return the present_value and use parameters given. 
def present_loan_value():
    future_value = 1000
    remaining_months = 12
    annual_discount_rate = 0.20
    present_value =  present_value =  1000 / (1 + 0.20 / 12) ** 12
    return present_value    

present_loan_value = present_value
print(f"The present loan value is ${present_loan_value: .2f}")

# Based on the loan infortmation, calculare present value.  Use 20% (0.20) for the annual_discount_rate.
present_value =  1000 / (1 + 0.20 / 12) ** 12
print(f"The present value of the loan is: ${present_value: .2f}")


"""Part 4: Conditionally filter lists of loans"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list "[]" of inexpensive loans:
inexpensive_loans = []

# Make a loop through all the loans and append the loans that are less than or equal to $500 to the inexpensive_loans list.  
loans = [200, 500, 700, 900]
inexpensive_loans = loans[0:2]


# Print your list of inexpensive loans
for num in loans:
    print(inexpensive_loans)


"""Part 5: Save the results."""

# Set the output header using "loan price, repayment intervals, future values, and remaining months".
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path with "inexpensive loans".
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row names provided
# use loan values from inexpensive loans list 
csvpath = Path("inexpensive_loans.csv")
counter = 0
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        
        counter = counter + 1

        print("row counter", counter)
        print(row)

#Workcited: UCB-Coding-Bootcamp (2021-2022).  Module 1. UC Berkeley Fintech Extension.  https://courses.bootcampspot.com/
