import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class MedicoGPT:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    
    def diagnosticar_doenca_stream(self, sintomas):
        prompt = f"Qual a doença mais comum para os sintomas a seguir: {sintomas}. Responda apenas com o nome da doença."
        
        stream = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        
        resposta_completa = ""

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                # print(content, end="")  # debug
                resposta_completa += content
        
        return resposta_completa
    
    
    def buscar_remedio_comum(self, doenca):
        prompt = f"Qual o remédio mais comum para tratar a doença: {doenca}? Responda apenas com o nome do remédio."
        
        stream = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        
        resposta_completa = ""

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                # print(content, end="")  # debug
                resposta_completa += content
        
        return resposta_completa
