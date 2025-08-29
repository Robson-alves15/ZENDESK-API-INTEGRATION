import http.client
import ssl
import certifi
import json
from base64 import b64encode
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv(dotenv_path=".env")

# Informações básicas
subdomain = os.getenv("ZENDESK_SUBDOMAIN") 
email = os.getenv("ZENDESK_EMAIL")
api_token = os.getenv("ZENDESK_API_TOKEN")

# ID do ticket desejado
ticket_id = 101
url_path = f"/api/v2/tickets/{ticket_id}.json"
full_url = f"https://{subdomain}.zendesk.com{url_path}"
print(f"Fazendo requisição para: {full_url}")

# SSL seguro 
context = ssl.create_default_context()
context.load_verify_locations(cafile=certifi.where())

# Conexão HTTPS com o Zendesk
conn = http.client.HTTPSConnection(f"{subdomain}.zendesk.com", context=context)

# Cabeçalho de autenticação
auth_value = f"{email}/token:{api_token}"
encoded_auth = b64encode(auth_value.encode("utf-8")).decode("utf-8")

headers = {
    "Authorization": f"Basic {encoded_auth}"
}

# Enviar requisição
conn.request("GET", url_path, headers=headers)

# Obter resposta
response = conn.getresponse()

if response.status == 200:
    data = json.loads(response.read().decode())
    ticket = data.get("ticket", {})

    # Filtrar campos relevantes usando placeholders
    filtered_data = {
        "ID": ticket.get("id"),
        "Criado em": ticket.get("created_at"),
        "Atualizado em": ticket.get("updated_at"),
        "Status": ticket.get("status"),
        "Prioridade": ticket.get("priority"),
        "Assunto": ticket.get("subject"),
        "Descrição": ticket.get("description"),
        "Solicitante ID": "ID_DO_SOLICITANTE",
        "Responsável ID": "ID_DO_RESPONSAVEL",
        "Tags": "LISTA_DE_TAGS",
        "Nome do Cliente": "NOME_DO_CLIENTE",
        "CPF": "CPF_DO_CLIENTE",
    }

    # Exibir os dados do ticket
    print("\n===== Detalhes do Ticket Zendesk =====")
    for key, value in filtered_data.items():
        print(f"{key}: {value}")

else:
    print(f"Erro ao acessar a API. Status Code: {response.status}")

# Fechar conexão
conn.close()
