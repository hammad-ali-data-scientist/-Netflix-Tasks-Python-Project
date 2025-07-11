import pandas as pd
df = pd.read_csv('netflix2.csv')
print(df.head())
print(df.isnull().sum())

#*** fill missing values with specific values(e.g unknown)*******
df_cleaned = df.dropna()
print(df_cleaned)
df['director'].fillna('Unknown', inplace=True)
print(df['director'])

# ***** fill missing values *****

df['duration'] = df['duration'].fillna(df['duration'].median())
print(df['duration'])
df['duration'] = df['duration'].apply(lambda x:str(x)+' mins')
print(df['duration'])


df = pd.read_csv('netflix3.csv')
print(df.head())
df['duration'] = df['duration'].str.replace(' mins', '').astype(float)
print(df['duration'])
mean = df['duration'].mean()
df['duration'] = df['duration'].apply(lambda x : mean if x > mean else x)
print(f"Mean : {mean}")
print(df['duration'])
df['duration'] = df['duration'].fillna(df['duration'].mean())
print(df['duration'])
print(df.duplicated().sum())
df['title'] = df['title'].str.lower()
print(df['title'])

# ******* standardize date format*******

df['date_added'] = pd.to_datetime(df['date_added'])
print(df['date_added'])

# *******standardize categorical data*******
df['rating'] = df['rating'].str.upper()
df.dropna(inplace=True)
print(df)

# #******Correct error and inconsistencies********
df['country'] = df['country'].replace({'Usa':'USA', 'United States':'USA'})
print(df['country'])
df['country'] = df['country'].replace({'Pakistan':'USA'})
df.to_excel('final.xlsx', sheet_name='sheet1', index=False)