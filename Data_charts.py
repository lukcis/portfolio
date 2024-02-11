import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Total Investment by Continent and Year

path_file = "E:\\Programowanie\\Projekty\\pliki_uzyte_do_projektow\\"

countries = pd.read_csv(path_file + "countries.csv")
economies = pd.read_csv(path_file + "economies.csv")

countries_df = pd.DataFrame(data=countries)
economies_df = pd.DataFrame(data=economies)

countries_economies_merge = countries_df.merge(economies_df, on='code', how='left')

plt.figure(figsize=(10, 5))
sns.barplot(data=countries_economies_merge, x='continent', y='total_investment', hue='year')
plt.xlabel("Continent")
plt.ylabel("Total Investment $")
plt.title("Total Investment by Continent and Year")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# Sum of Profit by Year

coffee_data = pd.read_csv("E:\\Programowanie\\Coffee Chain.csv")

coffee_data_df = pd.DataFrame(data=coffee_data)

coffee_data_df['Ddate_date_type'] = pd.to_datetime(coffee_data_df.Ddate, format='mixed')
coffee_data_coffee_x_years = coffee_data_df.groupby(coffee_data_df.Ddate_date_type.dt.year)[['Profit']].sum()
sns.barplot(data=coffee_data_coffee_x_years, y='Profit', x='Ddate_date_type')
plt.xticks(rotation=70)
plt.xlabel("Ddate_date_type")
plt.ylabel("Profit $")

plt.show()


# Imports and Exports by Continent

countries_economies_merge_imports = countries_economies_merge.groupby('continent')['imports'].sum()
countries_economies_merge_exports = countries_economies_merge.groupby('continent')['exports'].sum()

x = np.arange(len(countries_economies_merge_imports))

width = 0.35
plt.bar(x - width/2, countries_economies_merge_imports, width, label='Imports', color='blue')
plt.bar(x + width/2, countries_economies_merge_exports, width, label='Exports', color='red')

plt.xlabel('Continent')
plt.ylabel('Value')
plt.title('Imports and Exports by Continent')
plt.xticks(x, countries_economies_merge_imports.index)
plt.legend()
plt.xticks(rotation=45)

plt.show()