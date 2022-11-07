import os
from notion_client import Client
import pandas as pd 
import json 

#definition object notion_pandas
class NotionPandas:
    def __init__(self, authh, database_idd):  
        try:
            self.notion =  Client(auth=authh)
            self.my_page = self.notion.databases.query(database_id=database_idd)
            
        except:
            print('Please check your auth and database_id')

    def change_user(self, auth):
            try:
                self.notion = Client(auth)
            
            except:
                print('Please check your auth')
    
    def change_database(self, database_id):
        try:
            self.my_page = self.notion.databases.query(database_id)
        except:
            print('Please check your database_id')
    
    def return_pandas(self, print_json = False):
        data = self.my_page['results']
        #save my_page to json file
        with open('./result.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)

        # Show page json structure
        if print_json:
          self.show_json()

        df = pd.read_json('./result.json')  

        df.properties.to_json('./result.json', orient='records', force_ascii=False)
        df = pd.read_json('./result.json')
        col = df.columns  
        
        for c in col:
            type = dict(df[c][0])['type']
            if type == 'checkbox' or type == 'number':
                df[c] = df[c].apply(lambda x: dict(x)[type])
            
            elif type == 'date':
                df[c] = df[c].apply(lambda x: dict(dict(x)[type])['start'])
            
            elif type == 'status':
                df[c] = df[c].apply(lambda x: dict(dict(x)[type])['name'])
            
            elif type == 'title':
                df[c] = df[c].apply(lambda x: dict(list(dict(x)[type])[0])['text']['content'])
            
            elif type == 'multi_select':
                col_dict = []
                for i in range(len(df[c])):
                  multi = df[c][i][type]
                  multi_dict = []
                  for j in range(len(multi)):
                    multi_dict.append(multi[j]['name'])
                  col_dict.append(multi_dict)
                df[c]=col_dict
                df[c] = df[c].agg(', '.join) #remove list square brackets
            
            elif type == 'rich_text':
                col_dict = []
                for i in range(len(df[c])):
                  multi = df[c][i][type]
                  multi_dict = []
                  for j in range(len(multi)):
                    multi_dict.append(multi[j]['text']['content'])
                  col_dict.append(multi_dict)
                df[c]=col_dict
                df[c] = df[c].agg(', '.join) #remove list square brackets
        
        #delete ./result.json
        os.remove('./result.json')

        return df
    
    def to_csv(self, path):
        df = self.return_pandas()
        df.to_csv(path, index=False)
    
    def show_json(self):
        with open('./result.json', 'r') as json_file:
            json_object = json.load(json_file)
        print(json.dumps(json_object, indent=4))
                
                