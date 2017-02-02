"""
Ao ser executado deve imprimir todos resgistros presentes em arquivos.
O resultado deve ser ocombinado de todos registros dentro de arquivos pertencentes
ao diretório "arquivos". Formatos específicos da entrada: json ou csv.
Cada registro tem o primeiro campo com nome, segundo com sobrenome e terceiro como idade

Resolver o problema utilizando funções geradoras para cada um dos formatos,
desacoplando escrita da leitura
"""
import json
import csv
import os

for raiz, _, arquivos in os.walk(os.path.join('.', 'arquivos')):
    for a in arquivos:
        path_de_arquivo = os.path.join(raiz, a)
        with open(path_de_arquivo) as file:
            # esse data é uma lista, que também posso iterar por ela
            data = json.load(file)
            data = csv.reader(file)
            for inf in data:
                print((inf))


with open('./arquivos/pythonistas.csv') as file:
    # esse data é um iterável
    data = csv.reader(file)

