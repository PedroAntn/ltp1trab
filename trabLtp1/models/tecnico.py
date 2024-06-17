from models.pessoa import Pessoa

class Tecnico(Pessoa):
    def __init__(self, nome, idade, sexo, cpf, numero_tecnico, especialidade_tecnica, data_contratacao):
        super().__init__(nome, idade, sexo, cpf)
        self.__numero_tecnico = numero_tecnico
        self.__especialidade_tecnica = especialidade_tecnica
        self.__data_contratacao = data_contratacao

    def gravar_dados(self):
        with open('tecnicos.txt', 'a') as file:
            file.write(f"{self.__numero_tecnico},{self.__especialidade_tecnica},{self.__data_contratacao}\n")
        super().gravar_dados()

    @staticmethod
    def ler_dados():
        try:
            with open('tecnicos.txt', 'r') as file:
                for line in file:
                    numero_tecnico, especialidade_tecnica, data_contratacao = line.strip().split(',')
                    print(f"Número do Técnico: {numero_tecnico}, Especialidade Técnica: {especialidade_tecnica}, Data de Contratação: {data_contratacao}")
        except FileNotFoundError:
            print("Arquivo de técnicos não encontrado.")
