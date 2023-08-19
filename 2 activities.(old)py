import streamlit as st
from pathlib import Path
import sys
import os
import pandas as pd

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0,filepath)

from tomongo import ToMongo
# Creating the ToMongo Class and pinging the data from the MongoDB
c=ToMongo()
cursor=c.park_info.find()


# list into a dataframe
df =  pd.DataFrame(list(cursor))

# Creating a unique list of activities to select from
a_list = []
for i in range(len(df['activities'])):
    for act in df['activities'][i]:
        a_list.append(act)
a_list = list(set(a_list))
# Creating a unique list of states to pick from
st_list = []
for i in range(len(df['states'])):
    if type(df['states'][i]) == list:
        for sta in df['states'][i]:
            st_list.append(sta)
    else:
        st_list.append(df['states'][i])

st_list = list(set(st_list))


selection = st.selectbox('Type out the activity you want to see which parks have:', options=sorted(a_list))
# if loop to go through the dataframe and pull into a list every park with that
# activity. The list is converted into a set to get all the unique values and
# reconverted back into a list to be used. Afterwards, Streamlit will write the user a 
# pandas DataFrame showing all the park names that include that activity.

if selection:
    # Makes a new select box from the unique states list while adding the 
    # All States as an option. The All States is set as a placeholder so that 
    # the first thing the user sees is every park with that activity.
    # This also cognitively tells the user that out of all the state options, 
    # there is an All States option for them to use in case they would
    # assume otherwise.
    statez = st.selectbox('Select a state you would like to see:', placeholder="All States", options=(["All States"] + sorted(st_list)))
    # Since there are no All States in the states column, it is set to its own
    # conditional to pull every park that meets that condition and by index,
    # its state.
    if statez == "All States":
        p_list = []
        s_list = []
        for i in range(len(df['activities'])):
            for act in df['activities'][i]:
                if act == selection:
                    p_list.append(df['full_name'][i])
                    if type(df['states'][i]) == list:
                        s_list.append(", ".join(df['states'][i]))
                    else:
                        s_list.append(df['states'][i])
    
        st.dataframe(pd.DataFrame({"Park Names": p_list,"States":s_list}), width=800)
    # Once a state has been inputted, the application will check for any park 
    # that has that activity. It will then iterate through the pulled park's
    # states to see if the park resides in the state. If it does, it is
    # appended to the list and added to the DataFrame to be shown to the user.
    else:
        p_list = []
        s_list = []
        for i in range(len(df['activities'])):
            for act in df['activities'][i]:
                if act == selection:
                    if type(df['states'][i]) == list:
                        if statez in df['states'][i]:
                            s_list.append(", ".join(df['states'][i]))
                            p_list.append(df['full_name'][i])
                    else:
                        if statez == df['states'][i]:
                            s_list.append(df['states'][i])
                            p_list.append(df['full_name'][i])
        st.dataframe(pd.DataFrame({"Park Names": p_list,"States":s_list}), width=800)