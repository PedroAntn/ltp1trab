from models.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade, sexo, cpf, numero_cliente, tipo_cliente):
        super().__init__(nome, idade, sexo, cpf)
        self.__numero_cliente = numero_cliente
        self.__tipo_cliente = tipo_cliente

    def gravar_dados(self):
        with open('clientes.txt', 'a') as file:
            file.write(f"{self.__numero_cliente},{self.__tipo_cliente}\n")
        super().gravar_dados()

    @staticmethod
    def ler_dados():
        try:
            with open('clientes.txt', 'r') as file:
                for line in file:
                    numero_cliente, tipo_cliente = line.strip().split(',')
                    print(f"Número do Cliente: {numero_cliente}, Tipo de Cliente: {tipo_cliente}")
        except FileNotFoundError:
            print("Arquivo de clientes não encontrado.")
