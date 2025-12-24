import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("Level-1/plots", exist_ok=True)
df = pd.read_csv("Level-1/hockey_cleaned.csv")

stats = df.describe()
print("--- Summary Statistics ---\n", stats)

plt.figure(figsize=(8, 5))
sns.histplot(df['Wins'], bins=10, kde=True, color='skyblue')
plt.title("Distribution of Wins")
plt.savefig("Level-1/plots/wins_hist.png")

plt.figure(figsize=(8, 5))
sns.scatterplot(x='GF', y='Wins', data=df, hue='Win %', palette='viridis')
plt.title("Wins vs. Goals For (GF)")
plt.savefig("Level-1/plots/wins_vs_gf_scatter.png")

plt.figure(figsize=(8, 5))
sns.boxplot(x=df['GA'], color='salmon')
plt.title("Box Plot of Goals Against (GA)")
plt.savefig("Level-1/plots/ga_boxplot.png")

plt.figure(figsize=(10, 8))
corr = df[['Wins', 'Losses', 'Win %', 'GF', 'GA', 'Diff']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Performance Metrics")
plt.savefig("Level-1/plots/correlation_matrix.png")

with open("Level-1/EDA_Report.txt", "w") as f:
    f.write("EDA INSIGHT REPORT\n")
    f.write("==================\n")
    f.write(f"Total teams analyzed: {len(df)}\n")
    f.write(f"Average Wins: {df['Wins'].mean():.2f}\n")
    f.write(f"Highest Correlation: Wins vs Win % ({corr.loc['Wins', 'Win %']:.2f})\n")
    f.write("Findings: Goals For (GF) shows a positive correlation with Wins, while Goals Against (GA) shows a negative impact.")

print("EDA complete. Plots and report generated in 'Level-1' folder.")