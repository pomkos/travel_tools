import streamlit as st
import datetime as dt

def settings():
    '''
    Upload status and files
    '''
    col1, col2 = st.beta_columns(2)
    
    with col1:
        current_loc = st.text_input("Where are you?")
        my_pic = st.file_uploader("Upload plane ticket",type=['png','jpg'])
        
        if my_pic is not None:
            st.write(uploaded_file.getvalue())
        
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
        settings()
app()