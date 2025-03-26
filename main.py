from aulas.a1.pessoa import Pessoa as P1
from aulas.a2.pessoa import Pessoa
from aulas.a2.pessoa_abs import PessoaJuridica
import rich

print("*"*30)

# pessoa da aula1
p1 = P1(nome="Jose")
p1.exibe_dados()

print("*"*30)

# (pessoa.py) criar instancia de Pessoa - aula2 
p = Pessoa("Maria")
rich.print(p.nome)


print("*"*30)

# (pessoa_abs.py)
pj = PessoaJuridica("Italo","it@gov.br", "0000")
print(pj.nome)
