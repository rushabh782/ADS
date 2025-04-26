import pandas as pd

df = pd.read_csv('/content/sample_data/winemag-data-130k-v2.csv')

# select numerical cols for calculation.calculate statistics of each column
numerical_df = df.select_dtypes(include=['number'])
statistics = pd.DataFrame({
    'Mean':numerical_df.mean(),
    'Mode':numerical_df.mode().iloc[0],
    'Median':numerical_df.median(),
    'Standard Deviation':numerical_df.std(),
    'Variance':numerical_df.var(),
    'Range':numerical_df.max()-numerical_df.min(),
    'Q1':numerical_df.quantile(0.25),
    'Q3':numerical_df.quantile(0.75),
    '10 Percentile':numerical_df.quantile(0.10),
    '90 Percentile':numerical_df.quantile(0.90),
})

#Display all rows and columns
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)

print(statistics)

