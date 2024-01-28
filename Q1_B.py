import matplotlib.pyplot as plt

# Given result data
data = {'Maths': [100, 95, 85],
        'Science': [100, 100, 100],
        'SST': [60, 57, 53]}
names = ['Aarya', 'Manit', 'Sanvi']

# Creating a DataFrame
df = pd.DataFrame(data, index=names)

# Plotting the bar chart
ax = df.plot(kind='bar', figsize=(8, 6))

# Adding title and labels
ax.set_title('Result Analysis')
ax.set_xlabel('Name')
ax.set_ylabel('Score')

# Displaying legends
ax.legend(title='Subjects')

# Displaying the bar chart
plt.show()
