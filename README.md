# Bank Management System

A simple banking management system developed using Python and MySQL. This application allows users to manage bank accounts by providing functionalities such as creating accounts, depositing and withdrawing money, checking balances, and closing accounts.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Setup](#database-setup)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Predefined Data](#predefined-data)

## Features

- **Open a New Account**: Register a new bank account by providing the customer's name, account number, date of birth, address, phone number, and opening balance.
- **Deposit Amount**: Deposit money into an existing account.
- **Withdraw Amount**: Withdraw money from an existing account.
- **Balance Enquiry**: Check the current balance of an existing account.
- **Display Customer Details**: View the details of a specific customer account.
- **Close an Account**: Delete an account and its associated records from the system.

## Technologies Used

- **Python**: For the application logic and database interaction.
- **MySQL**: For database management.
- **MySQL Connector Python**: For connecting Python with MySQL.

## Database Setup

1. **Install MySQL** on your local machine if it's not already installed.
2. **Create the Database** using the SQL script provided below:

```sql
CREATE DATABASE IF NOT EXISTS Bank_Management;

USE Bank_Management;

CREATE TABLE account (
    Customer_Name VARCHAR(50),
    Account_no VARCHAR(20) PRIMARY KEY,
    DOB DATE,
    Address VARCHAR(100),
    Phone_no VARCHAR(15),
    Opening_Balance DECIMAL(10, 2)
);

CREATE TABLE amount (
    Customer_Name VARCHAR(50),
    Acc_no VARCHAR(20) PRIMARY KEY,
    Balance DECIMAL(10, 2)
);

INSERT INTO account (Customer_Name, Account_no, DOB, Address, Phone_no, Opening_Balance) VALUES
('John Doe', 'ACC001', '1985-05-15', '123 Main St', '555-1234', 5000.00),
('Jane Smith', 'ACC002', '1990-08-22', '456 Oak Ave', '555-5678', 3000.00);

INSERT INTO amount (Customer_Name, Acc_no, Balance) VALUES
('John Doe', 'ACC001', 5000.00),
('Jane Smith', 'ACC002', 3000.00);

```

## Getting Started

To get the banking management system up and running, follow these steps:

### Prerequisites
- **Python** (version 3.x)
- **MySQL** installed and running on your machine
- **MySQL Connector Python** (install using `pip install mysql-connector-python`)

### Installation
1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-usernamebank-management-system.git
   ```
   ```bash
   cd bank-management-system 
   ```

2. Install MySQL Connector: Make sure you have the MySQL Connector Python package installed. You can install it using:

   ```bash 
   pip install mysql-connector-python
   ```

3. Run the Application:
    ```bash
    python BankManagement.py
    ```

## How to Use

### Choose a task from the menu:

**1. OPEN NEW ACCOUNT** - to create a new account.

**2. DEPOSIT AMOUNT** - to deposit money into an existing account.

**3. WITHDRAW AMOUNT** - to withdraw money from an existing account.

**4. BALANCE ENQUIRY** - to check the balance of an account.

**5. DISPLAY CUSTOMER DETAILS** - to view the details of a customer.

**6. CLOSE AN ACCOUNT** - to delete an account.
#### Follow the prompts to input the required details.

## Predefined Data

- The system comes with 2 predefined customer accounts for testing purposes. You can interact with these accounts to deposit, withdraw, or view balance details.
