import pandas as pd
# Load the dataset from a CSV file
df = pd.read_csv('/content/sample_data/winemag-data-130k-v2.csv')
# Calculate the statistics for each column
# Select only numerical columns for calculations
numerical_df = df.select_dtypes(include=['number'])  # Selects columns with numerical data types
statistics = pd.DataFrame({
'Mean': numerical_df.mean(),  # Calculates mean for numerical columns
'Median': numerical_df.median(),  # Calculates median for numerical columns
'Mode': df.mode().iloc[0],  # Take the first mode in case there are multiple
'Standard Deviation': numerical_df.std(),  # Calculates std for numerical columns
'Variance': numerical_df.var(),  # Calculates variance for numerical columns
'Range': numerical_df.max() - numerical_df.min()  # Calculates range for numerical columns
})
# Set pandas options to display all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Automatically adjust the width of the display
pd.set_option('display.max_colwidth', None)  # Ensure no truncation of column values
# Print the statistics in a tabular format
print(statistics)