from pathlib import Path
import streamlit as st
import pandas as pd
import os
import sys

#establish a filepath to the orcale_cards.csv file
filepath=os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from tomongo import ToMongo
import myfuncs as mf
c=ToMongo()

#grab my collection
cursor=c.park_info.find()

#list into a dataframe
df =  pd.DataFrame(list(cursor))
#cleanse all nulls on the long and lat

#grab the stats list for possible values

states=mf.pos_values(df,'states')


st.header("Parks by State")

state=st.selectbox("Select a state:",options=states)


def locator (df,col,val):
    a_list=[]
    for i in range(len(df[col])):
        if type(df[col][i])==list:
            if val in df[col][i]:
                a_list.append(i)
        else:
            if val == df[col][i]:
                a_list.append(i)
    #return the list of locations to be used as a .iloc filter
    return a_list



st.map(df[['latitude','longitude']].iloc[locator(df,'states',state)],color="#39FF14")

result = st.data_editor(df['full_name'].iloc[mf.locator(df,'states',state)],hide_index=True,width=800)


