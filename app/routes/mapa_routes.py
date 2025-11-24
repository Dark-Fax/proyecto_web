from flask import Blueprint, render_template, session, flash, redirect, url_for
import requests
import os

mapa = Blueprint("mapa", __name__, url_prefix="/mapa")

@mapa.route("/")
def index():
    if "usuario_nombre" not in session:
        flash("Debes iniciar sesión", "warning")
        return redirect(url_for("usuarios.login"))

    url = "https://api.openchargemap.io/v3/poi/"

    params = {
        "output": "json",
        "countrycode": "CO",
        "latitude": 4.7110,
        "longitude": -74.0721,
        "distance": 20,
        "distanceunit": "KM",
        "maxresults": 200
    }

    # API KEY en headers (obligatorio)
    headers = {
        "X-API-Key": os.getenv("API_OCM_KEY"),
        "Content-Type": "application/json"
    }

    print("API KEY DETECTADA EN FLASK:", os.getenv("API_OCM_KEY"))
    response = requests.get(url, params=params, headers=headers)

    print("STATUS CODE:", response.status_code)
    print("RESPONSE TEXT:", response.text[:500])

    try:
        estaciones = response.json()
        print("ESTACIONES ENCONTRADAS:", len(estaciones))
    except Exception as e:
        print("ERROR AL DECODIFICAR JSON:", e)
        estaciones = []

    return render_template("mapa/mapa.html", estaciones=estaciones, titulo_pagina="Mapa de Estaciones🗺️")
