from models.pessoa import Pessoa

class Atendente(Pessoa):
    def __init__(self, nome, idade, sexo, cpf, numero_atendente, data_contratacao):
        super().__init__(nome, idade, sexo, cpf)
        self.__numero_atendente = numero_atendente
        self.__data_contratacao = data_contratacao

    def gravar_dados(self):
        with open('atendentes.txt', 'a') as file:
            file.write(f"{self.__numero_atendente},{self.__data_contratacao}\n")
        super().gravar_dados()

    @staticmethod
    def ler_dados():
        try:
            with open('atendentes.txt', 'r') as file:
                for line in file:
                    numero_atendente, data_contratacao = line.strip().split(',')
                    print(f"Número do Atendente: {numero_atendente}, Data de Contratação: {data_contratacao}")
        except FileNotFoundError:
            print("Arquivo de atendentes não encontrado.")
