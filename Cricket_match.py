import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('ODI_Match_info.csv')

# Set up the Streamlit app layout
st.title("Cricket Match Analysis")
st.sidebar.header("Select Options for Analysis")

# Sidebar: User Input for Analysis
st.sidebar.subheader("Analyze Team Performance")
Your_Team = st.sidebar.selectbox('Select Your Team for Analysis', df['team1'].unique())
Opposite_Team = st.sidebar.selectbox('Select Opposite Team for Comparison', df['team2'].unique())
Venue = st.sidebar.selectbox('Select Venue for Analysis', df['venue'].unique())
Toss_Winner = st.sidebar.selectbox('Select Toss Winner for Analysis', df['team1'].unique())

# Sidebar Button: Team Performance Analysis
if st.sidebar.button("Analyze Team Performance"):
    st.write(f"Analyzing Performance of {Your_Team}")
    
    # Filter data for team performance analysis
    filtered_data = df[(df['team1'] == Your_Team) | (df['team2'] == Your_Team)]
    
    # Matches played and won by the selected team
    matches_played = len(filtered_data)
    matches_won = len(filtered_data[filtered_data['winner'] == Your_Team])
    st.write(f"Matches Played: {matches_played}, Matches Won: {matches_won}")
    
    # Display a simple bar chart for toss wins and match wins
    toss_wins = df['toss_winner'].value_counts()
    match_wins = df['winner'].value_counts()
    
    fig, ax = plt.subplots(1, 2, figsize=(22, 8))
    
    ax[0].bar(toss_wins.index, toss_wins.values)
    ax[0].set_title('Total Tosses Won by Country')
    ax[0].set_xticklabels(toss_wins.index, rotation=90)
    
    ax[1].barh(match_wins.index, match_wins.values)
    ax[1].set_title('Wins by Country')
    
    st.pyplot(fig)

# Sidebar Button: Opposite Team Analysis
if st.sidebar.button("Analyze Team Comparison"):
    st.write(f"Analyzing Matches between {Your_Team} and {Opposite_Team}")
    
    # Filter data for matches between selected teams
    filtered_data = df[((df['team1'] == Your_Team) & (df['team2'] == Opposite_Team)) |
                       ((df['team1'] == Opposite_Team) & (df['team2'] == Your_Team))]
    
    total_matches_played = len(filtered_data)
    st.write(f'Total Matches Played between {Your_Team} and {Opposite_Team}: {total_matches_played}')
    
    matches_won_your_team = len(filtered_data[filtered_data['winner'] == Your_Team])
    matches_won_opposite_team = len(filtered_data[filtered_data['winner'] == Opposite_Team])
    
    # Show results
    st.write(f"Matches Won by {Your_Team}: {matches_won_your_team}")
    st.write(f"Matches Won by {Opposite_Team}: {matches_won_opposite_team}")
    
    # Plot a pie chart for wins comparison
    labels = [Your_Team, Opposite_Team]
    sizes = [matches_won_your_team, matches_won_opposite_team]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(f'Win Distribution between {Your_Team} and {Opposite_Team}')
    
    st.pyplot(fig)
