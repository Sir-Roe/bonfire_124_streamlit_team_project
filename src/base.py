from dotenv import load_dotenv
from os import getenv
from pathlib import Path
import pandas as pd
import urllib.request, json
import os
import numpy as np
load_dotenv()



folder_dir = os.path.join(Path(__file__).parents[0], 'data')

print(folder_dir)



class Base:
    
    __key= getenv("KEY")


    def __init__(self):
        self.api_url = "https://developer.nps.gov/api/v1/parks?limit=500"
        self.get_data()
        self.clean_data()
    
    def return_url(self):
        return self.api_url
    
    def get_data(self):
        endpoint = "https://developer.nps.gov/api/v1/parks?limit=500"
        HEADERS = {"X-Api-Key":self.__key}
        req = urllib.request.Request(endpoint,headers=HEADERS)
        response = urllib.request.urlopen(req)
        data = response.read()

        json_data = json.loads(data.decode('utf-8'))
        parks = json_data['data']
        self.df = pd.DataFrame.from_dict(parks)

    def clean_data(self):
        #dropping columns that had low data or unneccessary data
        self.df.drop(axis=1,columns = ['fees','latLong','entrancePasses','directionsInfo','directionsUrl','addresses','images','weatherInfo','name','contacts'],inplace= True)
        #rename old columns
        name_change = [{'fullName':'full_name'},{'parkCode':'park_code'},{'entranceFees':'entrance_fees'},{'operatingHours':'operating_hours'}]
        for name in name_change:
            self.df.rename(columns=name,inplace=True)
        #convert to numerics 
        self.df = self.df.apply(pd.to_numeric,errors='ignore')
        #fix 
        self.column_fix('topics')
        self.column_fix('activities')
        #split the cost and entrance values
        cost=[]
        entrance=[]

        for i in self.df['entrance_fees']:
            if len(i)==0:
                cost.append(0)
                entrance.append('Entrance - Free')
            else:
                if len(i)>0:
                    cost.append([i[c]['cost'] for c in range(len(i))])
                if len(i)>0:
                    entrance.append([i[c]['title'] for c in range(len(i))])

        self.df['cost']=cost
        self.df['entrance']=entrance

        self.df.drop('entrance_fees',axis=1,inplace=True)
        self.df['designation']=self.df['designation'].replace('',np.nan)
    #-----------------------------------Correct_Holidays-----------------------------

        operating=[]
        holidays=[]
        for i in self.df['operating_hours']:
            if len(i)>0:
                operating.append(i[0]['standardHours'])
            if len(i)==0:
                operating.append(np.nan)

        for i in self.df['operating_hours']:
            if len(i)>0 and len(i[0]['exceptions'])>0:
                holidays.append(list(set([i[0]['exceptions'][x]['name'] for x in range(len(i[0]['exceptions']))])))
            else:
                holidays.append(np.nan)

        self.df['standard_hours']=operating
        self.df['holidays']=holidays
        self.df.drop(columns='operating_hours', axis=1, inplace=True)
        #-----------------------------correct_states-------------------------
        s_list=[]
        for i in range(len(self.df['states'])):
            if len(self.df['states'].iloc[i].split(','))>1:
                s=self.df['states'].iloc[i].split(',')

                s_list.append(list([j for j in s]))
            else:
                s_list.append(self.df['states'].loc[i].split(',')[0])
        self.df['states'] = s_list


    #cleaning columns 
    def column_fix(self,column,name='name'):
            for i in range(len(self.df[column])):
                a_list = []
                for e in range(len(self.df[column][i])):
                    a_list.append(self.df[column][i][e][name])
                self.df[column][i] = a_list


    
        
        
if __name__ == '__main__':
    c = Base()
    print(c.df.info())
    c.df.to_csv(fr'{folder_dir}\National_Parks.csv', index=False)
