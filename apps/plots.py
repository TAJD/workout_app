import pandas as pd
import streamlit as st
import plotly.express as px
from utils import get_log

pd.options.display.float_format = "{:,.0f}".format


def app():
    st.markdown("# Plots ")
    workout = get_log()
    exercises = st.multiselect("Exercise", list(workout))
    if exercises:
        #
        for exercise in exercises:
            fig = px.scatter(x=workout[exercise].index, y=workout[exercise].values)
            fig.update_layout(
                # title="Plot Title",
                xaxis_title="Date",
                yaxis_title=exercise[0],
                font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
            )
            st.plotly_chart(fig)
