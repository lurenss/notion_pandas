# notion_pandas
A library that transforms notion tables into pandas dataframes by connecting with the notion API

## Installation
1. pip install -r ./requirements.txt
2. Create an integration [here](https://www.notion.so/my-integrations "Title").
3. Save your *token* from the previous page
4. Save the id of your table. the address of your table will be similar to this  https://www.notion.so/1234v=567. You need to save the numbers after the / and before the v
5. On the top left of your table visualization you have tre dots (...) click on that, after click on add connections and search for the integration you have create in point 2 and click confirm
2. Use this library 😎

## Example
```py
from notion_pandas import notion_pandas 
import pandas as pd

npd = notion_pandas("token", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
npd.to_csv('test.csv')

df =  npd.return_pandas()
df.head()
```