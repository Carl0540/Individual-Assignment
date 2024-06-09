# main.py
import functions as fn
import pandas as pd

def register_user():
    while True:
        ic_number = input("Enter your 12-digit IC number: ")
        password = input("Enter the last 4 digits of your IC number as the password: ")
        
        if fn.verify_user(ic_number, password):
            print("Registration successful!")
            return ic_number, password
        else:
            print("Invalid IC number or password. Please try again.")

def authenticate_user(ic_number, password):
    while True:
        entered_ic = input("Enter your 12-digit IC number: ")
        entered_password = input("Enter the last 4 digits of your IC number as the password: ")
        
        if entered_ic == ic_number and fn.verify_user(entered_ic, entered_password):
            print("Authentication successful!")
            return True
        else:
            print("Invalid credentials. Please try again.")

def main():
    filename = "tax_records.csv"
    
    if fn.read_from_csv(filename) is None:
        print("No registered users. Please register first.")
        ic_number, password = register_user()
    else:
        print("Existing user detected. Please authenticate.")
        ic_number, password = register_user()  # In this example, we prompt registration for demonstration purposes
    
    if authenticate_user(ic_number, password):
        annual_income = float(input("Enter your annual income: "))
        tax_relief = float(input("Enter your tax relief amount: "))
        
        tax_payable = fn.calculate_tax(annual_income, tax_relief)
        print(f"Your calculated tax payable is: RM {tax_payable:.2f}")
        
        user_data = [ic_number, annual_income, tax_relief, tax_payable]
        fn.save_to_csv(user_data, filename)
        
        print("Your data has been saved.")
        
        df = fn.read_from_csv(filename)
        if df is not None:
            print("\nCurrent Tax Records:")
            print(df)

if __name__ == "__main__":
    main()
