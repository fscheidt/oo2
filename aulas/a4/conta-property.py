from datetime import datetime
from rich import print
class Transacao:
    def __init__(self):
        self.operacao: str = None
        self.data: datetime = None
        self.valor: float = None
        self.origem: Conta = None
        self.destino: Conta = None
        self.status: bool = False
    # MÉTODOS ESTÁTICOS:
    # nao precisamos de uma instância da classe
    # para usa-lo. Não tem "self"
    def credito(
            valor: float, 
            origem: "Conta", 
            destino: "Conta") -> "Transacao":
        """ cria uma transacao de credito """
        t = Transacao()
        t.operacao = "C"
        t.data = datetime.now()
        t.valor = valor
        t.origem = origem
        t.destino = destino
        return t

class Conta: 
    """ Atributos: saldo, limite, pix, transacoes """
    def __init__(self, 
                 saldo: float,
                 pix: str, 
                 limite: float = 0,
                 ):
        self._saldo = saldo # _ para tornar atributo protegido
        self.limite = limite
        self._pix = pix
        # 1 Conta possui N Transacoes (1-N)
        self.transacoes: list[Transacao] = []

    @property
    def saldo_limite(self) -> float:  # GETTER
        """ 
        Atributo dinâmico - calculado com base no
        saldo da conta + limite disponível.
        ou seja, saldo_limite não é declarado no 
        construtor da classe Conta.
        """
        return self._saldo + self.limite

    # GET PIX
    @property
    def pix(self): return self._pix
    # SET PIX
    # validar: (1) é tipo string, (2) min de 4 char
    @pix.setter
    def pix(self, value: str):
        if not isinstance(value, str):
            raise TypeError()
        if len(value) < 4:
            raise ValueError("minimo de 4 characteres")
        self._pix = value

    @property
    def saldo(self) -> float: # MÉTODO GETTER
        return self._saldo
    
    @saldo.setter    # METODO SETTER
    def saldo(self, valor: float):
        # EXEMPLO DE VALIDACAO (descomentar para testar)
        # if self._saldo < 0: 
            # raise Exception() # levantar uma exceção
        self._saldo = valor
    
    def transferir(self, destino: "Conta", valor: float):
        """ realiza transferência pix """
        t_credito = Transacao.credito(
            valor,
            origem=self,
            destino=destino
        )
        destino.transacoes.append(t_credito)

        # t_debito = ....
        # .transcao

        # self.saldo(self._saldo - valor)
        # if valor > self.saldo_limite raise execption
        self.saldo -= valor # SETTER 
        destino.saldo += valor # SETTER

        t_credito.status = True # sucesso!

        print(f"Pix de R$ {valor} para {destino.pix}")

    def consulta(self):
        """ consulta saldo da conta """
        print("-"*40) # pip install rich
        cl = "red" if self.saldo < 0 else "blue" # GETTER
        print(f"Saldo atual é R$ [{cl}]{self.saldo}[/] (conta {self.pix})")

if __name__ == "__main__":
    maria = Conta(saldo=20_000, pix="maria@pessoa.br", limite=2000)
    jose = Conta(saldo=2000, pix="jose@pessoa.br")

    # jose.pix = 51000 # should not pass # TypeError
    # jose.pix = "ABC" # ValueError

    maria.consulta() 
    jose.consulta() 

    maria.transferir(jose, 8_000) 

    maria.consulta() 
    jose.consulta() 
