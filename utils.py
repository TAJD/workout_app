import numpy as np
import pandas as pd
import datetime as dt

def excel_to_csv_tables() -> None:
   workout_excel = pd.ExcelFile("workout.xlsx")
   df_reps = workout_excel.parse("exercise_volume_2")
   df_exercises = workout_excel.parse("exercises")
   df_reps.to_csv("volume.csv", index=False)
   df_exercises.to_csv("exercises.csv", index=False)


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
    df_join = df_join.drop(columns=['variable'])
    return df_join


if __name__ == "__main__":
    df = prep_spreadsheet_data()
    print(df.head())