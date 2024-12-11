import pandas as pd
#№2#
df = pd.read_csv('random\Mall_Customers.csv')
a = df[df['Genre'] == 'Female']
a_income = sum(a['Annual Income (k$)'])/len(a)
print(a_income)
#№3#
df = pd.read_csv('random\Mall_Customers.csv')
a = df[df['Genre'] == 'Female']
a_max = a['CustomerID'].where(a['Annual Income (k$)'] == max(a['Annual Income (k$)'])).dropna()
print(a_max.index)
b = df[df['Genre'] == 'Male']
b_max = b['CustomerID'].where(b['Annual Income (k$)'] == max(b['Annual Income (k$)'])).dropna()
print(b_max.index)
#№4#
import matplotlib.pyplot as plt
df = pd.read_csv('random\Mall_Customers.csv')
b = df[df['Genre'] == 'Male']
data = b.groupby('Age')['Annual Income (k$)'].mean()
plt.plot(data)
plt.show()
#№5#
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 6))
df = pd.read_csv('random\Mall_Customers.csv')
b = df[df['Genre'] == 'Male']
a = df[df['Genre'] == 'Female']
data_b = b.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()
data_a = a.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()
data_b.plot.bar(color='blue')
data_a.plot.bar(color='pink')
plt.show()