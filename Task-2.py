import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("quotes.csv")

print("Initial Dataset Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values before cleaning:")
print(df.isnull().sum())

df['Quote'] = df['Quote'].fillna("No Quote Available")
df['Author'] = df['Author'].fillna("Unknown")
df['Tags'] = df['Tags'].fillna("No Tags")

initial_rows = df.shape[0]
df = df.drop_duplicates()
final_rows = df.shape[0]

print(f"\nDuplicates removed: {initial_rows - final_rows}")

df['Quote'] = df['Quote'].str.replace('“|”', '', regex=True)
df['Quote'] = df['Quote'].str.strip()

df['Author'] = df['Author'].str.strip()

df['Tags'] = df['Tags'].str.lower()
df['Tags'] = df['Tags'].str.replace(" ", "")
df['Tags'] = df['Tags'].str.strip()

df['Quote_clean'] = df['Quote'].str.lower()

author_encoder = LabelEncoder()
df['Author_encoded'] = author_encoder.fit_transform(df['Author'])

df['Tags_list'] = df['Tags'].apply(lambda x: x.split(','))

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFinal Dataset Info:")
print(df.info())

print("\nFirst 5 rows of cleaned dataset:")
print(df.head())

df.to_csv("quotes_cleaned.csv", index=False)

print("\nCleaned dataset saved as 'quotes_cleaned.csv'")
