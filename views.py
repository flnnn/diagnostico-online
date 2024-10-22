from main import app
from flask import render_template
from flask import request

from medicogpt.medico import MedicoGPT

@app.route("/")
def home():
    return render_template("index.html", diagnostico=None)


@app.route("/llm", methods=["POST"])
def llm():
    if request.method == "POST":
        sintoma1 = request.form["sintoma1"]
        sintoma2 = request.form["sintoma2"]
        sintoma3 = request.form["sintoma3"]

        medico = MedicoGPT()
        resultado_diagnostico = medico.diagnosticar([sintoma1, sintoma2, sintoma3])

        return render_template("index.html", diagnostico=resultado_diagnostico)
