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

temps = list(df.Temperature_F)
colors = list(df.Star_color)
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(colors, temps, color ='maroon', 
        width = 0.4)
 
plt.xlabel("Star Colors")
plt.ylabel("Star Temps")
plt.title("Star Data Fun")
st.pyplot(fig)
  
  
  
