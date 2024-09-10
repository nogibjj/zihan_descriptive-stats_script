import pandas as pd  # imports pandas and calls the imported version 'pd'
import matplotlib.pyplot as plt  # imports the package and calls it 'plt'
import seaborn as sns  # imports the seaborn package with the imported name 'sns'

# get a rough view of what the data looks like - the list of all the world's billionaires from 2021
df = pd.read_csv("Billionaire_2021.csv")
print(df.head())

# get to know how many observations and variables in the dataset
print(df.shape)

# get the count of billionaires from each country
country_count = df.Country.value_counts()
print(country_count)

# get the descriptive statistics
print(f'Mean is {country_count.mean()}')
print(f'Median is {country_count.median()}')
print(f'Standard deviation is {country_count.std()}')

# Create a bar plot of where billionaires are from
plt.figure(figsize=(15, 12))
plt.bar(country_count.index, country_count)
plt.title("Where Are Billionaires From (2021)")
plt.xlabel("Country")
plt.ylabel("Number of Millionaires")
plt.xticks(rotation=90)                             ## rotate the x-label to make it visible
plt.show()                                          ## for some reason, plt.show() don't work in the codespace but you won't have this problem when doing it locally
plt.savefig('Where Are Billionaires From (2021)')   ## generate and save the picture