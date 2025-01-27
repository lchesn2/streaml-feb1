import streamlit as st
import pandas as pd
import bcrypt
from datetime import datetime

# Streamlit setup
st.set_page_config(page_title="Game Dashboard", layout="wide")

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

# Login page
def login(username_dict):
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True  # Skip login if already logged in

    st.title("Login")

    # Display login form and handle user input
    username = st.text_input("Username", key="username")  # This is the widget that sets session state for username
    password = st.text_input("Password", type="password", key="password")

    if st.button("Login"):
        # Check credentials and set session state
        if check_password(username, password, username_dict):
            st.session_state.logged_in = True
            st.session_state.username = username  # This updates the session state after login is successful
            st.success("Login Successful")
        else:
            st.error("Invalid username or password")

    return st.session_state.logged_in


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
