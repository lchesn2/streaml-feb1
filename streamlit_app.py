import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt 
# import altair as alt
# import plotly.express as px

# st.set_page_config(
#   page_title="The Lars Bars",
#   page_icon="",
#   layout="wide",
#   initial_sidebar_state="expanded")

# df= pd.read_csv('stardata3.csv')
# st.table(df)

import streamlit as st
from session_state import get

# Create a session state object
session_state = get(password="")

# Define a password for demonstration purposes
correct_password = "password123"

# Check if the user is logged in
def is_user_authenticated():
    return session_state.password == correct_password

# Streamlit app layout
def main():
    st.title("Streamlit Login Example")

    # Display login form if not logged in
    if not is_user_authenticated():
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            authenticate_user(password)

    # Display content after login
    if is_user_authenticated():
        st.success("Login successful!")
        st.write("Welcome to the Streamlit app. You can now access the content.")

# Authenticate the user
def authenticate_user(password_attempt):
    if password_attempt == correct_password:
        session_state.password = password_attempt
        st.experimental_rerun()

if __name__ == "__main__":
    main()
