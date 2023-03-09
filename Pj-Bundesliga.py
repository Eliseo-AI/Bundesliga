import streamlit as st
import pandas as pd
import plotly.express as px

df_bundes = pd.read_csv('data/Bundesliga.csv')

unique_values = sorted(set(df_bundes["Club"].unique()) | set(df_bundes["Season"].unique()))

selected_values = st.sidebar.multiselect("Select values", unique_values)

filtered_df = df_bundes[(df_bundes["Club"].isin(selected_values)) | (df_bundes["Season"].isin(selected_values))]

st.title("Bundesliga")
st.subheader("Analysis")

total_clubs = len(df_bundes)
Average_Points = df_bundes["Points"].mean()
Average_Goals = df_bundes["GF"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Club", f"{total_clubs:,.0f}")
col2.metric("Pts", f"{Average_Points:,.2f}")
col3.metric("GF", f"{Average_Goals:,.2f}")



def get_team_statistics(df_bundes):
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
