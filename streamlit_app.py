import pandas as pd
import streamlit as st
import plotly.express as px
from utils import load_workout_spreadsheet

pd.options.display.float_format = "{:,.0f}".format

workout = load_workout_spreadsheet()
perweek = workout.groupby(workout["WeekStartDate"]).sum()

st.set_page_config(page_title="My Workouts")

st.title("My workouts")

st.markdown("## Weekly metrics")
st.text("Sum of reps per exercise per week - the volume of each exercise per week.")
st.table(perweek[["Pull ups", "Press ups", "Burpees"]])


st.markdown("## Plots ")
left_column, right_column = st.beta_columns(2)
with left_column:
    exercises = st.multiselect("Exercise", list(workout))

with right_column:
    if exercises:
        #  checkbox or dropdown to select graphs
        for exercise in exercises:
            fig = px.scatter(x=workout[exercise].index, y=workout[exercise].values)
            fig.update_layout(
                # title="Plot Title",
                xaxis_title="Date",
                yaxis_title=exercise[0],
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#7f7f7f"
                )
            )
            st.plotly_chart(fig)


st.markdown("## Max reps")
st.text("Maximum exercise values")
st.table(workout.max())
