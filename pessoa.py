class Pessoa:
    def __init__(self, nome: str):  # construtor
        self.nome = nome     # atributo (public)
        self.cpf = None      # atributo (public)
    def exibe_dados(self):   # metodo/função (public)
        print(f"""<Pessoa>\
            \n    Nome: {self.nome}\
            \n    CPF: {self.cpf}\
            """)

p1 = Pessoa("Maria")
p1.cpf = "838380000"
# print(p1.nome)
print(id(p1))    # imprimi o "identificador" do objeto
p1.exibe_dados()

p2 = Pessoa("Joao")
p2.cpf = "138380000"
print(id(p2))  # imprimi o "identificador" do objeto
# print(p1.nome)
p2.exibe_dados()

