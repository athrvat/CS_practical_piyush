import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'Rollno': [1, 2, 3, 4, 5],
    'Name': ['Aatish Verma', 'Manisha Singh', 'Tushaar Jain', 'Siddhartha', 'Kushal Vinod'],
    'UT1': [24, 18, 20, 22, 15],
    'UT2': [24, 17, 22, 20, 20],
    'UT3': [20, 19, 18, 24, 18],
    'UT4': [22, 22, 24, 20, 22]
})

# (i) Print top two rows
print(df.head(2))

# (ii) Print last two rows
print(df.tail(2))

# (iii) Add one more column 'Total'
df['Total'] = df['UT1'] + df['UT2'] + df['UT3'] + df['UT4']

# (iv) Display rows where Rollno is 4
print(df[df['Rollno'] == 4])

# (v) Display column labels
print(df.columns)
