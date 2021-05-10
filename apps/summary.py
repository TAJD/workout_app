import pandas as pd
import streamlit as st
import plotly.express as px
from utils import prep_spreadsheet_data, quantity_per_week, load_volume, max_reps, weekly_total_table, get_log

pd.options.display.float_format = "{:,.0f}".format

# run the script to update from excel spreadsheet
weekly_totals = prep_spreadsheet_data()
perweek_movement_type = quantity_per_week(weekly_totals)

def app():
    st.markdown("## Weekly metrics")
    st.text("Sum of reps per exercise per week - the volume of each exercise per week.")
    # st.table(perweek_movement_type)
    fig_totals = px.bar(
        perweek_movement_type,
        x="WeekStartDate",
        y="value", # rename values to reps
        color="Movement type",
        barmode="group",
    )
    st.plotly_chart(fig_totals)

    # include table of values to see actual numbers
    st.markdown("## Weekly totals")
    st.table(weekly_total_table())

