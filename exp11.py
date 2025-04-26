import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')

# 1. Grouped Bar Plot
plt.figure(figsize=(8,6))
sns.barplot(x='species',y='sepal_length',hue='species',data=df)
plt.title('Grouped Bar Plot')
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(8,6))
sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=df)
plt.title('Scatter Plot')
plt.show()

# 3. Bubble Chart
plt.figure(figsize=(8,6))
sns.scatterplot(x='sepal_width', y='petal_width', size='sepal_length', hue='species', data=df, sizes=(20, 200))
plt.title('Bubble Chart - Sepal Width vs Petal Width (Size by Sepal Length)')
plt.legend(bbox_to_anchor=(1, 1))
plt.show()

# 4. Heat Map
plt.figure(figsize=(8,6))
# Select only numerical features for correlation calculation
numerical_df = df.select_dtypes(include=['number'])  
correlation = numerical_df.corr()  # Calculate correlation on numerical data
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Heat Map - Correlation Matrix')
plt.show()

# 5. Run Chart (Line plot over index)
plt.figure(figsize=(8,6))
plt.plot(df.index, df['sepal_length'], marker='o', linestyle='-')
plt.title('Run Chart - Sepal Length over Observations')
plt.xlabel('Observation')
plt.ylabel('Sepal Length')
plt.show()

# 6. Multivariate Chart (Pair Plot)
sns.pairplot(df, hue='species')
plt.suptitle('Multivariate Chart - Pair Plot', y=1.02)
plt.show()