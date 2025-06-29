# 🚗 Car Sales Data Analysis App

A Python application for analyzing and visualizing car sales data from the years **2022** and **2023**, using **Pandas** and **Matplotlib**. It provides users with insightful sales trends, rankings, and company growth to support better business decisions.

---

## 🔐 Login Required

- To use the application, you must **log in** with valid credentials.
- The **MySQL database** is located in the `MySql/` folder.
- The application starts from the `main.py` file, which handles database connection and displays the login screen.

---

## 🎯 Purpose

The app is designed to help users:

- Explore and understand **car sales trends**
- Visualize historical sales patterns
- Identify top-performing dealers and car models
- Monitor company growth over time

---

## ⚙️ How It Works

### 1. 📥 Data Loading
Loads car sales data (2022–2023) from CSV files and stores it into a **MySQL** database.

### 2. 🧹 Data Processing
Cleans and prepares the data using **Pandas**:  
- Removes outliers  
- Fixes formatting issues  
- Aggregates and structures data for analysis

### 3. 📊 Data Analysis
Performs **exploratory data analysis**, including:
- Descriptive statistics  
- Trend detection  
- Market behavior insights

### 4. 📈 Data Visualization
Generates charts using **Matplotlib (Pyplot)**:
- Bar charts  
- Line graphs  
- Histograms  
- Growth plots

---

## 🌟 Main Features

- 📅 **Daily Sales Analysis**  
  View sales patterns by day and detect seasonality.

- 🏆 **Top 5 Dealerships**  
  Identify the top five dealerships with the highest number of car sales.

- 🏢 **Top 10 Car Companies**  
  Discover the ten companies with the highest overall sales.

- 📆 **Monthly Sales Volume**  
  Visualize the number of cars sold each month.

- 🚙 **Top 10 Best-Selling Cars**  
  See the most popular car models during the period.

- 📈 **Company Growth Tracking**  
  Analyze the evolution of each car company’s sales over time.

---

## 🧑‍💻 User Interface Overview

### ▶️ App Startup
- Run `main.py` to launch the app.
- Connects to the database and opens the login screen.

### 🔐 Login System
- Enter a **username and password** to gain access.
- If valid, users are directed to the main menu.

### 🧭 Main Menu
- Displays available options based on user role:
  - View daily sales  
  - Top dealerships  
  - Company rankings  
  - Car popularity trends

### 👥 Role-Based Access

- **Users**:
  - View charts and data in the console.
- **Administrators**:
  - Edit/delete users  
  - Manage system accounts  
  - Access full application features

### 📊 Data Visualization
- Users can choose to:
  - View **individual reports**
  - See **all charts and tables**
- Visual output is powered by **Matplotlib**  
- Tabular data is also shown in the **console**

---

## 🛡️ Admin Features

Admins have full control over the system:
- 🧾 Edit or delete users  
- 🔍 View all user details  
- 🔐 Ensure data integrity and account security

---

## 💾 Requirements

- Python 3.8+
- MySQL Server
- Libraries:
  - pandas  
  - matplotlib  
  - mysql-connector-python (or SQLAlchemy)
    
 ---

## 📂 Folder Structure

```
📁 CarSalesApp/
├── MySql/              # Database scripts and schema
├── main.py             # Entry point of the application
├── data/               # Raw CSV data files
├── modules/            # Application logic (login, analysis, UI)
├── charts/             # Chart generation utilities
└── README.md
```


