import streamlit as st
from weather_api import call_geo_code, call_weather
st.set_page_config(
    page_title = "No Name Yet",
    page_icon= "🌤️",
    layout="wide"

)
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "",
    ["Dashboard","No Name AI Assistant"]
)
if page == "Dashboard":
    st.title("DASHBOARD")
else:
    st.title("Meet AI Assistant")
