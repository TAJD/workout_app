import streamlit as st
from multiapp import MultiApp

from apps import summary, plots, max_reps

app = MultiApp()

st.set_page_config(page_title="My Workouts")

st.markdown(
    """
# My Workouts

"""
)

# Add all your application here
app.add_app("Summary", summary.app)
app.add_app("Plots", plots.app)
app.add_app("Max reps", max_reps.app)
# The main app
app.run()
