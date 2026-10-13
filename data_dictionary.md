# Data Dictionary

Dataset: Superstore Sales (train.csv) from Kaggle
Rows: 9800, Columns: 18 (24 after cleaning)

## Original columns

| Column | Type | What it means | Why it matters |
|---|---|---|---|
| row_id | int | Row number of the record | Just for identifying rows |
| order_id | text | ID of the order | One order can have many products |
| order_date | date | When the order was placed | To see sales by month/year |
| ship_date | date | When the order was shipped | To check delivery time |
| ship_mode | text | How the order was shipped | Compare shipping types |
| customer_id | text | ID of the customer | To find repeat customers |
| customer_name | text | Name of the customer | Customer reports |
| segment | text | Consumer, Corporate or Home Office | Sales by customer type |
| country | text | Country | Only United States here |
| city | text | City | Sales by city |
| state | text | State | Sales by state |
| postal_code | text | Postal code | Location analysis |
| region | text | East, West, Central or South | Sales by region |
| product_id | text | ID of the product | Identify products |
| category | text | Furniture, Office Supplies or Technology | Which category sells most |
| sub_category | text | Smaller group inside category | More detailed product analysis |
| product_name | text | Name of the product | Find top products |
| sales | float | Sale amount in dollars | Main number for revenue |

## Columns I added

| Column | Type | What it means | Why it matters |
|---|---|---|---|
| order_year | int | Year of the order | Compare year to year |
| order_month | int | Month number of the order | Monthly trend |
| order_month_name | text | Month name | Easy to read in charts |
| order_weekday | text | Day of the week | See which days have more orders |
| shipping_days | int | Days between order and shipping | Delivery speed |
| sales_outlier | True/False | True if the sale is unusually high or low | Spot very big orders |

## Problems found in the data and what I did

1. Column names had spaces and capital letters, so I made them lowercase with underscores.
2. Dates were stored as text (dd/mm/yyyy), so I converted them to date format.
3. Postal code was missing for some rows (Burlington, Vermont). I filled it with 05401.
4. Postal codes were numbers so the leading zero was lost. I changed them to 5 digit text.
5. Some text columns had extra spaces, so I trimmed them.
6. Duplicate rows: checked, found none (0).
7. Outliers in sales: found 1145 rows using the IQR method. I did not delete them, I only marked them in the sales_outlier column.