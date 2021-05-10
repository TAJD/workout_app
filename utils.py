import numpy as np
import pandas as pd
import datetime as dt


def excel_to_csv_tables() -> None:
    # handle the absence of the excel file when uploaded to server
    try:
        workout_excel = pd.ExcelFile("workout.xlsx")
        df_reps = workout_excel.parse("exercise_volume_2")
        df_exercises = workout_excel.parse("exercises")
        df_reps.to_csv("volume.csv", index=False)
        df_exercises.to_csv("exercises.csv", index=False)
    except:
        print("Error loading spreadsheet. Existing data used.")


def load_volume(fname: str) -> pd.DataFrame:
    df = pd.read_csv(fname)
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df["WeekStartDate"] = df.apply(
        lambda row: row["Date"] - dt.timedelta(days=row["Date"].weekday()), axis=1
    )
    # df = df.set_index("Date")
    df = df.replace(np.nan, 0)
    return df


def load_exercises(fname: str) -> pd.DataFrame:
    df = pd.read_csv(fname)
    return df


def get_log() -> pd.DataFrame:
    df_reps = load_volume("volume.csv")
    return df_reps


def prep_spreadsheet_data() -> pd.DataFrame:
    excel_to_csv_tables()
    df_reps = load_volume("volume.csv")
    reshaped_reps = df_reps.melt(id_vars=["Date", "WeekStartDate"])
    df_exercises = load_exercises("exercises.csv")
    df_join = pd.merge(
        reshaped_reps,
        df_exercises,
        how="inner",
        left_on="variable",
        right_on="Exercise",
    )
    df_join = df_join.set_index("Date")
    df_join = df_join.drop(columns=["variable"])
    return df_join


def quantity_per_week(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(["WeekStartDate", "Movement type"]).sum()
    df = df.drop(columns=["Exercise"])
    df = df.reset_index()
    df = df.rename({"value": "Reps"})
    return df


def max_reps() -> pd.DataFrame:
    exercises = load_volume("volume.csv")
    exercises = exercises.drop(columns=["Date", "WeekStartDate"])
    max_vals = exercises.max()
    max_vals = max_vals.rename("Reps")
    return max_vals


def weekly_total_table() -> pd.DataFrame:
    df = prep_spreadsheet_data()
    weekly_totals = quantity_per_week(df)
    reshaped_weekly_totals = weekly_totals.pivot(
        index="WeekStartDate", columns="Movement type", values="value"
    )
    return reshaped_weekly_totals


if __name__ == "__main__":
    df = weekly_total_table()
    print(df)
