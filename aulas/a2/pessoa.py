from rich import print
class Pessoa:
    def __init__(self, 
                 nome: str, 
                 email: str = None
                 ):
        self.nome = nome
        self.email = email
        self.renda = 0

class PessoaJuridica(Pessoa): # extends 
    pass

if __name__ == "__main__":
    print("="*40)
    pj = PessoaJuridica("Muffato")
    print(pj.nome)

    print("="*40)
    # pagina web
    p1 = Pessoa("Maria", "maria@gmail.com")
    print(p1.nome)
    print(p1.email)
    p1.renda = 90_000
    print(f"Renda anual da {p1.nome} foi R$ {p1.renda}")

    p2 = Pessoa("James")
    print(p2.nome)
    print(p2.email)
