import streamlit as st
import pandas as pd
import plotly.express as px

df_origin = pd.read_csv('data/Bundesliga.csv')

with st.sidebar:
    Club = st.multiselect('Club', sorted(df_origin['Club'].unique()))
    Season = st.multiselect('Season', sorted(df_origin['Season'].unique()))
    City = st.checkbox('Location')

def filter_data(df, City, Season):
    df_copy = df.copy()

    if len(City) > 0:
        df_copy = df_copy[df_copy['Location'].isin(City)]
    if len(Season) > 0:
        df_copy = df_copy[df_copy['Season'].isin(Season)]

    if City == True:
        df_copy = df_copy[df_copy['Location'] != '-']
    
    return df_copy

df_ = filter_data(Season, Club, City)
st.title("Bundesliga")
st.subheader("Analysis")

total_clubs = len(df_)
Average_Points = df_['Pts'].mean()
Average_Goals = df_['GF)'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Club", f"{total_clubs:,.0f}")
col2.metric("Pts", f"{Average_Points:,.2f}")
col3.metric("GF", f"{Average_Goals:,.2f}")



def get_team_statistics(df):
    radar_columns = ['W','D','L','GF','GC','Pts']
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
