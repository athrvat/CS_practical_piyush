import pandas as pd

# Creating the DataFrame 'df'
data = {'Maths': [99, 98, 82],
        'Science': [100, 52, 91],
        'SST': [65, 57, 53]}
index = ['Aarya', 'Manit', 'Sanvi']
df = pd.DataFrame(data, index=index)

# Adding one column 'Total'
df['Total'] = df['Maths'] + df['Science'] + df['SST']

# Adding one row 'R4' with values 77, 93, 59
df.loc['R4'] = [77, 93, 59, 0]

# Printing scores of Maths and Science only
print(df[['Maths', 'Science']])

# Updating marks of Science of Sanvi to 82
df.at['Sanvi', 'Science'] = 82

# Deleting the row 'Sanvi'
df = df.drop('Sanvi')

# Displaying the modified DataFrame 'df'
print(df)
