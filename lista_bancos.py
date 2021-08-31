import csv

def get_lista(caminho):
   
    bancos = {}
    with open(caminho, mode= 'r+', encoding='latin_1') as arquivo:
        leitor = csv.reader(arquivo)

        #a chave é o código do banco
        for linha in leitor:
            nome_banco, codigo_banco = linha
            bancos[f'{codigo_banco}'] = nome_banco
    
    return bancos