# Electricity Bill Management System

## Overview

This project is a simple **Electricity Bill Management System** built using **Python** and **CSV** files for storing user data. The system allows users to add new users, pay bills, check user details, delete users, and view existing users. It manages users' electricity consumption and calculates bill amounts based on the number of units consumed.

## Features

1. **Add a New User**: Enter user details like serial number, name, units consumed, and generate a random User ID. The bill amount is calculated based on the number of units consumed (`unit * 15 Rs.`).
   
2. **Pay Electricity Bill**: Pay for consumed units, and the user's balance is updated accordingly.

3. **Check User Details**: Retrieve and display all details of a user based on their serial number.

4. **Delete a User**: Remove a user from the system by their User ID.

5. **Show Existing Users**: Display all the existing users stored in the CSV file.

6. **About the Project**: Displays brief information about the project.

## Project Structure

- **data1.csv**: Stores the complete user data with columns for serial number (`slno`), name, user ID (`uid`), units consumed, and bill amount.
- **data2.csv**: Stores a subset of the data from `data1.csv` with selected columns (e.g., name).

## Installation

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.x**
- **pandas** library: Install using `pip install pandas`

### Steps to Run

1. Clone the repository or download the source code.
2. Make sure `data1.csv` and `data2.csv` exist in the specified directory (`E:/Documents/`).
3. Run the Python script:


