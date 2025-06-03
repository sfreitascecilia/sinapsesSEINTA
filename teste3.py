import requests
from urllib.parse import urlencode
from config import login, senha

# URL para autenticação
url_auth = "https://sinapses-backend.ia.pje.jus.br/rest/usuario/autenticarUsuario"

# URL da API para a chamada seguinte
url_api = "https://sinapses-backend.ia.pje.jus.br/rest/modelo/executarServico/%2Ftrf2/GEN_TRN2024_CSF_SUMARIZACAO/3"

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

# Substitua com o texto desejado
# PET VER
#conteudo = "RVhDRUxFTlTDjVNTSU1PIFNFTkhPUiBET1VUT1IgSlVJWiBERSBESVJFSVRPIERPIF9fX18gSlVJWkFETyBFU1BFQ0lBTCBDw41WRUwgREEKQ0lSQ1VOU0NSScOHw4NPIEpVRElDScOBUklBIERFIF9fX19fX19fX19fX19fX19fX19fX19fX19fIC0gREYKIChGw7NydW0gY29tcGV0ZW50ZSAvIENpZGFkZSkKT1UKRVhDRUxFTlTDjVNTSU1PIFNFTkhPUiBET1VUT1IgSlVJWiBERSBESVJFSVRPIERPIEpVSVpBRE8gRVNQRUNJQUwgREEgRkFaRU5EQQpQw5pCTElDQSBETyBERgotLS01IExJTkhBUyAtLS0KUEFSVEUgUkVRVUVSRU5URTogX19fX19fX19fX19fX19fX19fX19fX19fX18sIG5hY2lvbmFsaWRhZGU6IF9fX19fX19fX19fX19fXywgZXN0YWRvCmNpdmlsOiBfX19fX19fX18sIHByb2Zpc3PDo286IF9fX19fX19fX18sIGZpbGlhw6fDo286IF9fX19fX19fX18sIHBvcnRhZG9yIGRhIENhcnRlaXJhIGRlCklkZW50aWRhZGUgbsK6OiBfX19fX19fX19fLCDDs3Jnw6NvIGV4cGVkaWRvci9VRjogX19fX19fX18sIGRhdGEgZGEgZXhwZWRpw6fDo286IF9fX19fX19fLAppbnNjcml0byBubyBDUEYgc29iIG8gbsK6OiBfX19fX19fXywgcmVzaWRlbnRlIGUgZG9taWNpbGlhZG8gbmEgX19fX19fX18sIENpZGFkZTogX19fX19fX18sCkNFUDogX19fX19fX18sIHRlbGVmb25lKHMpOiBfX19fX19fXywgV2hhdHNBcHA6IF9fX19fX19fLCBlLW1haWw6IF9fX19fX19fLCB2ZW0sIMOgIHByZXNlbsOnYQpkZSBWb3NzYSBFeGNlbMOqbmNpYSwgcHJvcG9yIGEgcHJlc2VudGUKQcOHw4NPIERFIF9fX19fX19fX19fX19fX18gb3UgKGVzY3JldmEg4oCcQ09OSEVDSU1FTlRP4oCdKQplbSBmYWNlIGRhIFBBUlRFIFJFUVVFUklEQTogX19fX19fX18sIG5hY2lvbmFsaWRhZGU6IF9fX19fX19fLCBlc3RhZG8gY2l2aWw6IF9fX19fX19fLApwcm9maXNzw6NvOiBfX19fX19fXywgZmlsaWHDp8OjbzogX19fX19fX18sIHBvcnRhZG9yIGRhIENhcnRlaXJhIGRlIElkZW50aWRhZGUgbsK6OiBfX19fX19fXywKw7NyZ8OjbyBleHBlZGlkb3IvVUY6IF9fX19fX19fLCBkYXRhIGRhIGV4cGVkacOnw6NvOiBfX19fX19fXywgaW5zY3JpdG8gbm8gQ1BGIHNvYiBvIG7CujoKX19fX19fX18sIHJlc2lkZW50ZSBlIGRvbWljaWxpYWRvIG5hIF9fX19fX19fLCBDaWRhZGU6IF9fX19fX19fLCBDRVA6IF9fX19fX19fLCB0ZWxlZm9uZShzKToKX19fX19fX18sIFdoYXRzQXBwOiBfX19fX19fXywgZS1tYWlsOiBfX19fX19fXywgcGVsYXMgcmF6w7VlcyBkZSBmYXRvIGEgc2VndWlyIGFkdXppZGFzLgpPVSwgc2UgZm9yIHBlc3NvYSBqdXLDrWRpY2EKZW0gZmFjZSBkYSBwYXJ0ZSBSRVFVRVJJREE6IF9fX19fX19fLCBwZXNzb2EganVyw61kaWNhIGRlIGRpcmVpdG8gcHJpdmFkbywgaW5zY3JpdGEgbm8gQ05QSgpzb2IgbyBuwrogX19fX19fX18sIGNvbSBlbmRlcmXDp286IF9fX19fX19fLCBDaWRhZGU6IF9fX19fX19fICwgQ0VQOiBfX19fX19fXywgZW0KZGVjb3Jyw6puY2lhIGRvcyBtb3Rpdm9zIGRlIGZhdG8gYSBzZWd1aXIgYWR1emlkb3MuClJFU1VNTyBET1MgRkFUT1MKKENvbnRhciByZXN1bWlkYW1lbnRlIG9zIGZhdG9zIHF1ZSBtb3RpdmFtIHN1YSBpbnRlbsOnw6NvIGRlIGFicmlyIHVtYSBhw6fDo28gZW0gZGVzZmF2b3IgZGEKcGFydGUgY29udHLDoXJpYSwgc2VtcHJlIHF1ZSBwb3Nzw612ZWwgZW0gb3JkZW0gY3Jvbm9sw7NnaWNhIGUgYSBjYWRhIHNpdHVhw6fDo28gY2l0YWRhIGluZm9ybWFyCmRhdGEsIGRhZG9zIGRlIGNvbnRyYXRvLCBwcm90b2NvbG9zLCBCTywgZXRjLCBzZW1wcmUgc2UgYmFzZWFuZG8gZW0gcHJvdmFzIGRvY3VtZW50YWlzIGVtCmFuZXhvIGUvb3UgdGVzdGVtdW5oYWlzIGEgc2VyIGFwcmVzZW50YWRhIGVtIGp1w616by4uLiBlbmZpbSBuw6NvIGjDoSB1bSByaWdvciBuYSBsaW5ndWFnZW0KanVyw61kaWNhLi4uIGFwZW5hcyBjb250YXIgZGUgbW9kbyBzaW1wbGVzIGUgbMOzZ2ljbyBvIHF1ZSBhY29udGVjZXUsIHRlbnRhdGl2YXMgZGUgcmVzb2x2ZXIgbwpwcm9ibGVtYSBlIHN1YSBpbnRlbsOnw6NvIGNvbSBlc3RhIGHDp8OjbykKUEVESURPUwpGYWNlIGFvIGV4cG9zdG8sIHJlcXVlcjoKYSkgYSBjaXRhw6fDo28gZGEgcGFydGUgcmVxdWVyaWRhIGRhIHByZXNlbnRlIGHDp8OjbywgYmVtIGNvbW8gc2VqYSBpbnRpbWFkYSBhIGNvbXBhcmVjZXIKcGVzc29hbG1lbnRlIMOgIGF1ZGnDqm5jaWEgZGUgY29uY2lsaWHDp8OjbywgY3VqbyBuw6NvIGNvbXBhcmVjaW1lbnRvIGltcG9ydGEgZW0gcGVuYSBkZQpyZXZlbGlhOwpiKSBhIHByb2NlZMOqbmNpYSBkbyhzKSBwZWRpZG9zIHBhcmEgY29uZGVuYXIgYSBwYXJ0ZSByZXF1ZXJpZGEgw6AgKGV4LjogcGFnYXIgYSBxdWFudGlhIGRlIFIkLApmYXplciBkZXRlcm1pbmFkYSBvYnJpZ2HDp8OjbywgZXRjKS4gU2UgaG91dmVyIG1haXMgZGUgdW0gcGVkaWRvLCBzw7MgY3JpYXIgbWFpcyB1bSBpdGVtIC4uLiBjKQpWQUxPUiBEQSBDQVVTQQpBdHJpYnVpLXNlIMOgIGNhdXNhIG8gdmFsb3IgZGUgUiQgX19fX19fX19fXy4gKE8gdmFsb3IgZGV2ZSBjb3JyZXNwb25kZXIgYSBzb21hIGRvcyB2YWxvcmVzIGRlIHRvZG9zIG9zIHBlZGlkb3MuCkNhc28gbsOjbyBoYWphIHBlZGlkbyBkZSBjdW5obyBlY29uw7RtaWNvLCBwb2RlIHV0aWxpemFyIG8gdmFsb3Igc2ltYsOzbGljbyBkZSBSJCAxMDAsMDApCkxPQ0FMLCBEQVRBIGUgQVNTSU5BVFVSQS4g"

# PET FALSA
# conteudo = "RVhDRUxFTlTDjVNTSU1PIFNFTkhPUiBET1VUT1IgSlVJWiBERSBESVJFSVRPIERPIF9fX18gSlVJWkFETyBFU1BFQ0lBTCBDw41WRUwgREEKQ0lSQ1VOU0NSScOHw4NPIEpVRElDScOBUklBIERFIF9fX19fX19fX19fX19fX19fX19fX19fX19fIC0gREYKIChGw7NydW0gY29tcGV0ZW50ZSAvIENpZGFkZSkKT1UKRVhDRUxFTlTDjVNTSU1PIFNFTkhPUiBET1VUT1IgSlVJWiBERSBESVJFSVRPIERPIEpVSVpBRE8gRVNQRUNJQUwgREEgRkFaRU5EQQpQw5pCTElDQSBETyBERgoKU0VHVUUgRU0gQU5FWE8="
# Substitua com o número desejado
#quantidadeClasses = 2

# Texto para o modelo GEN_TRN2024_CSF_SUMARIZACAO
conteudo = '''
    ACÓRDÃO
    Vistos, relatados e discutidos os autos em que são partes as acima indicadas, acordam os Ministros da Segunda Turma do Superior Tribunal de Justiça, por unanimidade, não conhecer do agravo interno, nos termos do voto do(a) Sr(a). Ministro(a)-Relator(a)." Os Srs. Ministros Herman Benjamin, Og Fernandes, Mauro Campbell Marques e Assusete Magalhães votaram com o Sr. Ministro Relator.
    RELATÓRIO
    O EXMO. SR. MINISTRO FRANCISCO FALCÃO (Relator):
    Na origem, cuida-se de agravo de instrumento interposto pelo Município de Fronteira contra decisão judicial que acolheu parcialmente o incidente de impugnação ao valor da causa para retificar o valor dado aos embargos à execução.
    No Tribunal de Justiça do Estado de Minas Gerais, a decisão judicial foi mantida em acórdão assim ementado:
    AGRAVO DE INSTRUMENTO - EMBARGOS À EXECUÇÃO - IMPUGNAÇÃO AO VALOR DA CAUSA - PRELIMINARES - AUSÊNCIA DE INTERESSE RECURSAL - DECISÃO ULTRA PETITA - REJEITADAS - ALEGAÇÃO DE OBRIGAÇÃO ILÍQUIDA - RECURSO DESPROVIDO
    1. O interesse recursal se traduz no binômio necessidade/utilidade do provimento jurisdicional solicitado.
    2. O valor da causa nos embargos à execução deve guardar consonância com o proveito econômico perseguido pelo embargante.
    O Município de Fronteira interpôs recurso especial com fundamento no art; 105, III, a, da Constituição Federal por ofensa ao art. 535, II, do CPC/73, cujo seguimento foi obstado pelo Tribunal de origem, ensejando a interposição de agravo nos próprios autos.
    Recebidos os autos pelo Superior Tribunal de Justiça, negou-se provimento ao recurso especial diante da ausência de violação do art. 535, II, do CPC/73.
    Foi interposto o presente agravo interno contra essa decisão.
    É o relatório.
    VOTO
    O EXMO. SR. MINISTRO FRANCISCO FALCÃO (Relator):
    O recurso não merece ser conhecido.
    A decisão recorrida, objeto deste agravo interno, foi disponibilizada no Diário de Justiça eletrônico em 18/10/2018 (quinta-feira), considerando-se publicada em 19/10/2018 (sexta-feira), certidão à fl. 405.
    Assim sendo, a contagem do prazo de 30 dias úteis para interposição do agravo interno, nos termos do art. 1.070 c/c o art. 183 do CPC/2015, iniciou-se em 22/10/2018 (segunda-feira) - primeiro dia útil após a data de publicação -, encerrando-se no dia 5/12/2018 (quarta-feira), conforme certidão à fl. 422. Todavia, a parte agravante somente interpôs o agravo interno no dia 6/12/2018, o que o torna intempestivo.
    Nesse sentido, a jurisprudência do STJ:
    AGRAVO INTERNO NO AGRAVO EM RECURSO ESPECIAL. INTEMPESTIVIDADE. NÃO CONHECIMENTO.
    1. Não se conhece do agravo interno interposto após o encerramento do prazo estabelecido pelo art. 1.070 do Código de Processo Civil/2015.
    2. Agravo interno não conhecido.
    (AgInt no AREsp n. 877.362/RO, Rel. Ministro Og Fernandes, Segunda Turma, julgado em 6/4/2017, DJe 17/4/2017.)
    PROCESSUAL CIVIL. AGRAVO INTERNO NO RECURSO ESPECIAL. RECURSO INTEMPESTIVO. INTERPOSIÇÃO ALÉM DO PRAZO LEGAL. ART. 1.070 DO CPC/2015. RECURSO SUBSCRITO E TRANSMITIDO DIGITALMENTE POR ADVOGADO SEM PROCURAÇÃO NOS AUTOS, NA VIGÊNCIA DO CPC/2015. ART. 104 C/C ART. 932, PARÁGRAFO ÚNICO, DO CPC/2015. AUSÊNCIA DA REGULARIZAÇÃO DA REPRESENTAÇÃO PROCESSUAL, APESAR DA INTIMAÇÃO, PARA TANTO. NÃO CONHECIMENTO. SÚMULA 115 DO STJ. AGRAVO INTERNO NÃO CONHECIDO.
    I. Agravo interno aviado contra decisão publicada em 19/10/2016, que, por sua vez, julgara recurso interposto contra decisum publicado na vigência do CPC/73.
    II. A decisão, objeto deste Agravo interno, foi disponibilizada em 18/10/2016 (terça-feira), no Diário de Justiça eletrônico, considerando-se publicada em 19/10/2016 (quarta-feira), e o presente recurso foi interposto em 22/11/2016, quando já escoado o prazo legal, em 14/11/2016, conforme certificado nos autos.
    III. Descumprido, portanto, o prazo de quinze dias úteis, para a interposição do Agravo interno, previsto no art. 1.070 do Código de Processo Civil vigente, inviável a análise dos argumentos recursais, uma vez que não preenchido um dos requisitos extrínsecos de sua admissibilidade.
     ..
    VII. Agravo interno não conhecido, pela intempestividade e pela ausência de procuração, ou regular substabelecimento, outorgando poderes ao advogado subscritor, conforme certidões nos autos.
    (AgInt no REsp n. 1.630.054/SC, Rel. Ministra Assusete Magalhães, Segunda Turma, julgado em 4/4/2017, DJe 11/4/2017.)
    PROCESSUAL CIVIL. AGRAVO INTERNO NO AGRAVO EM RECURSO ESPECIAL. ENUNCIADO ADMINISTRATIVO 3/STJ. DESCUMPRIMENTO DO PRAZO RECURSAL. IMPOSSIBILIDADE DE CONTAGEM EM DOBRO. LITISCONSÓRCIO COM ADVOGADOS DISTINTOS. PROCESSO ELETRÔNICO.
    1. A decisão impugnada no agravo interno é considerada publicada em 16/09/2016, o que fez com o que prazo recursal tivesse início em 19/09/2016 e o fim no dia 07/10/2016, de maneira que o protocolo eletrônico da minuta do agravo interno apenas em 14/10/2016 revela a intempestividade do exercício do direito de recorrer.
    2. Não se aplica a contagem do prazo em dobro quando os litisconsortes, apesar de defendidos por procuradores diferentes, litigarem em processo com autos eletrônicos. Inteligência do art. 229, "caput" e § 2.º, do CPC/2015.
    3. Agravo interno não conhecido.
    (AgInt no AREsp n. 978.549/RJ, Rel. Ministro Mauro Campbell Marques, Segunda Turma, julgado em 7/3/2017, DJe 13/3/2017.)
    Ante o exposto, não conheço do agravo interno.
    É o voto.
    '''

# Montando o payload
#payload_api = {
#    "mensagem": {
#        "tipo": "TEXTO",
#        "conteudo": conteudo
#    },
#    "quantidadeClasses": quantidadeClasses
#}

# Montando o payload para o modelo GEN_TRN2024_CSF_SUMARIZACAO
payload_api = {
    "mensagem": conteudo
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
