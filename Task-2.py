import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np

df = pd.read_csv("Level-1/hockey_teams.csv")

df = df.replace('', np.nan)
df = df.fillna(method='ffill')

num_cols = ['Wins', 'Losses', 'OT Losses', 'Win %', 'GF', 'GA', 'Diff']
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

Q1 = df['GF'].quantile(0.25)
Q3 = df['GF'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['GF'] < (Q1 - 1.5 * IQR)) | (df['GF'] > (Q3 + 1.5 * IQR)))]

le = LabelEncoder()
df['Team_Code'] = le.fit_transform(df['Team Name'])

scaler = StandardScaler()
df[['Wins_Scaled', 'GF_Scaled', 'GA_Scaled']] = scaler.fit_transform(df[['Wins', 'GF', 'GA']])

df.to_csv("Level-1/hockey_cleaned.csv", index=False)
print("Data cleaning, outlier removal, and standardization complete.")