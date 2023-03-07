import streamlit as st
import pandas as pd
import plotly.express as px


df_origin = pd.read_csv('data/Bundesliga.csv')

with st.sidebar:
    season = st.multiselect('Season',sorted(df_origin['Season'].unique()))
    club = st.multiselect('Club', sorted(df_origin['Club'].unique()))
    is_state = st.checkbox('State')

def filter_data(df, season, club, is_state):
    df_copy = df.copy()

    if len(season) > 0:
        df_copy = df_copy[df_copy['Season'].isin(season)]
    if len(club) > 0:
        df_copy = df_copy[df_copy['Club'].isin(club)]

    if is_state == True:
        df_copy = df_copy[df_copy['State'] != '-']
    
    return df_copy

df_ = filter_data(df_origin, season, club, is_state)
st.title("Bundesliga")
st.subheader("Analysis")

total_jugadores = len(df_)
rating_medio = df_['Overall'].mean()
valor_medio = df_['Value(in Euro)'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("# Jugadores", f"{total_jugadores:,.0f}")
col2.metric("Rating Medio", f"{rating_medio:,.1f}")
col3.metric("Valor $ Medio", f"{valor_medio:,.0f}")



def get_team_statistics(df):
    radar_columns = ['Pace Total','Shooting Total','Passing Total',
                'Dribbling Total','Defending Total','Physicality Total']
    metrics = []
    for metric in radar_columns:
        metrics.append(df_[metric].mean())
    
    return pd.DataFrame(dict(metrics=metrics, theta=radar_columns))

radar_fig = px.line_polar(get_team_statistics(df_), r='metrics', theta='theta', line_close=True)

radar_fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 100]
    )),
  showlegend=False
)
st.plotly_chart(radar_fig)

st.dataframe(df_)