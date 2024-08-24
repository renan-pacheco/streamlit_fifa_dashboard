import streamlit as st
import numpy     as np

# Configure the page layout parameters:
st.set_page_config(
    layout = "wide",
    page_icon = "🏃‍",
    page_title = "Players Statistics"
)

# Import the dataframe from the session state cache:
df_fifa = st.session_state['data']

# Create variable as categories to be used by teams' filter:
team_vals = df_fifa['Club'].unique()
team_vals = np.sort(team_vals)[::1]  #Team names sorted in alphabetical order (from A to Z)

# Create the sidebar selectors to filter the data by team names:
team_filter = st.sidebar.selectbox(
    label = "Teams",
    options = team_vals
)

# Create a dataframe that is filtered by the 'team_filter' select box:
df_player = df_fifa[df_fifa['Club'] == team_filter].reset_index(drop=True)

# Create variable as categories to be used by the players' filter:
player_vals = df_player['Name'].unique()
player_vals = np.sort(player_vals)[::1]  #Player names sorted in alphabetical order (from A to Z)

# Create the sidebar selectors to filter the data by player names:
player_filter = st.sidebar.selectbox(
    label = "Player",
    options = player_vals
)

# Get the instance of each player selected by the 'player_filter' box filter:
player_stats_instance = df_fifa[df_fifa['Name'] == player_filter].iloc[0]

# Display photo of the player selected by the 'player_filter' box filter:
st.image(player_stats_instance['Photo'])

# Display name of the player as a title:
st.title(player_stats_instance['Name'])

# Display other features of the player as markdown:
st.markdown(f"**Team/Club:** {player_stats_instance['Club']}")
st.markdown(f"**Position:** {player_stats_instance['Position']}")

# Create a table-like structure to show the player's features as columns:
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Age** {player_stats_instance['Age']}")
col2.markdown(f"**Height:** {player_stats_instance['Height(cm.)'] / 100} m")
col3.markdown(f"**Weight:** {(player_stats_instance['Weight(lbs.)'] * 0.453):.2f} kg")

# Create a physical divider for the next section:
st.divider()

# Display a sub-header for the player's overall stat:
st.subheader(f"Overall Stat: {player_stats_instance['Overall']}")

# Display a progress bar for the player's overall stat:
st.progress(value = int(player_stats_instance['Overall']))

# Create another physical divider:
st.divider()

# Create another table-like structure for other player's features:
col1, col2, col3 = st.columns(3)

# For each column of the table-like structure, add player's metrics as cards:
col1.metric(label = "Market Value", value = f"£ {player_stats_instance['Value(£)']:,}")
col2.metric(label = "Weekly Wage", value = f"£ {player_stats_instance['Wage(£)']:,}")
col3.metric(label = "Release Clause", value = f"£ {player_stats_instance['Release Clause(£)']:,}")
