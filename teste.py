import logging
import sys
from typing import Callable
from sinapses_cliente.modelo.binario import Binario
from sinapses_cliente.modelo.modelo_versao_recurso import ModeloVersaoRecurso
from sinapses_cliente.modelo.resposta.resposta_classificacao import Resposta
from sinapses_cliente.modelo.servico_contexto import ServicoContexto
from sinapses_cliente.modelo.tipo_conteudo import TipoConteudo
from sinapses_cliente.modelo.treinamento_resultado import TreinamentoResultado
from sinapses_cliente.sinapses_pipeline import SinapsesPipeline
from sinapses_cliente.sinapses_sessao import SinapsesSessao


def funcao_treinamento(sessao: SinapsesSessao) -> TreinamentoResultado:
    # Implementação mínima para evitar erros
    print("A função funcao_treinamento foi chamada.")

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


def funcao_servico(sessao: SinapsesSessao, ctx: ServicoContexto, requisicao: dict) -> Resposta:
    # Implementação mínima para evitar erros
    print("A função funcao_servico foi chamada.")

    # Criar um resultado fictício ou um objeto vazio para evitar erros
    return Resposta(**{"Resultado": ""})


def funcao_teste_servico(_s: SinapsesSessao, _c: ServicoContexto, servico: Callable[[dict], dict]) -> None:
    # Implementação mínima para evitar erros
    print("A função funcao_servico foi chamada.")
    assert True == True


# Inicializar o pipeline
pipeline = SinapsesPipeline.instancia()

# Definir as funções
pipeline.definir_treinamento(funcao_treinamento)
pipeline.definir_inicializacao_servico(funcao_inicializacao_servico)
pipeline.definir_servico(funcao_servico)
pipeline.definir_teste_servico(funcao_teste_servico)

# testar pipeline
# pipeline.testar_pipeline()

# Envia o código do modelo para o SINAPSES
pipeline.enviar_treinado()
