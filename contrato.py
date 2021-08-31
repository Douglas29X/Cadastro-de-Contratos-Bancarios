import csv
import os
from lista_bancos import get_lista


class Contrato:
    def __init__(self, codigo_banco, valor_despesa, data):
        self.__codigo_banco = codigo_banco
        self.__valor_despesa = valor_despesa
        self.__data = data

    @property
    def codigo_banco(self):
        return self.__codigo_banco

    @property
    def valor_despesa(self):
        valor_despesa = float(self.__valor_despesa)
        return f'{valor_despesa:.2f}'
 
    @property
    def data(self):
        return self.__data

    def __str__(self):
        return f'{self.__codigo_banco},{self.__valor_despesa},{self.__data}\n'
    
    def __dir__(self):
        lista = [self.__codigo_banco, self.__valor_despesa, self.__data]
        return lista

def le_contratos(caminho, encoding='latin_1'):
    
    contratos= []
    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)
        numero_contrato = 0

        for linha in leitor:
            numero_contrato += 1
            codigo_banco, valor_despesa, data = linha

            contrato = Contrato(codigo_banco, valor_despesa, data)
            contratos.append(contrato)
    
    print(f'\nNúmero de contatos criados: {numero_contrato}\n')

    bancos = get_lista('dados/codigos_bancarios.csv')

    for contrato in contratos:
        print(f'Banco: {contrato.codigo_banco} - {bancos[contrato.codigo_banco]}\nValor: R${contrato.valor_despesa}\nData do registro: {contrato.data}\n\n')


def registra_contrato():
    
    bancos = get_lista('dados/codigos_bancarios.csv')
    with open('dados/contratos.csv', mode='a+') as arquivo:
        try:
            while True:
                os.system('cls')
                codigo_banco = input('Digite o código do seu banco: ')
                valor_despesa = float(input('Digite o valor da despesa do contrato: '))

                while True:
                    dia = int(input('Digite o dia do cadastro do contrato: '))
                    if dia < 10 and dia > 0:
                        dia = f'0{dia}'
                        break
                    elif dia >= 32 or dia <= 0:
                        print('Desculpe, dia inválido, tente novamente.\n')
                    else:
                        break
                
                while True:
                    mes = int(input('Digite o mês do cadastro do contrato: '))
                    if mes < 10 and mes > 0:
                        mes = f'0{mes}'
                        break
                    elif mes <= 0 or mes >= 13:
                        print('Desculpe, mês inválido, tente novamente.\n')
                    else: 
                        break
                
                ano = int(input('Digite o ano do cadastro do contrato: '))

                data = f'{dia}/{mes}/{ano}'
                contrato = Contrato(codigo_banco, valor_despesa, data)
                print(f'Banco: {contrato.codigo_banco} - {bancos[contrato.codigo_banco]}\nValor: R${contrato.valor_despesa}\nData do registro: {contrato.data}\n\n')
                arquivo.write(str(contrato))
                arquivo.flush()
                escolha = input('Pressione START para cadastrar outro cliente ou digite (1) para encerrar\n')
                
                if escolha == '1':
                    raise KeyboardInterrupt
        except KeyboardInterrupt:
            print('\nProcesso de escrita encerrado.')
        except IndexError:
            escolha = int(input('Desculpe, o código bancário digitado não consta em nosso sistema.\n'
            'Digite (1) se quiser ver a lista dos códigos atuais ou\n(2) para reiniciar o programa'))

            if escolha == 1:
                print()
                return False
            elif escolha == 2:
                return True

        finally: 
            print('Programa finalizado')