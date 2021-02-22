import streamlit as st



def app():
    st.title("Where in the world is Peter Gates?")
    st.write("""
    Right now he is in __Mexico City__
    He will be in __Naples, FL__ on Feb 28
    """)
    st.write("## Plane Ticket")
    st.image("images/ticket.png")
    
    # admin page
    admin = st.experimental_get_query_params()
    if admin:
        st.write(admin)
app()