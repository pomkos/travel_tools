import streamlit as st

st.set_page_config(page_title='Traveling Tuesday', page_icon="✈️")

selection = st.sidebar.selectbox("What should we do", ['Find Peter','Research','Review'])
selection = selection.lower()

if 'home' in selection:
    from apps import explore
    explore.app()
    
elif 'research' in selection:
    from apps import review
    review.app()
    
elif 'peter' in selection:
    from apps import find_me
    find_me.app()
