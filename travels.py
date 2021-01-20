import streamlit as st

selection = st.sidebar.selectbox("What should we do", ['Explore','Review'])
selection = selection.lower()

if 'review' in selection:
    from apps import review
    review.app()
elif 'explore' in selection:
    from apps import explore
    explore.app()