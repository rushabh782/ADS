import pandas as pd

df = pd.read_csv('/content/sample_data/adult.csv')

print("Original Data:")
print(df.head())

# Steps for data cleaning 
# Step 1: Handle the missing values
df.replace('?',pd.NA,inplace=True)

#Drop rows with missing values
df.dropna(inplace=True)

#Srep 2 - Removing duplicate values
df.drop_duplicates(inplace=True)

#Step 3 - Correcting data types
#convert income to category
df['income']= df['income'].astype('category')

#convert education.num to integer
df['education.num'] = df['education.num'].astype(int)

#Step 4 Renaming columns for consistency
df.rename(columns={
    'education.num':'education_num',
    'marital.status':'marital_status',
    'workclass':'work_class',
    'capital.gain':'capital_gain',
},inplace=True)


print('Cleaned Data:')
print(df.head())

#Save to csv
df.to_csv('cleaned_adult_data.csv',index=False)
