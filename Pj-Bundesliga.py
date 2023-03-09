import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
df_bundes = pd.read_csv('data/Bundesliga.csv')

unique_values = sorted(set(df_bundes["Club"].unique()) | set(df_bundes["Season"].unique()))

selected_values = st.sidebar.multiselect("Select values", unique_values)

filtered_df = df_bundes[(df_bundes["Club"].isin(selected_values)) | (df_bundes["Season"].isin(selected_values))]

st.title("Bundesliga")
st.markdown(
'''A collaborative''')
    
st.subheader("Analysis")
with st.beta_expander("Explanation & Tips"):
     st.markdown(""" The Bundesliga Statistics. \n
     1. Total Number of Clubs.
     2. Average of Points(win= 3 points, Draw = 1 point, Loss = 0 Points).
     3. Average Goals for.
     4. Graph consolidate average of Wins, Losses and Draws. 
     5. Graph consolidate average of Wins, Losses and Draws.
     6. Choose view between normalized over 100k and non-normalized data. 
     
total_clubs = len(df_bundes)
Average_Points = df_bundes["Points"].mean()
Average_Goals = df_bundes["GF"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Club", f"{total_clubs:,.0f}")
col2.metric("Points", f"{Average_Points:,.2f}")
col3.metric("GF", f"{Average_Goals:,.2f}")

def get_team_games(df_bundes):
    radar_columns = ['Win','Draw','Loss']
    metrics = []
    for metric in radar_columns:
        metrics.append(df_bundes[metric].mean())
    
    return pd.DataFrame(dict(metrics=metrics, theta=radar_columns))

radar_fig_1 = px.line_polar(get_team_games(df_bundes), r='metrics', theta='theta', line_close=True, title="Average Wins, Losess & Draws")

def get_team_statistics(df_bundes):
    radar_columns = ['GF','GC','Points']
    metrics = []
    for metric in radar_columns:
        metrics.append(df_bundes[metric].mean())
    
    return pd.DataFrame(dict(metrics=metrics, theta=radar_columns))

radar_fig_2 = px.line_polar(get_team_statistics(df_bundes), r='metrics', theta='theta', line_close=True, title="Average Point, Goals For and against")

radar_fig_1.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 25]
    )),
  showlegend=False
)

radar_fig_2.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 60]
    )),
  showlegend=False
)
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(radar_fig_1, use_container_width=True)
with col2:
    st.plotly_chart(radar_fig_2, use_container_width=True)

st.dataframe(df_bundes)
