import logging
import sys
import base64
from typing import Callable
from sinapses_cliente.modelo.requisicao.mensagem import Mensagem
from sinapses_cliente.modelo.servico_contexto import ServicoContexto
from sinapses_cliente.modelo.treinamento_resultado import TreinamentoResultado
from sinapses_cliente.modelo.requisicao.requisicao_sumarizacao import RequisicaoSumarizacao
from sinapses_cliente.modelo.resposta.resposta_sumarizacao import RespostaSumarizacao
from sinapses_cliente.sinapses_pipeline import SinapsesPipeline
from sinapses_cliente.sinapses_sessao import SinapsesSessao
from lexrank import LexRank
from lexrank.mappings.stopwords import STOPWORDS


def decodificar_texto_sumarizado_json(resposta_json: dict) -> str:
    try:
        texto_base64 = resposta_json.get('textoSumarizado')
        if not texto_base64:
            raise ValueError("Chave 'textoSumarizado' não encontrada ou vazia.")

        return base64.b64decode(texto_base64).decode('UTF-8')

    except Exception as e:
        print(f"Erro ao decodificar: {e}")
        return ""


def funcao_treinamento(sessao: SinapsesSessao) -> TreinamentoResultado:
    # Implementação mínima para evitar erros
    #print("A função funcao_treinamento foi chamada.")
    # Criar um resultado fictício ou um objeto vazio para evitar erros
    return TreinamentoResultado(1, [])


def funcao_inicializacao_servico(sessao: SinapsesSessao):
    # Implementação mínima para evitar erros
    logger = logging.getLogger('Sinapses')
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # Armazenar o modelo, tokenizer e logger
    ctx = {
        'modelo': {
            'model': None,
            'tokenizer': None
        },
        'logger': None
    }
    return ServicoContexto(**ctx)


def funcao_servico(sessao: SinapsesSessao, ctx: ServicoContexto,
                   requisicao: RequisicaoSumarizacao) -> RespostaSumarizacao:
    # O texto é extraído da requisição
    texto = sessao.get_mensagem_texto(requisicao.mensagem)
    quantidade_sentencas = 5
    lxr = LexRank(texto, stopwords=STOPWORDS['pt'])
    sentencas = texto.split('.')
    sentencas = [s.strip() for s in sentencas if s.strip()]
    resumo = lxr.get_summary(sentencas, summary_size=quantidade_sentencas, threshold=.1)
    teor_ementa_gerada = '\n'.join(resumo)
    # print(teor_ementa_gerada)
    return RespostaSumarizacao(teor_ementa_gerada, None)


def funcao_teste_servico(_s: SinapsesSessao, _c: ServicoContexto, servico: Callable[[dict], dict]) -> None:
    texto_1 = '''
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

    texto_2 = '''
    Neste domingo, Meirelles participou da cerimônia de entrega do prêmio “Banco Central do ano”, oferecido pela revista The Banker à instituição que preside.
    “Este é um sinal importante de reconhecimento do nosso trabalho, de que o Brasil está indo na direção correta”, disse ele.
    Segundo Meirelles, o Banco Central do Brasil está sendo percebido como uma instituição comprometida com a meta de inflação.
    '''

    texto_3 = '''
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

    r1 = servico({'mensagem': Mensagem.texto(texto_1).to_dict()})
    # print(r1)

    r2 = servico({'mensagem': Mensagem.texto(texto_2).to_dict()})
    r3 = servico({'mensagem': Mensagem.texto(texto_3).to_dict()})

    texto_decodificado = decodificar_texto_sumarizado_json(r1)
    # print(texto_decodificado)

    assert r1 == r3


# Inicializar o pipeline
pipeline = SinapsesPipeline.instancia()

# Definir as funções
pipeline.definir_treinamento(funcao_treinamento)
pipeline.definir_inicializacao_servico(funcao_inicializacao_servico)
pipeline.definir_servico(funcao_servico)
pipeline.definir_teste_servico(funcao_teste_servico)

# testar pipeline
pipeline.testar_pipeline()

# Envia o código do modelo para o SINAPSES
pipeline.enviar_treinado()
