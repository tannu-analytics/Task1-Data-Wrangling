import pandas as pd

df = pd.read_csv("data/raw/train.csv")
print("Original shape:", df.shape)

# 1. Column names standard karna
df.columns = (df.columns.str.strip().str.lower()
              .str.replace(" ", "_").str.replace("-", "_"))

# 2. Duplicates hatana
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# 3. Dates ko proper format mein badalna
df["order_date"] = pd.to_datetime(df["order_date"], format="%d/%m/%Y", errors="coerce")
df["ship_date"] = pd.to_datetime(df["ship_date"], format="%d/%m/%Y", errors="coerce")

# 4. Missing postal code
mask = (df["city"] == "Burlington") & (df["state"] == "Vermont") & df["postal_code"].isnull()
df.loc[mask, "postal_code"] = 5401
df["postal_code"] = df["postal_code"].fillna(0).astype(int).astype(str).str.zfill(5)

# 5. Text columns saaf karna
for col in ["customer_name", "city", "state", "product_name"]:
    df[col] = df[col].str.strip()

# 6. Feature engineering
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["order_month_name"] = df["order_date"].dt.month_name()
df["order_weekday"] = df["order_date"].dt.day_name()
df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days

# 7. Outliers ko flag karna (hatana nahi)
q1, q3 = df["sales"].quantile([0.25, 0.75])
iqr = q3 - q1
df["sales_outlier"] = (df["sales"] < q1 - 1.5 * iqr) | (df["sales"] > q3 + 1.5 * iqr)
print("Outliers:", df["sales_outlier"].sum())

# 8. Validation
print("Ship date order date se pehle:", (df["shipping_days"] < 0).sum())
print("Missing values:\n", df.isnull().sum())

df.to_csv("data/cleaned/cleaned_data.csv", index=False)
print("Final shape:", df.shape, "- saved!")