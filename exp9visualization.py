import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
df = pd.read_csv('/content/sample_data/Iris.csv')

# 1. Numerical / Quantitative - Histogram for petal length
plt.figure(figsize=(5, 4))
sns.histplot(df['PetalLengthCm'], bins=15, color='orange', kde=True)
plt.title("Petal Length Distribution (Quantitative)")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 2. Categorical / Qualitative - Countplot for species
plt.figure(figsize=(5, 4))
sns.countplot(x='Species', data=df, palette='Set3')
plt.title("Count of Each Iris Species (Qualitative)")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()

# 3. Quantitative vs Categorical - Boxplot of Sepal Width by Species
plt.figure(figsize=(6, 4))
sns.boxplot(x='Species', y='SepalWidthCm', data=df, palette='pastel')
plt.title("Sepal Width by Species (Quantitative vs Categorical)")
plt.xlabel("Species")
plt.ylabel("Sepal Width (cm)")
plt.show()

# 4. Pairplot to show relationships between all numerical variables
sns.pairplot(df, hue='Species', palette='husl')
plt.suptitle("Pairwise Relationships (Quantitative & Categorical)", y=1.02)
plt.show()
