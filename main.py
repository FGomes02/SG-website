from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main-page.html")

@app.route("/servicos")
def services_page():
    return render_template("services-page.html")

@app.route("/portfolio")
def portfolio_page():
    return render_template("portfolio-page.html")

@app.route("/contactos")
def contacts_page():
    return render_template("contacts-page.html")