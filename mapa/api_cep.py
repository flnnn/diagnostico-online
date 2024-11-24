import requests
import os
from dotenv import load_dotenv

load_dotenv()

def consultar_cep(cep):
    url = f"https://www.cepaberto.com/api/v3/cep?cep={cep}"
    token = os.getenv("TOKEN_API")
    headers = {'Authorization': f'Token token={token}'}
    response = requests.get(url, headers=headers)
    return response.json()


def consultar_farmacias_raio(latitude, longitude, raio):
    key = os.getenv("PLACES_API")

    # raio de 5km (5000m => "&radius=5000")
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={raio}&type=pharmacy&key={key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro ao fazer a requisição. Status code: {response.status_code}")

