# functions.py
import pandas as pd
import os

def verify_user(ic_number, password):
    """
    Verify the user's credentials by checking if the IC number is 12 digits long
    and if the password matches the last 4 digits of the IC number.
    """
    if len(ic_number) == 12 and password == ic_number[-4:]:
        return True
    return False

def calculate_tax(income, tax_relief):
    """
    Calculate the tax payable based on the Malaysian tax rates for the current year.
    This is a simplified version and may not reflect the actual tax calculation rules.
    """
    taxable_income = income - tax_relief
    tax_payable = 0

    if taxable_income <= 5000:
        tax_payable = 0
    elif taxable_income <= 20000:
        tax_payable = (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        tax_payable = 150 + (taxable_income - 20000) * 0.03
    elif taxable_income <= 50000:
        tax_payable = 600 + (taxable_income - 35000) * 0.08
    elif taxable_income <= 70000:
        tax_payable = 1800 + (taxable_income - 50000) * 0.14
    elif taxable_income <= 100000:
        tax_payable = 4600 + (taxable_income - 70000) * 0.21
    else:
        tax_payable = 10900 + (taxable_income - 100000) * 0.24

    return tax_payable

def save_to_csv(data, filename):
    """
    Save the user's data (IC number, income, tax relief, and tax payable) to a CSV file.
    If the file doesn't exist, create a new file with a header row. If the file exists,
    append the new data to the existing file.
    """
    columns = ["IC Number", "Income", "Tax Relief", "Tax Payable"]
    df = pd.DataFrame([data], columns=columns)

    if not os.path.isfile(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)

def read_from_csv(filename):
    """
    Read data from the CSV file and return a pandas DataFrame containing the data.
    If the file doesn't exist, return None.
    """
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    return None
