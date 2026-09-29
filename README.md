# StyleKart – E-Commerce Analytics

End-to-end data analytics project covering:

Excel → Python → SQL → Power BI → Machine Learning → GenAI

## Business Objective

Analyze sales, customers, products, regions and returns
to identify actionable business insights.

## Dataset

Customers     : 1,000
Products      : 300
Orders        : 5,000
Payments      : 5,000
Returns       : 445
Inventory     : 300

## Tech Stack

Python
Pandas
MySQL
Power BI
Scikit-learn
Gemini / GenAI

## Analytics Workflow

Data Cleaning
↓
EDA
↓
SQL Analysis
↓
Power BI
↓
Machine Learning
↓
GenAI

## Key Results

Total Sales: ₹8.58M
Total Orders: 5,000
Active Customers: 992

## Machine Learning

K-Means customer segmentation using:

- Total Spend
- Order Count
- Average Order Value

## GenAI

Natural-language analytics using Gemini
to convert business questions into SQL queries.

## Dashboard

<img width="1222" height="682" alt="image" src="https://github.com/user-attachments/assets/fe84f013-386f-43cb-8875-c670ad536295" />


## 📁 Project Structure

```text
StyleKart-Capstone/
│
├── Customers.csv
├── Products.csv
├── Orders.csv
├── Payments.csv
├── Returns.csv
├── Inventory.csv
│
├── StyleKart_Capstone_Dataset.xlsx
├── StyleKart_Customer_Segments.xlsx
│
├── EDA.py
├── convert_excel_to_csv.py
│
├── Sql.sql
│
├── app.py
├── genai.py
│
├── bi_dashboard.pbix
│
├── .gitignore
└── README.md
```

### 📂 File Description

| File                               | Description                          |
| ---------------------------------- | ------------------------------------ |
| `Customers.csv`                    | Customer master data                 |
| `Products.csv`                     | Product and category information     |
| `Orders.csv`                       | Order and sales transaction data     |
| `Payments.csv`                     | Payment transaction details          |
| `Returns.csv`                      | Product return information           |
| `Inventory.csv`                    | Product inventory and stock details  |
| `StyleKart_Capstone_Dataset.xlsx`  | Original Excel dataset               |
| `StyleKart_Customer_Segments.xlsx` | Customer segmentation output         |
| `EDA.py`                           | Python exploratory data analysis     |
| `convert_excel_to_csv.py`          | Converts Excel sheets into CSV files |
| `Sql.sql`                          | SQL analysis queries                 |
| `app.py`                           | Application / analytics workflow     |
| `genai.py`                         | Gemini-based GenAI analytics         |
| `bi_dashboard.pbix`                | Power BI dashboard                   |
| `.gitignore`                       | Files excluded from Git tracking     |
| `README.md`                        | Project documentation                |

---

# 🔄 End-to-End Analytics Pipeline

```text
Excel Dataset
      ↓
Data Cleaning & Preparation
      ↓
Python / Pandas
      ↓
Exploratory Data Analysis
      ↓
MySQL / SQL Analytics
      ↓
Power BI Dashboard
      ↓
Machine Learning
      ↓
GenAI Analytics
      ↓
Business Insights
```

---

# 📊 Power BI Dashboard

The Power BI dashboard provides an interactive view of StyleKart's business performance.

### Dashboard Includes

* Total Sales KPI
* Total Orders KPI
* Active Customers KPI
* Returns KPI
* Revenue by Category
* Sales by Region
* Order Amount by Region
* Region slicer
* Category slicer

### Dashboard Preview

Add your dashboard screenshot here:

```markdown
![StyleKart Power BI Dashboard](screenshots/StyleKart_Dashboard.png)
```

---

# 🤖 Machine Learning

Customer segmentation was performed using **K-Means Clustering**.

### Features Used

* Total Spend
* Order Count
* Average Order Value

### Customer Segments

| Segment   | Customers | Segment Description        |
| --------- | --------: | -------------------------- |
| Segment 0 |       480 | Frequent Value Shoppers    |
| Segment 1 |       212 | Occasional Big Spenders    |
| Segment 2 |       300 | Loyal High-Value Customers |

The segmentation helps identify different customer purchasing patterns and supports customer-focused analytics.

---

# 🧠 GenAI Analytics

Gemini was integrated into the project to enable **Natural Language to SQL** analytics.

Users can ask business questions in natural language, and the GenAI workflow generates an SQL query, executes it against the database, and returns the result.

### Workflow

```text
Business Question
       ↓
Gemini / GenAI
       ↓
SQL Query Generation
       ↓
MySQL Database
       ↓
Query Execution
       ↓
Result
       ↓
Business Insight
```

### Example

**Question:**

```text
Which product categories generated the highest revenue?
```

The generated SQL query is executed against the StyleKart database and the result can be validated against the Power BI dashboard.

---

# 🔍 SQL Analytics

MySQL was used to perform business-focused analysis, including:

* Sales analysis
* Category revenue analysis
* Regional performance
* Customer analysis
* Product analysis
* Payment method analysis
* Returns analysis
* Inventory analysis

The SQL queries are available in:

```text
Sql.sql
```

---

# 🐍 Python & EDA

Python and Pandas were used for:

* Data loading
* Data cleaning
* Missing-value analysis
* Duplicate detection
* Data transformation
* Exploratory Data Analysis
* Statistical analysis
* Data visualization

Main analysis file:

```text
EDA.py
```

---

# 💡 Key Business Insights

The project provides insights into:

* Overall sales performance
* Regional revenue contribution
* Product category performance
* Customer purchasing behavior
* Customer value segments
* Product returns
* Inventory availability
* Payment behavior

These insights provide a data-driven view of StyleKart's overall business performance.

---

# 🛠️ Technologies Used

```text
Excel
Python
Pandas
MySQL
SQL
Power BI
DAX
Scikit-learn
Gemini / GenAI
Git
GitHub
```

---

# 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Kavipriya-R24/StyleKart-Capstone.git
```

### 2. Navigate to the project folder

```bash
cd StyleKart-Capstone
```

### 3. Install Python dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn mysql-connector-python google-generativeai
```

### 4. Run the Python analysis

```bash
python EDA.py
```

### 5. SQL Analysis

Open:

```text
Sql.sql
```

in MySQL Workbench and execute the required queries.

### 6. Power BI

Open:

```text
bi_dashboard.pbix
```

using Power BI Desktop.

---

# 🎯 Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis
* Python
* Pandas
* SQL
* MySQL
* Excel
* Power BI
* DAX
* Data Visualization
* Machine Learning
* K-Means Clustering
* GenAI
* Natural Language to SQL
* Business Intelligence
* Git & GitHub

---

# 👩‍💻 Author

**Kavipriya**

**Data Analytics | Python | SQL | Power BI | Machine Learning | GenAI**

---

## ⭐ Project

This project demonstrates an end-to-end approach to transforming raw e-commerce data into **business insights, interactive dashboards, machine-learning segments, and AI-powered analytics**.
