# atualizar pip

#python.exe -m pip install --upgrade pip

# criar um ambiente virtual do Python com Anaconda

#conda create --name nomeambiente python=3.11
#conda activate nomeambiente

# executar no terminal, dentro da venv

#pip install sentencepiece

# versão 3.10.1 do python ou anterior (até 3.8)

#pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# versão 3.11.9 do python

#pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu121

#pip install transformers datasets torch
#pip install transformers[torch]
#pip install accelerate -U

#pip install --upgrade sinapses-nbextension sinapses-cliente ia-utils

#pip install jupyter --> não precisa <--

# listar os pacotes instalados

#pip freeze

# verificar a versão do python

#python --version

# verificar a instalação (na célula do jupyter):

#!python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"

# instalar bibliotecas

#pip install -r requirements.txt