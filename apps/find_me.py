import streamlit as st
import datetime as dt

def admin():
    '''
    Upload status and files
    '''
    col1, col2 = st.beta_columns()
    
    with col1:
        current_loc = st.text_input("Where are you?")
        current_date = dt.datetime.now()
    with col2:
        future_loc = st.text_input("Where are you going?")
        future_date = st.date_input("When?", min_value=dt.datetime.now())

def app():
    st.title("Where in the world is Peter Gates?")
    st.write("""
    * Right now he is in __Mexico City__
    * He will be in __Naples, FL__ on Feb 28
    """)
    st.write("## Plane Ticket")
    #st.image("images/ticket.png")
    
    # admin page
    admin = st.experimental_get_query_params()
    if admin:
        admin()
app()