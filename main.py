from contrato import Contrato, le_contratos, registra_contrato
import os

def main():
    os.system('cls')
    print('Seja bem vindo ao programa de registro e leitura de contratos!')
    escolha = input('Digite (1) se você deseja registrar um novo contrato ou\n(2) para ver a lista dos contratos já registrados:\n')
    if escolha == '1':
        executar = registra_contrato()
        if executar:
            main()

    elif escolha == '2':
        le_contratos('dados/contratos.csv')
    else:
        input('Escolha inválida, aperte ENTER para tentar novamente')
        main()

if __name__ == '__main__':
    main()