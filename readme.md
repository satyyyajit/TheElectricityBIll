# Electricity Bill Management System

This project provides a simple command-line based Electricity Bill Management System using Python and CSV files for data storage. It allows you to manage users, handle their electricity bill payments, and view or modify user account information.

## Features

- **Add New User:** Register a new user with name, units, and a unique user ID.
- **Pay Electricity Bill:** Pay for consumed units; updates user balance and remaining units.
- **Check User Details:** Retrieve and display details of a specific user.
- **Delete User:** Remove a user from the system using their User ID.
- **Show Existing Users:** View all current users and their account details.
- **About Project:** Display information about the project and its structure.

## How It Works

The system stores user data in two CSV files:
- `data1.csv`: Main user data file (serial number, name, user ID, units, amount).
- `data2.csv`: Secondary data file (used for display and payment verification).

All user interactions are menu-driven and happen through the terminal.

## Usage

### Prerequisites

- Python 3.x
- `pandas` library

Install dependencies via pip if needed:
```bash
pip install pandas
```

### Running the Project

1. Clone the repository.
2. Ensure `data1.csv` and `data2.csv` are in the project directory.
3. Run the main script:

```bash
python electricity.py
```

4. Follow on-screen prompts to interact with the system.

### Menu Options

```
--------------------------------------------------
 ELECTRICITY BILL MANAGEMENT
--------------------------------------------------

0- ABOUT THE PROJECT
1- ADD A NEW USER
2- PAY THE ELECTRICITY BILL
3- CHECK USER DETAILS
4- DELETE THE USER
5- SHOW EXISTING USERS
6- EXIT THE PROGRAM
```

## Project Structure

- `electricity.py`: Main Python script containing all business logic.
- `data1.csv`, `data2.csv`: CSV files used for storing and displaying user data.

## Example

Here's how adding a new user works:
- Enter serial number, name, and units.
- The script generates a unique User ID and calculates the initial bill.
- User data is saved and can be viewed or updated as needed.

## About

This project is aimed at demonstrating basic file handling and user management in Python using CSV files.

**Thank you for checking out this project!**

---
*Author: satyyyajit*
