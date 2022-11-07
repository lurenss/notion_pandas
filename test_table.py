from NotionPandas import NotionPandas 
import pandas as pd

token = "insert_your_secret_token"
id_table = "insert_your_table_id" 

npd = NotionPandas(token, id_table)
npd.to_csv('test.csv')
df = npd.return_pandas(print_json=False)

print(df.head())