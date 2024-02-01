import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px





st.set_page_config(
  page_title="The Lars Bars",
  page_icon="",
  layout="wide",
  initial_sidebar_state="expanded")

alt.themes.enable("dark")

df= pd.read_csv('stardata.csv')

with st.sidebar:
  st.title('The Lars Bars')
  
  
