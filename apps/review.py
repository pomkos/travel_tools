import streamlit as st

st.title("Pete's Travels")
st.write("Go ahead, click something!")

def app():
    year = st.sidebar.select_slider("Choose a year",options=[2021, 2020, 2019, 2016, 2012])

    if year == 2012:
        options = ['Backpacking Through Europe']
    elif year == 2016:
        options = ['Dolly Sods Hike']
    elif year == 2019:
        options = ['Hungary']
    elif year == 2020:
        options = ['Socially Distant Road Trip', "Pete and Roos Visit the Family"]
    elif year == 2021:
        options = ['Mexico City','Florida']
    selection = st.selectbox("What would you like to see?",options = options)
    selection = selection.lower()

    if 'mexico' in selection:
        st.image('images/airport1.jpg', width=360)
    if 'florida' in selection:
        st.image('images/florida.jpg', width=620)
    if 'road' in selection:
        st.write("[Check out the archives](https://t.me/joinchat/SkXOm0OlcoEr0mz4)")
        st.image('images/road.jpg', width=620)