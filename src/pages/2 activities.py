import streamlit as st
from pathlib import Path
import sys
import os
import pandas as pd

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0,filepath)

from tomongo import ToMongo
import myfuncs as mf
c=ToMongo()
cursor=c.park_info.find()


# list into a dataframe
df =  pd.DataFrame(list(cursor))

# Creating a unique list of states to pick from
st_list = []
for i in range(len(df['states'])):
    for sta in df['states'][i]:
        st_list.append(sta)


selection = st.selectbox('Type out the activity you want to see which parks have:', options=mf.pos_values(df,['activities']))


st_list = mf.pos_values(df,'states')
