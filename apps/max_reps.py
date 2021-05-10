import pandas as pd
import streamlit as st
import plotly.express as px
from utils import (
    max_reps
)

pd.options.display.float_format = "{:,.0f}".format

def app():
    st.markdown("# Max reps")
    st.text("Maximum exercise values")
    exercise_max_reps = max_reps()
    st.table(exercise_max_reps)
