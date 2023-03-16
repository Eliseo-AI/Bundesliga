import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Bundesliga Analysis", page_icon=":soccer:", layout="wide")
df = pd.read_csv('data/Bundesliga.csv')

st.title("Bundesliga Data Analysis")

st.sidebar.header("Theme Selection")
theme = st.sidebar.selectbox("Choose a theme", ["plotly_white", "plotly_dark",
"ggplot2", "seaborn"])

st.sidebar.header("Filters")
season = st.sidebar.selectbox("Choose a season", df["Season"].unique())
club = st.sidebar.selectbox("Choose a club", df(df["Club"]==season))

st.header("Season Comparison")
season_df = df[df["Season"]==season]
season_avg = season_df[["W", "D", "L"]].mean()
club_stats = df[(df["Club"]==club) & (df["Season"]==season)][["W", "D", "L"]]
fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=[season_avg.W, season_avg.D, season_avg.L],
theta=["Wins", "Draws", "Losses"],
fill="toself",
name="Season Average"))
fig.add_trace(go.Scatterpolar(r=[club_stats.W, club_stats.D, club_stats.L],
theta=["Wins", "Draws", "Losses"],
fill="toself",
name=club))
fig.update_layout(polar=dict(radialaxis=dict(visible=True)),
showlegend=True,
template=theme)
st.plotly_chart(fig)

st.header("Points, Goals For and Against Comparison")
season_df = df[df["Season"]==season]
season_avg = season_df[["Pts", "GF", "GC"]].mean()
club_stats = df[(df["Club"].isin(clubs)) & (df["Season"]==season)][["Pts", "GF", "GC"]]
fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=[season_avg.Pts, season_avg.GF, season_avg.GC],
theta=["Points", "Goals For", "Goals Against"],
fill="toself",
name="Season Average"))
for club in clubs:
        club_stats_2 = df[(df["Club"]==club) & (df["Season"]==Season)][["Pts", "GF", "GC"]]
        fig.add_trace(go.Scatterpolar(r=[club_stats_2.Pts, club_stats_2.GF, club_stats_2.GC],
        theta=["Points", "Goals For", "Goals Against"],
        fill="toself",
        name=club))
fig.update_layout(polar=dict(radialaxis=dict(visible=True)),
showlegend=True,
template=theme)
st.plotly_chart(fig)
