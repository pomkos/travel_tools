import streamlit as st

def app():
    st.title("Pete's Travels")
    st.write("Go ahead, click something!")

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
        st.write("""
        1. Plans on Jan 23, 2021:
            1. __Panama City Beach -> Dallas__: Leave 10:00am. Arrive 12:21pm.
            2. __Dallas -> Mexico City__: Leave 10:10pm. Arrive 12:59am.
        2. Plans Jan 24 - Feb 5
            1. :)
        3. Plans after Feb 5:
            1. Unknown.
        """)
    if 'florida' in selection:
        st.image('images/florida.jpg', width=620)
    if 'road' in selection:
        st.write("[Check out the archives](https://t.me/joinchat/SkXOm0OlcoEr0mz4)")
        st.image('images/road.jpg', width=620)