from rich import print
from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, 
                 nome: str, 
                 email: str = None
                 ):
        self.nome = nome
        self.email = email
        self.renda = 0
    @abstractmethod
    def calcular_ir(self):
        # PF paga 20% e PJ paga 10%
        pass
    def exibe_dados(self):   # metodo/função (public)
        print(f"""<Pessoa>\
            \n    Nome: {self.nome}\
            \n    Renda: {self.renda}\
            """)
            

class PessoaJuridica(Pessoa): # extends 
    def __init__(self, nome, email, cnpj): # sobrescrita do construtor
        super().__init__(nome, email)
        self.cnpj = cnpj
    def calcular_ir(self):
        return self.renda * 0.1

class PessoaFisica(Pessoa): # extends 
    def __init__(self, nome, email, cpf): # sobrescrita do construtor
        super().__init__(nome, email)
        self.cpf = cpf
    def calcular_ir(self):
        return self.renda * 0.2

if __name__ == "__main__":
    p1 = PessoaFisica("Maria", "mary@gmail.com", "100.000.000-99")
    p1.renda = 90_000
    print(f"IR a pagar {p1.nome} foi R$ {p1.calcular_ir()}")

    p1 = PessoaJuridica("MUFFATO", "mmm@gmail.com", "0001/111.000-22")
    p1.renda = 25_200_000
    print(f"IR a pagar {p1.nome} foi R$ {p1.calcular_ir()}")