import numpy as np
import pandas as pd
import datetime as dt


def load_workout_spreadsheet() -> pd.DataFrame:
    workout_excel = pd.ExcelFile("workout.xlsx")
    df = workout_excel.parse("exercise_volume_2")
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df["WeekStartDate"] = df.apply(
        lambda row: row["Date"] - dt.timedelta(days=row["Date"].weekday()), axis=1
    )
    df = df.set_index("Date")
    df = df.replace(np.nan, 0)
    return df
