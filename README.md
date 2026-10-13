# Task 1: Data Immersion & Wrangling

ApexPlanet Data Analytics Internship

## About
In this task I took the Superstore Sales dataset from Kaggle and cleaned it so it is ready for analysis.

## Dataset
- Source: Kaggle Superstore Sales Dataset (train.csv)
- Original size: 9800 rows and 18 columns
- Cleaned size: 9800 rows and 24 columns

## Folder Structure
- data/raw/ : original train.csv
- data/cleaned/ : cleaned_data.csv (final output)
- scripts/cleaning.py : cleaning script
- data_dictionary.md : meaning of every column

## What I Did
1. Checked the data for missing values, duplicates, wrong formats and outliers.
2. Made column names lowercase with underscores.
3. Checked for duplicate rows (found 0).
4. Converted order_date and ship_date from text to date format.
5. Filled the missing postal code (Burlington, Vermont) and kept postal codes as 5 digit text.
6. Trimmed extra spaces in text columns.
7. Created new columns: order_year, order_month, order_month_name, order_weekday, shipping_days.
8. Flagged 1145 sales outliers using the IQR method (not deleted).

## How to Run
pip install pandas numpy matplotlib
python scripts/cleaning.py

## Tools Used
Python, Pandas, VS Code

## Author
Tannu Prasad