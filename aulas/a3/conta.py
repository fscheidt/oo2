
from rich import print
class Transacao:
    """ Atributos: op, tipo, data, valor, origem, destino, status """
    pass

class Conta: 
    """ Atributos: saldo, limite, pix, transacoes """
    def __init__(self, 
                 saldo: float,
                 pix: str, 
                 limite: float = 0,
                 ):
        self.saldo = saldo
        self.limite = limite
        self.pix = pix
        # 1 Conta possui N Transacoes (1-N)
        self.transacoes: list[Transacao] = []
    
    def transferir(self, destino: "Conta", valor: float):
        """ realiza transferência pix   """
        # self == maria
        # destino == jose
        self.saldo -= valor
        destino.saldo += valor
        print(f"Pix de R$ {valor} para {destino.pix}")

    def consulta(self):
        """ consulta saldo da conta """
        print("-"*40) # pip install rich
        cl = "red" if self.saldo < 0 else "blue"
        print(f"Saldo atual é R$ [{cl}]{self.saldo}[/] (conta {self.pix})")

if __name__ == "__main__":
    # Testes:
    maria = Conta(saldo=20_000, pix="maria@pessoa.br", limite=2000)
    jose = Conta(saldo=-6000, pix="jose@pessoa.br")
    maria.consulta() 
    jose.consulta() 

    maria.transferir(jose, 8_000) 

    maria.consulta() 
    jose.consulta() 

    maria.transferir(jose, 30_000) # Nao pode deixar!
    maria.consulta() # deve printar 12_000

    maria.transferir(jose, 14_000) # pode usando o limite
    maria.consulta() # deve printar 0
