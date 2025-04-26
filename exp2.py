import pandas as pd

df = pd.read_csv('/content/sample_data/winemag-data-130k-v2.csv')

#convert first to numerical cols to calculate Measures of variation and then calculate statistics
numerical_df = df.select_dtypes(include=['number'])

statistics= pd.DataFrame({
    'Range':numerical_df.max() - numerical_df.min(),
    'IQR':numerical_df.quantile(0.75) - numerical_df.quantile(0.25),
    'Standard Deviation': numerical_df.std(),
    'Variance':numerical_df.var(),
    'C.V': (numerical_df.std()/numerical_df.mean())*100,
})

#print all rows and columns
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)

print(statistics)
