import streamlit as st
import numpy     as np

# Configure the page layout parameters:
st.set_page_config(
    page_title = "Teams Statistics",
    page_icon = "⚽",
    layout = "wide"
)

# Import the dataframe from the session state cache:
df_fifa = st.session_state['data']

# Create variable as categories to be used by teams' filter:
team_vals = df_fifa['Club'].unique()
team_vals = np.sort(team_vals)[::1]

# Create the sidebar selectors to filter the data by team names:
team_filter = st.sidebar.selectbox(
    label = "Teams",
    options = team_vals
)

# Create a dataframe that is filtered by the 'team_filter' select box:
df_teams = df_fifa[df_fifa['Club'] == team_filter].reset_index(drop=True).set_index('Name')
df_teams = df_teams.sort_index(ascending=True, axis=0)

# Add image of the team selected by the filter:
st.image(df_teams.iloc[0]['Club Logo'])

# Add a markdown as the name of the selected team:
st.markdown(f"## {team_filter}")

# Define the columns from the dataframe to be displayed on the table:
cols_to_show = ['Age', 'Photo', 'Flag', 'Overall', 'Value(£)', 'Wage(£)',
                'Joined', 'Height(cm.)', 'Weight(lbs.)',
                'Contract Valid Until', 'Release Clause(£)']

# Constructed the dataframe filtered by the above columns:
df_teams = st.dataframe(
    data = df_teams[cols_to_show],
    column_config = {
        "Overall": st.column_config.ProgressColumn(
            "Overall", min_value=0, max_value=100, format="%d"
        ),
        "Wage(£)": st.column_config.ProgressColumn(
            "Weekly Wage", min_value=0, format="£%f",
            max_value=df_teams['Wage(£)'].max()
        ),
        "Photo": st.column_config.ImageColumn(),
        "Flag": st.column_config.ImageColumn("Country")
    }
)