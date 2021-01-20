import streamlit as st

st.set_page_config(page_title='Traveling Tuesday', page_icon="✈️")

selection = st.sidebar.selectbox("What should we do", ['Home','Review'])
selection = selection.lower()

if 'home' in selection:
    from apps import explore
    explore.app()
    
elif 'review' in selection:
    from apps import review
    review.app()