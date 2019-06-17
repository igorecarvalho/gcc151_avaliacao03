# Avaliação 3 de PLN 16.06.19
Este repositório contêm a solução para a prova 3 da disciplina de GCC151-PLN.

## O grupo:
- Igor Carvalho: https://github.com/igorecarvalho
- Franciscone Luiz: https://github.com/franciscone14
- Victor Hugo Landin: https://github.com/vhal9

## O problema esta descrito no arquivo pdf.
- Arquivo Notebook/Prova3.ipynb realiza o estudados dos dados.
- Arquivo Prova3-PLN.pdf contém o relatório de desenvolvimento da avaliação.

- As biblioteca que contêm rotinas de normatização estão contidas em:
- - notebook/nlputils/lexical/preprocessing.py
- - notebook/nlputils/syntax/preprocessing.py
- - notebook/nlputils/morphosyntax/preprocessing.py
- - notebook/nlputils/semantics/preprocessing.py

# Para executar:
- ```git clone https://github.com/igorecarvalho/gcc151_avaliacao03```
- entre no diretório do repositório.
- crie o diretório models
- baixe a biblioteca da língua portguesa do spacy através do comando ```python -m spacy download pt_core_news_sm``` e salve na pasta models.
- instale as bibliotecas do python com o comando: ```pip3 install -r requirements.txt```
- execute o comando: ```jupyter notebook```.

## Download do corpora
- criar o diretório data/dataset
- baixar o corpus no link ```https://drive.google.com/open?id=1mxU_rCKRoRUcOH1GrSho8hqtAmJbNIqm``` pois os alguns arquivos .xml estavam com erros de edição nas tags impedindo a leitura correta dos arquivos.
- salvar os corpus dentro do diretório criado.