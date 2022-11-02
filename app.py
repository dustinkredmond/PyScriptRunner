import secrets

from flask import Flask, flash, render_template, request

from db import get_conn, setup_db
from scripts import (create_script, delete_script, execute_script,
                     get_and_render_scripts, get_script, update_script)

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=secrets.token_hex())
setup_db()


@app.route("/")
def index():
    return get_and_render_scripts()


@app.route("/add")
def add():
    return render_template("add.html")


@app.post("/new_script")
def new_script():
    script_name = request.form["script_name"]
    code = request.form["code"]
    error = None

    if not script_name:
        error = True
        flash("Script name is required.")
    if not code:
        error = True
        flash("Code cannot be blank.")

    if not error:
        create_script(script_name, code)
        return get_and_render_scripts()
    else:
        return render_template("add.html", script_name=script_name, code=code)


@app.route("/execute/<int:id>")
def execute(id):
    execute_script(id)
    return get_and_render_scripts()


@app.route("/edit/<int:id>")
def edit(id):
    script = get_script(id)
    return render_template("edit.html", script=script)


@app.post("/edit_script/<int:id>")
def edit_script(id):
    script_name = request.form["script_name"]
    code = request.form["code"]
    error = None

    if not script_name:
        error = True
        flash("Script name is required.")
    if not code:
        error = True
        flash("Code cannot be blank.")

    if not error:
        update_script(script_name, code, id)
        return get_and_render_scripts()
    else:
        script = get_script(id)
        return render_template("edit.html", script=script)


@app.route("/delete/<int:id>")
def delete(id):
    delete_script(id)
    return get_and_render_scripts()


if __name__ == "__main__":
    app.run()
