import sqlite3


def get_conn():
    conn = sqlite3.connect("PyScriptRunner.db")
    conn.row_factory = sqlite3.Row
    return conn


def setup_db():
    with open("schema.sql", "r") as file:
        get_conn().executescript(file.read())
