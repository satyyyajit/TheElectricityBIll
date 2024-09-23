import pandas as pd
import sys
import random

# Load data only once
df = pd.read_csv("E:/Documents/data1.csv", index_col="slno")

# Function to fetch the second CSV file
def fetchcsv():
    print(pd.read_csv("E:/Documents/data2.csv", index_col="slno"))

# Function to write DataFrame back to CSV
def writecsv(df, filename="E:/Documents/data1.csv"):
    df.to_csv(filename)
    fetchcsv()

# Main menu display
def menu():
    print("\n" + "." * 50)
    print(" ELECTRICITY BILL MANAGEMENT")
    print("." * 50)
    print("\n0- ABOUT THE PROJECT")
    print("1- ADD A NEW USER")
    print("2- PAY THE ELECTRICITY BILL")
    print("3- CHECK USER DETAILS")
    print("4- DELETE THE USER")
    print("5- SHOW EXISTING USERS")
    print("6- EXIT THE PROGRAM\n")

# Add a new user
def add_newuser():
    global df  # Access global df
    print(df)
    try:
        slno = int(input("ENTER serial no: "))
        name = input("ENTER YOUR NAME: ")
        unit = int(input("ENTER YOUR UNITS: "))
        uid = random.randint(12107, 99999)
        bal = unit * 15.0
        df.loc[slno] = [name, uid, unit, bal]
        writecsv(df)
        print("User added successfully!")
    except Exception as e:
        print(f"Error adding user: {e}")

# Pay the electricity bill
def pay():
    fetchcsv()
    try:
        slno = int(input("Enter Your Serial No.: "))
        amount = int(input("Enter Your Units to pay: "))
        m = amount * 15.0
        print(f'You have to pay {m} Rs.')
        df.loc[slno, 'unit'] -= amount
        df.loc[slno, 'amount'] -= m
        writecsv(df)
        print("Payment updated successfully!")
    except Exception as e:
        print(f"Error processing payment: {e}")

# Check user details
def checkuser():
    fetchcsv()
    try:
        slno = int(input("Enter your Serial no.: "))
        print("\nYour USER DETAILS are given below:\n")
        print(df.loc[slno])
    except Exception as e:
        print(f"Error fetching user details: {e}")

# Delete a user
def deleteuser():
    global df  # Access global df
    try:
        uid = int(input("Enter User ID: "))
        df.set_index("uid", inplace=True)  # Set 'uid' as the index temporarily
        df.drop(uid, inplace=True)
        df.reset_index(inplace=True)  # Reset index back to 'slno'
        writecsv(df)
        print(f"User with ID {uid} has been deleted.")
    except Exception as e:
        print(f"Error deleting user: {e}")

# About the project
def aboutproject():
    print("\nTHIS PROJECT IS ABOUT ELECTRICITY BILL MANAGEMENT WITH CSV FILES AND PYTHON\n")
    print("CSV Files Used: data1.csv and data2.csv")
    print("THANK YOU")

# Main logic
print("LOADING, PLEASE WAIT")
print("WELCOME TO THE ELECTRICITY DEPARTMENT")
X = input("ENTER USERNAME: ")
Y = int(input("ENTER PASSWORD: "))
print(f"HELLO USER {X}")
input("Press Enter To See The Menu")

while True:
    menu()
    try:
        choice = int(input("ENTER YOUR CHOICE: "))
        if choice == 1:
            add_newuser()
        elif choice == 2:
            pay()
        elif choice == 3:
            checkuser()
        elif choice == 4:
            deleteuser()
        elif choice == 5:
            fetchcsv()
        elif choice == 6:
            print("Thank You")
            sys.exit()
        elif choice == 0:
            aboutproject()
        else:
            print("INVALID CHOICE")
    except Exception as e:
        print(f"Error: {e}")
