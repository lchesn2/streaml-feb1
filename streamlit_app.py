import streamlit as st
import pandas as pd
import bcrypt
from datetime import datetime
import sqlalchemy
import requests

import streamlit as st
import pymysql
from sqlalchemy import create_engine
import mysql.connector
import streamlit as st
import pandas as pd

import MySQLdb
import sshtunnel

st.set_page_config(page_title="Game Dashboard", layout="wide")


# timeout = 10
# connection = pymysql.connect(
#   charset="utf8mb4",
#   connect_timeout=timeout,
#   cursorclass=pymysql.cursors.DictCursor,
#   db="defaultdb",
#   host="sequence-larahsmiles-seq.e.aivencloud.com",
#   read_timeout=timeout,
#   port=26458,
#   user="avnadmin",
#   write_timeout=timeout,
# )
  
# try:
#   cursor = connection.cursor()
#   cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
#   cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
#   cursor.execute("SELECT * FROM mytest")
#   print(cursor.fetchall())
# finally:
#   connection.close()



# try:
#     with st.spinner('Connecting to database...'):
#         # df = run_query('SELECT * FROM Memories LIMIT 5')  # Test with limited data first
#         # st.dataframe(df)
#         conn = st.connection(
#             "mysql",
#             type="sql",
#             url="mysql+pymysql://oldgreg:spong3Bob@oldgreg.mysql.pythonanywhere-services.com:3306/oldgreg$mems"
#         )
#         df = conn.query("SHOW TABLES;")
# except Exception as e:
#     st.error(f"Connection failed: {str(e)}")
# conn = st.connection(
#     "mysql",
#     type="sql",
#     url="mysql+pymysql://oldgreg:spong3Bob@oldgreg.mysql.pythonanywhere-services.com:3306/oldgreg$mems"
# )




# db = pymysql.connect(host = "oldgreg.mysql.pythonanywhere-services.com",
#                     user = "oldgreg",
#                      passwd="spong3Bob",  # your password
#                      db="oldgreg$mems")        # name of the data base
# conn = st.connection(
#     "mysql",
#     type="sql",
#     url="mysql:://oldgreg:spong3Bob@oldgreg.mysql.pythonanywhere-services.com/oldgreg$mems"
# )

#df = conn.query("SELECT * FROM Memories")


# Dictionary for storing usernames and hashed passwords (For simplicity, we're using a small dict here)
# In a real-world scenario, you would likely want to store these securely in a file or database.
username_dict = {
    'Larah': bcrypt.hashpw('newton'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')  # Hashed password for 'newton'
}

# Helper function for user authentication (with password hashing)
def check_password(username, password, username_dict):
    if username in username_dict:
        # Check if the provided password matches the hashed password
        if bcrypt.checkpw(password.encode('utf-8'), username_dict[username].encode('utf-8')):
            return True
    return False



# Function to display game data
def display_game_data():
    today = datetime.now().date()
    st.title("Game Dashboard")

    # Load data (replace with SQL queries if using a DB)
    game_df = pd.read_csv('./games.csv')
    team_df = pd.read_csv('./dailyteams.csv')

    # Filter today's data
    today_games = game_df[game_df['date'] == str(today)]
    today_teams = team_df[team_df['date'] == str(today)]

    st.write("Today's Games")
    st.dataframe(today_games)

    st.write("Today's Teams")
    st.dataframe(today_teams)

# Function to submit game results
def submit_game_result():
    st.title("Submit Game Result")

    date = st.date_input("Date", min_value=datetime(2022, 1, 1))
    time = st.time_input("Time", value=datetime.now().time())
    name = st.selectbox("Player 1", ["Fermi","Andy","Behring","Brian","Daniel","Hannah","Howard","Ghost","Jose","Jaemo","Kenji","Larah","Maya","Mel","Nate","Nishant","Paul","Poonam","Russel"])
    game_type = st.selectbox("Game Type", ["Assist", "Block", "Sequence"])
            

    if st.button("Submit"):
        new_game = {
            'date': date,
            'time': time,
            'name': name,
            'type': game_type
        }

        # Save new game to CSV (use a DB in production)
        game_df = pd.read_csv('./games.csv')#
        game_df.loc[len(game_df)]=new_game
        #game_df = game_df.append(new_game, ignore_index=True)
        game_df.to_csv('./games.csv', index=False)

        st.success("Game result submitted successfully!")



# Function to show the Hall of Fame
def hall_of_fame():
    st.title("Hall of Fame")

    # Load and process the game data
    df = pd.read_csv('./games.csv')
    current_year = datetime.now().year
    this_year = df[df['date'].str[:4] == str(current_year)]

    block = this_year[this_year['type'] == 'Block'].groupby('name').size().reset_index(name='TotalFinishes').sort_values(by='TotalFinishes', ascending=False)
    assist = this_year[this_year['type'] == 'Assist'].groupby('name').size().reset_index(name='TotalFinishes').sort_values(by='TotalFinishes', ascending=False)
    seq = this_year[this_year['type'] == 'Sequence'].groupby('name').size().reset_index(name='TotalFinishes').sort_values(by='TotalFinishes', ascending=False)

    st.write("Top Block Players")
    st.dataframe(block)

    st.write("Top Assist Players")
    st.dataframe(assist)

    st.write("Top Sequence Players")
    st.dataframe(seq)

# Main function to control the app flow
def main():
    # Call the login function and return if not logged in
#    if not login(username_dict):
#        return

    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Choose an option", ["Dashboard", "Submit Game", "Hall of Fame"])

    if option == "Dashboard":
        display_game_data()
    elif option == "Submit Game":
        submit_game_result()
#    elif option == "Submit Team":
#        submit_team()
    elif option == "Hall of Fame":
        hall_of_fame()

if __name__ == "__main__":
    main()
