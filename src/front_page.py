import streamlit as st

st.title("National Park Service")
st.text("An application that uses Streamlit, Pandas, MongoDB, and Tableau")

st.header("Here are the different pages of my application.")
st.subheader('Park Info')
st.text('Park Info: Query to pull up a single park.')
st.text("""This information pull are park name, an image, park hours,
        park description, park url, activities & topics, entrance fees if any""")

st.subheader("Activities")
st.text("Activities: Query that returns all parks with those activities.")

st.subheader("Mapping")
st.text("Mapping: Pulls a map from Tableau that can be zoomed in to see each park.")

st.subheader("Stats")
st.text("Stats: Pulls statistical information from a Tableau Dashboard")

st.subheader("Summary")
st.text("""Summary: A page explaining all the inner workings
        of the app and the "why" behind each""")