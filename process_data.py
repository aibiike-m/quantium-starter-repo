import pandas as pd
import os

data_dir = 'data/'
output_file = 'processed_data.csv'

dataframes = []

for filename in os.listdir(data_dir):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(data_dir, filename))
        df = df[df["product"] == "pink morsel"]
        
        df['price'] = df['price'].str.replace(r'[/$,]', '', regex=True).astype(float)

        df['sales'] = df['price'] * df['quantity']

        df = df[['sales', 'date', 'region']]

        dataframes.append(df)

result_df = pd.concat(dataframes, ignore_index=True)
result_df.to_csv(output_file, index=False)
