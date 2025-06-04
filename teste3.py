import requests
from urllib.parse import urlencode
from config import login, senha

# URL para autenticação
url_auth = "https://sinapses-backend.ia.pje.jus.br/rest/usuario/autenticarUsuario"

# URL da API para a chamada seguinte
url_api = "https://sinapses-backend.ia.pje.jus.br/rest/modelo/executarServico/%2Ftrf2/GEN_IA_REVISOR_INTELIGENTE_CSF/2"

# Payload para autenticação
payload_auth = {
    "login": login,
    "senha": senha
}

# Cabeçalhos para a requisição
headers_auth = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Fazendo a chamada POST para autenticação
response_auth = requests.post(url_auth, data=urlencode(payload_auth), headers=headers_auth)

if response_auth.status_code == 200:

    token = response_auth.text
    print("Token recebido:", token)
else:
    print("Falha na autenticação: Status Code", response_auth.status_code)
    print("Detalhes:", response_auth.text)


# Montando o payload para o modelo
payload_api = {
  "classe": {
    "tipo": "TEXTO_PURO",
    "conteudo": "Procedimento do Juizado Especial Cível"
  },
  "assunto": {
    "tipo": "TEXTO_PURO",
    "conteudo": "Pensão por Morte (Art. 74/9)"
  },
  "numeroProcesso": {
    "tipo": "TEXTO_PURO",
    "conteudo": "50013586020254025103"
  },
  "movimentos": [
    {
      "codigo": {
        "tipo": "TEXTO_PURO",
        "conteudo": "26"
      },
      "nome": {
        "tipo": "TEXTO_PURO",
        "conteudo": "Distribuição"
      },
      "dataHora": {
        "tipo": "TEXTO_PURO",
        "conteudo": "2025-02-26T13:02:29.000Z"
      }
    },
    {
      "codigo": {
        "tipo": "TEXTO_PURO",
        "conteudo": "12164"
      },
      "nome": {
        "tipo": "TEXTO_PURO",
        "conteudo": "Outras Decisões"
      },
      "dataHora": {
        "tipo": "TEXTO_PURO",
        "conteudo": "2025-03-10T18:09:31.000Z"
      }
    },
    {
      "codigo": {
        "tipo": "TEXTO_PURO",
        "conteudo": "11010"
      },
      "nome": {
        "tipo": "TEXTO_PURO",
        "conteudo": "Mero expediente"
      },
      "dataHora": {
        "tipo": "TEXTO_PURO",
        "conteudo": "2025-03-21T17:25:24.000Z"
      }
    },
    {
      "codigo": {
        "tipo": "TEXTO_PURO",
        "conteudo": "11010"
      },
      "nome": {
        "tipo": "TEXTO_PURO",
        "conteudo": "Mero expediente"
      },
      "dataHora": {
        "tipo": "TEXTO_PURO",
        "conteudo": "2025-03-25T21:20:27.000Z"
      }
    },
    {
      "codigo": {
        "tipo": "TEXTO_PURO",
        "conteudo": "898"
      },
      "nome": {
        "tipo": "TEXTO_PURO",
        "conteudo": "Por decisão judicial"
      },
      "dataHora": {
        "tipo": "TEXTO_PURO",
        "conteudo": "2025-03-26T23:19:27.000Z"
      }
    },
    {
      "codigo": {
        "tipo": "TEXTO_PURO",
        "conteudo": "12067"
      },
      "nome": {
        "tipo": "TEXTO_PURO",
        "conteudo": "Levantamento da Suspensão ou Dessobrestamento"
      },
      "dataHora": {
        "tipo": "TEXTO_PURO",
        "conteudo": "2025-04-30T18:33:56.000Z"
      }
    }
  ]
}

# Cabeçalhos para a requisição com o token
headers_api = {
    "Authorization": f"Bearer {token}",
    "accept": "application/json",
    "Content-Type": "application/json"
}

# Fazendo a chamada POST para a API
response_api = requests.post(url_api, json=payload_api, headers=headers_api)

if response_api.status_code == 200:
    # Processando a resposta
    resposta_api = response_api.json()
    print("Resposta da API:", resposta_api)
else:
    print("Falha na chamada da API: Status Code", response_api.status_code)
    print("Detalhes:", response_api.text)
