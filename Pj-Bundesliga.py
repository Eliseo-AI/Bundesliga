import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

st.set_page_config(page_title="Bundesliga Analysis", page_icon=":soccer:", layout="wide")
df = pd.read_csv('data/Bundesliga.csv')

st.title("Bundesliga Data Analysis")

st.sidebar.header("Theme Selection")
theme = st.sidebar.selectbox("Choose a theme", ["plotly_white", "plotly_dark",
"ggplot2", "seaborn"])

st.sidebar.header("Filters")
season = st.sidebar.selectbox("Choose a season", df["Season"].unique())
club = st.sidebar.multiselect("Choose two club", df.query("Season == @season")["Club"].unique()[:2])

if len(clubs) == 2:
    club1, club2 = clubs

    st.header("Season Comparison")
    season_df = df[df["Season"] == season]

    club1_stats = df[(df["Club"] == club1) & (df["Season"] == season)][["Win", "Draw", "Loss"]].values.flatten()
    club2_stats = df[(df["Club"] == club2) & (df["Season"] == season)][["Win", "Draw", "Loss"]].values.flatten()
    
    fig1 = go.Figure()
    fig1.add_trace(go.Scatterpolar(r=club1_stats, theta=["Wins", "Draws", "Losses"], fill="toself", name=club1))
    fig1.add_trace(go.Scatterpolar(r=club2_stats, theta=["Wins", "Draws", "Losses"], fill="toself", name=club2))
    fig1.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True, template=theme)
    st.plotly_chart(fig1)

    st.header("Points, Goals For and Against Comparison")
    club1_stats = df[(df["Club"] == club1) & (df["Season"] == season)][["Points", "GF", "GC"]].values.flatten()
    club2_stats = df[(df["Club"] == club2) & (df["Season"] == season)][["Points", "GF", "GC"]].values.flatten()

    fig2 = go.Figure()
    fig2.add_trace(go.Scatterpolar(r=club1_stats, theta=["Points", "Goals For", "Goals Against"], fill="toself", name=club1))
    fig2.add_trace(go.Scatterpolar(r=club2_stats, theta=["Points", "Goals For", "Goals Against"], fill="toself", name=club2))
    fig2.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True, template=theme)
    st.plotly_chart(fig2)
else:
    st.warning("Please select exactly two clubs to compare.")

# Define a function to update the visualization when the clubs are changed
def update_viz(clubs):
    # Split the comma-separated list of clubs and create a new DataFrame with the data for the selected clubs
    club_list = [club.strip() for club in clubs.split(',')]
    club_df = bundesliga_df[bundesliga_df['club'].isin(club_list)]

    # Create a box with the club column
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
    plt.subplots_adjust(hspace=0.5)

    # Loop through the selected columns and create a visualization for each one
    for i, col in enumerate(['Points', 'Win', 'Draw', 'Loss', 'GF', 'GC']):
        # Calculate the mean values for each season
        season_means = bundesliga_df.groupby('season')[col].mean()

        # Create a visualization for the selected column
        ax = axs[i//3, i%3]
        for club in club_list:
            club_data = club_df[club_df['club'] == club]
            x = club_data['season']
            y = club_data[col]
            ax.plot(x, y, linestyle='dotted', label=club)
        ax.plot(season_means.index, season_means, linestyle='solid', label='Season Mean')
        ax.set_xlabel('Season')
        ax.set_ylabel(col)
        ax.legend()
        ax.set_title(col)

    # Add a title to the overall visualization
    plt.suptitle('Season Performance Comparison')
    plt.show()

# Define the default clubs to include in the text box
default_clubs = 'Bayern Munich, Borussia Dortmund'

# Create the text box widget and display it
clubs_textbox = widgets.Text(value=default_clubs, description='Clubs:')
display(clubs_textbox)

# Create a button to update the visualization
update_button = widgets.Button(description='Update')
display(update_button)

# Define the event handler for the button click
def on_button_click(button):
    update_viz(clubs_textbox.value)

# Attach the event handler to the button click
update_button.on_click(on_button_click)

