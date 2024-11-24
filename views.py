from main import app
from flask import render_template, request, jsonify, redirect

from medicogpt.medico import MedicoGPT
from mapa.api_cep import consultar_cep, consultar_farmacias_raio

@app.route("/")
def home():
    return render_template("index.html", diagnostico=None)


@app.route("/llm", methods=["POST"])
def llm():
    if request.method == "POST":
        sintoma1 = request.form["sintoma1"]
        sintoma2 = request.form["sintoma2"]
        sintoma3 = request.form["sintoma3"]

        if not(sintoma1 and sintoma2 and sintoma3):
            return redirect("/")

        medico = MedicoGPT()
        resultado_diagnostico = medico.diagnosticar_doenca_stream([sintoma1, sintoma2, sintoma3])
        resultado_remedio = medico.buscar_remedio_comum(resultado_diagnostico)

        return render_template("index.html", diagnostico=resultado_diagnostico, remedio=resultado_remedio)
    

@app.route("/buscar", methods=["POST"])
def buscar():
    dados_request = request.get_json()
    cep = dados_request.get("cep")
    raio = dados_request.get("raio")
    cep = cep.replace(".", "").replace("-", "")

    dados_cep = consultar_cep(cep)
    latitude, longitude = float(dados_cep["latitude"]), float(dados_cep["longitude"])
    dados_farmacias = consultar_farmacias_raio(latitude, longitude, raio)
    farmacias = dados_farmacias["results"]

    if cep and raio:
        sucesso = True
    else:
        sucesso = False
    
    return jsonify({"success": sucesso, "coords": [latitude, longitude], "pharmacies": farmacias})

