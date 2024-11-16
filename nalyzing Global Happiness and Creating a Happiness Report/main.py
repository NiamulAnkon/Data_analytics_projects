import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Create a sample dataset
data = {
    'Country': ['Finland', 'Denmark', 'Switzerland', 'Iceland', 'Netherlands'],
    'Happiness_Score': [7.8, 7.6, 7.5, 7.4, 7.3],
    'GDP_per_Capita': [1.34, 1.36, 1.29, 1.28, 1.30],
    'Social_Support': [1.5, 1.52, 1.49, 1.48, 1.44],
    'Healthy_Life_Expectancy': [72.4, 71.8, 73.1, 72.8, 72.0],
    'Freedom_to_Make_Choices': [0.87, 0.89, 0.86, 0.88, 0.85],
    'Generosity': [0.16, 0.18, 0.17, 0.15, 0.19],
    'Perceptions_of_Corruption': [0.21, 0.23, 0.19, 0.24, 0.22]
}

df = pd.DataFrame(data)
df.head()

print(df.info())
print(df.describe())

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Factors Influencing Happiness")
plt.show()

top_5 = df.sort_values('Happiness_Score', ascending=False)
sns.barplot(data=top_5, x='Happiness_Score', y='Country', palette='viridis')
plt.title('Top 5 Happiest Countries')
plt.xlabel('Happiness Score')
plt.ylabel('Country')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='GDP_per_Capita', y='Happiness_Score', hue='Country', s=100)
plt.title('Happiness Score vs GDP per Capita')
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness Score')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Freedom_to_Make_Choices', y='Country', palette='Spectral')
plt.title('Freedom to Make Choices Across Countries')
plt.show()

for col in df.columns[2:]:
    corr, _ = pearsonr(df['Happiness_Score'], df[col])
    print(f"Correlation between Happiness Score and {col}: {corr:.2f}")

def generate_report(df):
    top_country = df.loc[df['Happiness_Score'].idxmax(), 'Country']
    low_country = df.loc[df['Happiness_Score'].idxmin(), 'Country']
    avg_score = df['Happiness_Score'].mean()

    report = f"""
    Global Happiness Analysis Report:
    --------------------------------
    - The happiest country is {top_country} with a happiness score of {df['Happiness_Score'].max()}.
    - The least happy country is {low_country} with a happiness score of {df['Happiness_Score'].min()}.
    - On average, countries have a happiness score of {avg_score:.2f}.
    - GDP per Capita and Social Support show the strongest correlations with Happiness Score.
    - Generosity and Perceptions of Corruption show weaker correlations with Happiness Score.

    Recommendations:
    - Improving GDP and access to social support systems can significantly enhance overall happiness.
    - Encouraging transparency and reducing corruption are also critical for improving happiness scores.
    """
    print(report)

generate_report(df)

plt.savefig('happiness_score_vs_gdp.png')
df.to_csv('happiness_analysis.csv', index=False)
