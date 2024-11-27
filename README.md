# Diagnóstico Online 🤖

Este é um projeto de diagnóstico assistido por IA. O projeto foi desenvolvido para ajudar o usuário a entender melhor os sintomas que está experienciando. O funcionamento será mediante o usuário informando os sintomas que está sentindo, então uma Inteligência Artificial (ChatGPT) irá analisar as informações fornecidas e sugerir possíveis doenças associadas e fará também a recomendação de remédio para o tratamento. Além disso, também será possível localizar farmácias próximas para a compra do remédio recomendado.


# Objetivos ✔️

O objetivo do projeto é fornecer um recurso acessível e de fácil uso, promovendo a conscientização sobre a saúde e ajuda aos usuários a tomarem decisões mais informadas. Tudo isso utilizando de soluções de Inteligência Artificial baseada em LLMs (Large Language Models), como o ChatGPT e testes da aplicação com os conhecimentos adquiridos na disciplina de Teste de Software.


# Realização 👷

Este é um trabalho em conjunto para a disciplina de Projeto Integrador IV.

Responsáveis:
- Felipe Leoncio Nunes
- Gabriel dos Santos
- Guilherme Barbosa
- Guilherme Guimarães
- João Victor Leoni


# Rodando a Aplicação 🆙
1 - Tenha o docker disponível em sua máquina.

2 - Clone este repositório e acesse-o.

3 - Execute o comando: `docker build --tag diagnostico-online .`

4 - Antes de executar a aplicação configure o arquivo .env disponível com as chaves APIs necessárias.

5 - Então execute: `docker --env-file .env -d -p 5000:5000 diagnostico-online`

#### [!] É importante ressaltar que esse comando está sendo executado com o usuário no grupo "docker" no linux, logo não se faz necessário o uso de "sudo".
#### [!] Caso não seja o seu caso, use "sudo" antes do comando mostrado.
---

### Observações a respeito das chaves APIs:
- TOKEN_API: É necessário criar uma conta em https://www.cepaberto.com/, a API é gratuita.
- PLACES_API: Uma conta no Google é necessária. Documentação para o recurso usado: https://developers.google.com/maps/documentation/places/web-service/migrate-nearby.
- OPENAI_API_KEY: Conta na OpenAI necessária, a API não é gratuita.

*"Uma longa viagem começa por um passo."* - Provérbio Chinês
