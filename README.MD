# Zendesk Ticket Fetcher

Este projeto demonstra como realizar uma requisição segura à API do Zendesk para obter detalhes de um ticket específico.  
O script utiliza Python com conexão HTTPS, autenticação via API Token e variáveis de ambiente para manter as credenciais seguras.

## Funcionalidades
- Conexão segura com o Zendesk usando `ssl` e `certifi`.
- Autenticação via Basic Auth com email e token.
- Carregamento de credenciais a partir de um arquivo `.env`.
- Consulta de um ticket específico pelo seu ID.
- Exibição dos principais campos do ticket em formato legível.

## Estrutura do Projeto
.
├── script.py        # Código principal para buscar ticket
├── .env             # Arquivo com variáveis de ambiente
├── requirements.txt # Dependências do projeto
└── README.md        # Documentação


## Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/zendesk-ticket-fetcher.git
   cd zendesk-ticket-fetcher

ZENDESK_SUBDOMAIN=seu_subdominio
ZENDESK_EMAIL=seu_email
ZENDESK_API_TOKEN=seu_token

pip install -r requirements.txt

Fazendo requisição para: https://SEU_SUBDOMINIO.zendesk.com/api/v2/tickets/101.json

===== Detalhes do Ticket Zendesk =====
ID: 101
Criado em: 2026-06-24T12:00:00Z
Atualizado em: 2026-06-24T12:05:00Z
Status: open
Prioridade: high
Assunto: Exemplo de Ticket
Descrição: Este é um ticket de teste
Solicitante ID: ID_DO_SOLICITANTE
Responsável ID: ID_DO_RESPONSAVEL
Tags: LISTA_DE_TAGS
Nome do Cliente: NOME_DO_CLIENTE
CPF: CPF_DO_CLIENTE



