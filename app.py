import streamlit as st
from weather_api import call_geo_code, call_weather
weather_codes = {
	"0": "Clear sky",
	"1": "Mainly clear",
	"2": "Partly cloudy",
	"3": "Overcast",
    "48": "Depositing rime fog",
	"45": "Fog",
	"51": "Light drizzle",
	"53": "Moderate drizzle",
	"55": "Dense drizzle",
	"56": "Light freezing drizzle",
	"57": "Dense freezing drizzle",
	"61": "Slight rain",
	"63": "Moderate rain",
	"65": "Heavy rain",
	"66": "Light freezing rain",
	"67": "Heavy freezing rain",
	"71": "Slight snowfall",
	"73": "Moderate snowfall",
	"75": "Heavy snowfall",
	"77": "Snow grains",
	"80": "Slight rain showers",
	"81": "Moderate rain showers",
	"82": "Violent rain showers",
	"85": "Slight snow showers",
	"86": "Heavy snow showers",
	"95": "Thunderstorm",
	"96": "Thunderstorm with slight hail",
	"97": "Heavy thunderstorm",
	"99": "Thunderstorm with heavy hail"

}
st.set_page_config(
    page_title = "No Name Yet",
    page_icon= "🌤️",
    layout="wide"

)
st.markdown("""
<style>
.current-weather-card{
    width: 1000px;
    background-color: #1F2937;
    padding: 20px;
    border-radius: 12px;
    color: #F9FAFB;
}
</style>
""", unsafe_allow_html = True)
st.sidebar.title("Explore")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard","No Name AI Assistant"]
)
if page == "Dashboard":
    st.title("DASHBOARD")
    with st.form("city_search"):
        city = st.text_input(
            "Search for a city",
            placeholder = "e.g London"
        )
        submitted = st.form_submit_button("Search")
        
    if submitted:
        if not city.strip():
            st.warning("Please enter a city.")
        else:
            try:
                coordinates = call_geo_code(city)
                if coordinates is None:
                    st.error("City not found!")
                else:
                    latitude = coordinates[0]
                    longitude = coordinates[1]
                    with st.spinner("Searching for city..."):
                        data = call_weather(latitude, longitude)
                    temperature = data["current"]["temperature_2m"]
                    humidity = data["current"]["relative_humidity_2m"]
                    feel_like_temp = data["current"]["apparent_temperature"]
                    wind_speed = data["current"]["wind_speed_10m"]
                    uv_index = data["current"]["uv_index"]
                    weather_code_num = data["current"]["weather_code"]
                    condition = weather_codes.get(str(weather_code_num), "Unknown Weather Code")
                    st.markdown(f"""
                    <div class = "current-weather-card">
                        <h2>{temperature} F</h2>
                        <p>{condition}</p>
                    </div>
                    """, unsafe_allow_html = True)
            except Exception as e:
                st.error("Something went wrong!")
       
else:
    st.title("Meet AI Assistant")
