import streamlit as st
import requests 
import os
import sys
from PIL import Image
from pathlib import Path
import pandas as pd
from io import BytesIO
filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)
import myfuncs as mf
from tomongo import ToMongo

c=ToMongo()
cursor=c.park_info.find()
df =  pd.DataFrame(list(cursor))


st.image('https://www.nps.gov/articles/images/NPS-Transparent-Logo.png',width=80)

st.title('Find A Park')

pk_list = df.full_name.tolist()
select= st.selectbox('type a park', options=pk_list)
if select:
    st.subheader(select)
    
    for i in range(len(df['full_name'])):
        if select == df['full_name'][i]:
            link = (df['images'][i][0])
            index = i
    st.image(link['url'],caption=link['caption'])
    st.subheader('About The Park:')
    st.write(df['description'][index])
    st.subheader('Things to do:')
    act_string=''
    for act in df['activities'][index]:
        act_string +=act+', '
    st.markdown(act_string)
    st.subheader('Entrance fees types and hours:')
   
    #sort hours func to grab hours value
    st.dataframe(mf.hour_sort(df['standard_hours'][index]))

    if type(df['entrance'][index]) == list:
        st.dataframe(pd.DataFrame({"Fee":df['entrance'][index],"Costs":df['cost'][index]}),hide_index=True)
    else:
        st.dataframe({"Fee":df['entrance'][index],"Costs":df['cost'][index]})


    st.subheader('Press the link for more info')
    st.write(df['url'][index])
    