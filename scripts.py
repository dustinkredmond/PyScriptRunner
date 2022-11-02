from db import get_conn
from flask import render_template, flash


def create_script(script_name, code):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO script (name, code) VALUES (?, ?)", (script_name, code))
    conn.commit()


def get_and_render_scripts():
    cursor = get_conn().cursor()
    scripts = cursor.execute("SELECT * FROM script").fetchall()
    return render_template("index.html", scripts=scripts)


def execute_script(id):
    conn = get_conn()
    cursor = conn.cursor()
    script = cursor.execute("SELECT * FROM script WHERE id = ?", (id,)).fetchone()
    conn.commit()
    # noinspection PyBroadException
    try:
        exec(script["code"])
        flash("Script executed successfully.")
    except Exception:
        flash("Script failed to execute successfully.")


def get_script(id):
    conn = get_conn()
    cursor = conn.cursor()
    script = cursor.execute("SELECT * FROM script WHERE id = ?", (id,)).fetchone()
    conn.commit()
    return script


def update_script(script_name, code, id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE script SET name = ?, code = ? WHERE id = ?", (script_name, code, id)
    )
    conn.commit()


def delete_script(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM script WHERE id = ?", (id,))
    conn.commit()
