import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
# import altair as alt
# import plotly.express as px





st.set_page_config(
  page_title="The Lars Bars",
  page_icon="",
  layout="wide",
  initial_sidebar_state="expanded")

# alt.themes.enable("dark")

df= pd.read_csv('stardata3.csv')



# shows as table
#st.table(df)


# graphing plot

t= (df['Temperature_K'] - 273.15) * 9/5 + 32
df.insert(loc=1,column='Temperature_F', value=t) 
  
# creating the dataset

st.bar_chart(chart_data, x="Temperature_F", y="Star_color", , color=["#DFFF00", "#6495ED"] )
  
  
  
