# Investment and Bond Repayment Calculator

A Python calculator that allows a client to calculate their investment earnings and bond repayment amounts.

## Description

This program is for a financial company that allows a client to calculate their interest on an investment or calculate the amount that should be repaid on a home loan each month.

The investment calculator allows the client to:

* Calculate the Simple interest given the interest rate, principal amount and time period.
* Calculate the Compound interest given the interest rate, accumulated amount and the time period.

The bond repayment calculator allows the client to:

* Calculate the monthly bond repayments given the property value, interest rate and payment period.

## Functionality summary

* Calculates investment earnings
* Calculates bond repayments

## Programming principles

This program employs the fundamental programming principles of Python variables and control structures.

## Dependencies

    import math

## Running the program

Run the inventory.py file in any Python IDE.

## Code preview

```python 
# when investment entered
if (calculator == "investment"):
    deposit = float(input("How much money are you depositing in £?\n"))
    interest_rate = float(input("What is the interest rate (as a percentage)?\n"))
    years = int(input("How many years?\n"))

    # using indented if statement for interest type
    interest = input("Do you want 'simple' or 'compound' interest?\n").lower()
    if interest == "simple":
        # calculate using simple interest rate forumula to 2 decimal places
        # simple interest = deposit * (1 + (interest rate / 100) * years)
        # divide interest rate by 100 to get a decimal
        interest = round(deposit * ((1 + ((interest_rate / 100) * years))), 2)

        print(f"After {years} years your total investment will be £{interest}.")
```

## Program preview

```
Choose either 'investment' or 'bond' from the menu below to proceed:

investment      -       to calculate the amount of interest you'll earn on your investment

bond            -       to calculate the amount you'll have to pay on a home loan

bond
What is the value of the house in £?
100000
What is the interest rate (as a percentage)?
4
The number of months they plan to take to repay the bond?
108
You will have to pay £1104.1 each month over 108 months.
```

## Author  

Manjeet Dhiman
