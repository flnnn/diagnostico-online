import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class MedicoGPT:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


    def diagnosticar(self, sintomas):
        sintomas = ", ".join(sintomas)

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Você vai gerar um diagnóstico médico com base nos sintomas que o usuário te informou."
                },
                {
                    "role": "user",
                    "content": f"Meus sintomas são: {sintomas}"
                }
            ]
        )

        return completion.choices[0].message.content
    
