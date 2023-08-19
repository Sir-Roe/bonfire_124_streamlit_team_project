import streamlit as st
from pathlib import Path
import sys
import os
import pandas as pd

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0,filepath)

from tomongo import ToMongo
import myfuncs as mf
# Creating the ToMongo Class and pinging the data from the MongoDB
c=ToMongo()
cursor=c.park_info.find()

# list into a dataframe
df =  pd.DataFrame(list(cursor))
# Creating a unique list of activities to select from
a_list = mf.pos_values(df,'activities')

selection = st.selectbox('Type out the activity you want to see which parks have:', placeholder="ATV OFF-Roading", options=sorted(a_list))

#custom df for outputs and my avail states
dff = df.iloc[mf.locator(df,'activities',selection)]
#index corrector 
dff.reset_index(drop=True,inplace=True)
#create dummy string that plays nice in  streamlit
dff['pl']= mf.stringConvert(dff,'states')

#create possible states for the seleced activities
st_list = mf.pos_values(dff,'states')

statez = st.selectbox('States where activities are available:', placeholder="All States", options=(["All States"] + sorted(st_list)))

#conditional to make create different outputs
if statez == "All States":
    st.dataframe(pd.DataFrame({"Park Names": dff.full_name.tolist(),"States":dff.pl.tolist()}), width=800)
else:
    st.dataframe(pd.DataFrame({"Park Names": dff['full_name'].iloc[mf.locator(dff,'states',statez)].tolist(),"States":dff['pl'].iloc[mf.locator(dff,'states',statez)].tolist()}), width=800)