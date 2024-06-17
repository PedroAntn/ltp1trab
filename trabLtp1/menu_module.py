from models.pessoa import Pessoa
from models.cliente import Cliente
from models.atendente import Atendente
from models.tecnico import Tecnico

def show_menu():
    while True:
        # Exibe as opções do menu para o usuário
        print("\nMenu:")
        print("1. Cadastrar Pessoa")
        print("2. Cadastrar Cliente")
        print("3. Cadastrar Atendente")
        print("4. Cadastrar Técnico")
        print("5. Exibir Pessoas")
        print("6. Exibir Clientes")
        print("7. Exibir Atendentes")
        print("8. Exibir Técnicos")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Cadastra uma nova pessoa
            nome = input("Nome: ")
            idade = input("Idade: ")
            sexo = input("Sexo: ")
            cpf = input("CPF: ")
            pessoa = Pessoa(nome, idade, sexo, cpf)
            pessoa.gravar_dados()
        elif opcao == '2':
            # Cadastra um novo cliente
            nome = input("Nome: ")
            idade = input("Idade: ")
            sexo = input("Sexo: ")
            cpf = input("CPF: ")
            numero_cliente = input("Número do Cliente: ")
            tipo_cliente = input("Tipo de Cliente: ")
            cliente = Cliente(nome, idade, sexo, cpf, numero_cliente, tipo_cliente)
            cliente.gravar_dados()
        elif opcao == '3':
            # Cadastra um novo atendente
            nome = input("Nome: ")
            idade = input("Idade: ")
            sexo = input("Sexo: ")
            cpf = input("CPF: ")
            numero_atendente = input("Número do Atendente: ")
            data_contratacao = input("Data de Contratação: ")
            atendente = Atendente(nome, idade, sexo, cpf, numero_atendente, data_contratacao)
            atendente.gravar_dados()
        elif opcao == '4':
            # Cadastra um novo técnico
            nome = input("Nome: ")
            idade = input("Idade: ")
            sexo = input("Sexo: ")
            cpf = input("CPF: ")
            numero_tecnico = input("Número do Técnico: ")
            especialidade_tecnica = input("Especialidade Técnica: ")
            data_contratacao = input("Data de Contratação: ")
            tecnico = Tecnico(nome, idade, sexo, cpf, numero_tecnico, especialidade_tecnica, data_contratacao)
            tecnico.gravar_dados()
        elif opcao == '5':
            # Exibe todas as pessoas cadastradas
            Pessoa.ler_dados()
        elif opcao == '6':
            # Exibe todos os clientes cadastrados
            Cliente.ler_dados()
        elif opcao == '7':
            # Exibe todos os atendentes cadastrados
            Atendente.ler_dados()
        elif opcao == '8':
            # Exibe todos os técnicos cadastrados
            Tecnico.ler_dados()
        elif opcao == '9':
            # Sai do programa
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
