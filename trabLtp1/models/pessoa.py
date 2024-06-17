class Pessoa:
    def __init__(self, nome, idade, sexo, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__cpf = cpf

    def gravar_dados(self):
        with open('pessoas.txt', 'a') as file:
            file.write(f"{self.__nome},{self.__idade},{self.__sexo},{self.__cpf}\n")

    @staticmethod
    def ler_dados():
        try:
            with open('pessoas.txt', 'r') as file:
                for line in file:
                    nome, idade, sexo, cpf = line.strip().split(',')
                    print(f"Nome: {nome}, Idade: {idade}, Sexo: {sexo}, CPF: {cpf}")
        except FileNotFoundError:
            print("Arquivo de pessoas não encontrado.")
