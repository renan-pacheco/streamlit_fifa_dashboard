import streamlit  as st
import pandas     as pd
from datetime import datetime

# Set the page configurations:
st.set_page_config(
    layout = "wide",
    page_icon = "🏠",
    page_title = "FIFA Overview & Players"
)

# Finally run the dataframe into the session state to be used by other pages:
@st.cache_data
def load_data() -> pd.DataFrame:
    """
    Function that reads the dataset
    :returns: Dataframe with loaded data
    """
    if "data" not in st.session_state:
        # Import the dataframe from the directory:
        df_fifa = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv')
        # Drop first column:
        df_fifa.drop(columns=['Unnamed: 0'], inplace=True)
        # Filter the dataset based on necessary criteria:
        df_fifa = df_fifa[df_fifa['Contract Valid Until'] >= datetime.today().year]
        df_fifa = df_fifa[df_fifa['Value(£)'] > 0]
        df_fifa = df_fifa.sort_values(by='Overall', ascending=False).reset_index(drop=True)

    return df_fifa

# Initialize the session state:
st.session_state["data"] = load_data()


# ==================================================================================================

# Create a markdown title for the main page:
st.markdown("## FIFA 2023 OFFICIAL DATASET ⚽")

# Create markdown texts for the side bar:
st.sidebar.markdown("App developed by Renan. All copyrights reserved.")
st.sidebar.markdown(
    "Please refer to my Linkedin page [here](https://www.linkedin.com/in/renan-pacheco-301324aa/)."
)

# Create button and logic for accessing Kaggle dataset page:
button = st.link_button(
    "Acess official dataset in Kaggle",
    "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data"
)

# Create markdown text to be printed on the main screen:
st.markdown(
    """
    The Football Player Dataset from 2017 to 2023 provides comprehensive information about 
    professional football players. The dataset contains a wide range of attributes, including 
    player demographics, physical characteristics, playing statistics, contract details, and club 
    affiliations. 
    
    **With over 17,000 records**, this dataset offers a valuable resource for football 
    analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing 
    world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, 
    player positioning, and player development over time.
    """
)

# if __name__ == '__main__':
#     load_data()