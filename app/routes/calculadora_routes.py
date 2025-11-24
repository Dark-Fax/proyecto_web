from flask import Blueprint, render_template, request, session, redirect, url_for, flash
import math

calculadora = Blueprint("calculadora", __name__, url_prefix="/calculadora")


# === Mostrar la página ===
@calculadora.route("/")
def index():
    if "usuario_nombre" not in session:
        flash("Debes iniciar sesión", "warning")
        return redirect(url_for("usuarios.login"))

    return render_template("calculadora/calculadora.html", titulo_pagina="Calculadora 🧮")



# === Procesar los cálculos ===
@calculadora.route("/calcular", methods=["POST"])
def calcular():
    if "usuario_nombre" not in session:
        flash("Debes iniciar sesión", "warning")
        return redirect(url_for("usuarios.login"))

    try:
        # === Datos requeridos ===
        autonomia_km = float(request.form["autonomia"])

        # === Datos opcionales con default ===
        bateria_kWh = request.form.get("bateria_kwh")
        distancia_km = request.form.get("distancia")
        precio_kWh = request.form.get("precio_kwh")

        bateria_kWh = float(bateria_kWh) if bateria_kWh else 65      # default
        distancia_km = float(distancia_km) if distancia_km else 100   # default
        precio_kWh = float(precio_kWh) if precio_kWh else 15          # default

        # Opcionales: tasa de carga
        km_carga = request.form.get("km_carga")
        min_carga = request.form.get("min_carga")

        km_carga = float(km_carga) if km_carga else None
        min_carga = float(min_carga) if min_carga else None

        if km_carga and min_carga:
            rate_km_min = km_carga / min_carga
        else:
            rate_km_min = 160 / 30

        # === Cálculos ===

        # Cargas equivalentes necesarias
        cargas_totales = math.ceil(distancia_km / autonomia_km)

        # Si empieza cargado, restar 1
        recargas_necesarias = max(0, cargas_totales - 1)

        # Energía por km
        energia_por_km = bateria_kWh / autonomia_km

        # Energía total
        energia_total = energia_por_km * distancia_km

        # Tiempo total estimado de recarga
        # Solo se usa la distancia que requiere recarga, NO la carga inicial
        km_recargados = max(0, distancia_km - autonomia_km)
        tiempo_min_total = km_recargados / rate_km_min
        tiempo_horas = tiempo_min_total / 60

        # Costo total
        costo_total = energia_total * precio_kWh

        # === Empaquetar resultados ===
        resultados = {
            "autonomia": autonomia_km,
            "bateria_kwh": bateria_kWh,
            "distancia": distancia_km,
            "cargas_totales": cargas_totales,
            "recargas_necesarias": recargas_necesarias,
            "energia_total": round(energia_total, 2),
            "tiempo_minutos": round(tiempo_min_total, 2),
            "tiempo_horas": round(tiempo_horas, 2),
            "costo_total": round(costo_total, 2),
            "precio_kwh": precio_kWh
        }

        return render_template("calculadora/calculadora.html", resultados=resultados, titulo_pagina="Calculadora 🧮")

    except Exception as e:
        flash(f"Error al procesar los datos: {str(e)}", "danger")
        return redirect(url_for("calculadora.index"))
