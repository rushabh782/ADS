import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('movies.csv')

# 1. Clean 'YEAR' - Extract the year in YYYY format and convert to numeric
df['YEAR'] = df['YEAR'].str.extract('(\d{4})').astype(float)

# 2. Clean 'GENRE' - Remove extra spaces and quotes
df['GENRE'] = df['GENRE'].str.strip().str.replace('"', '').str.replace(' ', ', ')

# 3. Clean 'RATING' - Handle missing values by filling with the mean
df['RATING'] = pd.to_numeric(df['RATING'], errors='coerce')  # Convert to numeric, coercing errors
df['RATING'] = df['RATING'].fillna(df['RATING'].mean())  # Fill missing ratings with the mean

# 4. Clean 'VOTES' - Remove commas and convert to numeric
df['VOTES'] = df['VOTES'].str.replace(',', '').astype(float)  # Remove commas and convert to float
df['VOTES'] = df['VOTES'].fillna(df['VOTES'].mean())  # Fill missing votes with the mean

# 5. Clean 'Gross' - Remove dollar signs, 'M' or 'B' and convert to numeric
def clean_gross(value):
    if isinstance(value, str):
        value = value.replace('$', '').strip()
        if 'M' in value:
            value = float(value.replace('M', '').strip()) * 1_000_000
        elif 'B' in value:
            value = float(value.replace('B', '').strip()) * 1_000_000_000
        else:
            value = float(value)
    return value

df['Gross'] = df['Gross'].apply(clean_gross)
df['Gross'] = df['Gross'].fillna(df['Gross'].mean())

# 6. Clean 'RunTime' - Remove spaces and convert to float
df['RunTime'] = df['RunTime'].astype(str).str.replace(' ', '').astype(float)
df['RunTime'] = df['RunTime'].fillna(df['RunTime'].mean())

# 7. Clean 'STARS' - Remove unwanted characters and extra spaces
df['STARS'] = df['STARS'].str.replace(r'\n|\r', ', ', regex=True)
df['STARS'] = df['STARS'].str.replace('Director:|Stars:', '', regex=True).str.strip()
df['STARS'] = df['STARS'].fillna('Unknown')

# 8. Clean 'ONE-LINE' - Trim extra spaces
df['ONE-LINE'] = df['ONE-LINE'].str.strip()

# 9. Handle missing values in 'GENRE' (optional)
df['GENRE'] = df['GENRE'].fillna('Unknown')

# 10. Save cleaned dataset
print("\nCleaned dataset:\n", df.head())
df.to_csv('cleaned_movies.csv', index=False)
