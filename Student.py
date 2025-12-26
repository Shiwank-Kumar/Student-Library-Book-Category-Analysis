import pandas as pd
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Category': ['Management', 'Economics', 'Computer Science', 'Literature', 'Science', 'Law'],
    'Books_Issued': [120, 95, 150, 80, 110, 60]
}

df = pd.DataFrame(data)

# ----- Bar Chart -----
plt.figure()
plt.bar(df['Category'], df['Books_Issued'])
plt.xlabel('Book Category')
plt.ylabel('Number of Books Issued')
plt.title('Category-wise Book Usage in Library')
plt.show()

# ----- Pie Chart -----
plt.figure()
plt.pie(df['Books_Issued'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
plt.title('Percentage Share of Book Usage by Category')
plt.show()
