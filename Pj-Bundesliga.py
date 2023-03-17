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
club = st.sidebar.multiselect("Choose club(s)", df.query("Season == @season")["Club"].unique(),default=season[:2])

st.header("Season Comparison")
season_df = df[df["Season"]==season]
season_avg = season_df[["Win", "Draw", "Loss"]].mean()
club_stats = df[(df["Club"]==club) & (df["Season"]==season)][["Win", "Draw", "Loss"]]
fig1 = go.Figure()
fig1.add_trace(go.Scatterpolar(r=[season_avg.Win, season_avg.Draw, season_avg.Loss],
theta=["Wins", "Draws", "Losses"],
fill="toself",
name="Season Average"))
fig1.add_trace(go.Scatterpolar(r=[club_stats.Win, club_stats.Draw, club_stats.Loss],
theta=["Wins", "Draws", "Losses"],
fill="toself",
name=club))
fig1.update_layout(polar=dict(radialaxis=dict(visible=True)),
showlegend=True,
template=theme)
st.plotly_chart(fig1)

st.header("Points, Goals For and Against Comparison")
season_df = df[df["Season"]==season]
season_avg = season_df[["Points", "GF", "GC"]].mean()
club_stats = df[(df["Club"]==club) & (df["Season"]==season)][["Points", "GF", "GC"]]
fig2 = go.Figure()
fig2.add_trace(go.Scatterpolar(r=[season_avg.Points, season_avg.GF, season_avg.GC],
theta=["Points", "Goals For", "Goals Against"],
fill="toself",
name="Season Average"))
fig2.add_trace(go.Scatterpolar(r=[club_stats.Points, club_stats.GF, club_stats.GC],
theta=["Points", "Goals For", "Goals Against"],
fill="toself",
name=club))
fig2.update_layout(polar=dict(radialaxis=dict(visible=True)),
showlegend=True,
template=theme)
st.plotly_chart(fig2)
