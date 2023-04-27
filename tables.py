import pandas as pd
import csv 

csv_file = open('Anchor_fire_retardant_marine_tables.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Properties','Technical Data'])

# Webpage url                                                                                                               
url = 'https://anchorplywood.com/ProductDescription.aspx?ProductId=1020'

# Extract tables
dfs = pd.read_html(url)


# Get first table                                                                                                           
df = dfs[0]
df1 = dfs[1]
pd.set_option('max_colwidth', 400)
print(df)
print(df1)

# df.to_csv('python.csv')
# df1.to_csv('python.csv')
csv_writer.writerow([df,df1])

# Extract columns                                                                                                           
# df2 = df[['Test Prescribed in IS: 2202 (Part-I), 1999','Minimum Value for Conformity','Observed Value']]
# print(df2)