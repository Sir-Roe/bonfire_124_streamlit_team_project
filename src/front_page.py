import streamlit as st



st.set_page_config(
    page_title="National Parks App", #<------- Change this to the page you're currently on when copying/pasting after your imports
    page_icon="⛰️",
    menu_items={
        'About': """This is an app developed by 5 Peers at Coding Temple. Here are our
        Github accounts: \n\rHarrison : https://github.com/Acronine, \n\rJoshua : https://github.com/TechNTalk,
        \n\rLogan : https://github.com/Sir-Roe, \n\rVaidic: https://github.com/tvaidic"""}
)

st.title("National Park Service")

st.image('https://www.nps.gov/articles/images/NPS-Transparent-Logo.png',width=200)

st.text("Our Weekend Parks Project that uses: Streamlit, Python, MongoDB, Pandas, and National Parks API")

st.header("Here are the different pages of our application:")
st.subheader('Park Info')
st.text('Park Info: Query to pull up a single park.')
st.text("""This information pull are park name, an image, park hours,
        park description, park url, activities & topics, entrance fees if any""")

st.subheader("Activities")
st.text("Activities: Query that returns all parks with those activities.")

st.subheader("Mapping")
st.text("Mapping: Pulls a map from Tableau that can be zoomed in to see each park.")

st.subheader("Summary")
st.text("""Summary: A page explaining all the inner workings
        of the app and the "why" behind each""")
