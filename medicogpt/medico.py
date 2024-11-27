import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def diagnosticar_doenca_stream(sintomas):
    # Monta o prompt a ser enviado à API
    prompt = f"Qual a doença mais comum para os sintomas a seguir: {sintomas}. Responda apenas com o nome da doença."
    
    # Modelo de chamada da API igual na doc da openai
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    
    # Variável para armazenar a resposta final
    resposta_completa = ""

    # Não sei pq do for mas na doc da openai ta assim
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            print(content, end="")  # Exibe a resposta em tempo real
            resposta_completa += content  # Armazena a resposta completa
    
    # Retorna resposta
    return resposta_completa

def buscar_remedio_comum(doenca):
    # Prompt para obter remédio
    prompt = f"Qual o remédio mais comum para tratar a doença: {doenca}? Responda apenas com o nome do remédio."
    
    # Modelo de chamada da API igual na doc da openai
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    
    # Variável para armazenar a resposta final
    resposta_completa = ""

    # Não sei pq do for mas na doc da openai ta assim
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            print(content, end="") 
            resposta_completa += content
    
    # Retorna a resposta final completa
    return resposta_completa

if __name__ == "__main__":
    # Input dos sintomas
    sintomas_usuario = input("Informe os sintomas (ex: febre, dor de cabeça, cansaço): ")
    
    # Chama a função que já consultou na API
    doenca = diagnosticar_doenca_stream(sintomas_usuario)
    
    # Resposta
    print(f"\nA doença mais comum para os sintomas informados é: {doenca}")

    # Chama a função para buscar o remédio mais comum para a doença diagnosticada
    remedio = buscar_remedio_comum(doenca)
    
    # Exibe o remédio comum para a doença
    print(f"\nO remédio mais comum para a doença {doenca} é: {remedio}")
