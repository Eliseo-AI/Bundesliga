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



