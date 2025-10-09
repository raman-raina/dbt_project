import pandas as pd
import sqlite3
import numpy as np

csv_file = 'path/to/superstore.csv'
db_file = 'superstore.db'
table_name = 'data'

df = pd.read_csv(csv_file, encoding='latin1')

df1 = df.drop(columns=['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 
                 'Segment', 'Country', 'City', 'State', 
                 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 
                 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'])

unique_values = df1['Customer ID'].unique()
random_values = np.random.randint(18, 60, size=len(unique_values))
value_map = dict(zip(unique_values, random_values))
df1['Age'] = df1['Customer ID'].map(value_map)

conn = sqlite3.connect(db_file)
df.to_sql('orders', conn, if_exists='replace', index=False)
df1.to_sql('customers', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
