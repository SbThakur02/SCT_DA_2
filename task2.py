import pandas as pd

# Load dataset
df = pd.read_excel("Global_Superstore.xlsx")

# Display first 5 rows
print(df.head())

# Check missing values
print(df.isnull().sum())

# Fill missing values in numeric columns
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Fill missing values in text columns
text_cols = df.select_dtypes(include=["object", "string"]).columns
df[text_cols] = df[text_cols].fillna("Unknown")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

# Save cleaned dataset
df.to_csv("Cleaned_Global_Superstore.csv", index=False)

print("✅ Data Cleaning Completed Successfully!")