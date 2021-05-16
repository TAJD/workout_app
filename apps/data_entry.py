import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
import streamlit as st


URI_SQLITE_DB = "test.db"


def init_db(conn: Connection):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS exercises
        (
            name TEXT
            type TEXT
        );

        CREATE TABLE IF NOT EXISTS record
        (
            date TEXT
            
        )
        """
    )
    conn.commit()


if __name__ == "__main__":
    pass
