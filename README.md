# Orientação a Objetos II

<details>
<summary>INFO DA DISCIPLINA</summary>

- **[AVA](https://ava.ifpr.edu.br/course/view.php?id=13096)**
- Curso: TADS
- Período: 3°
- Horário: quarta, 19:00 às 22:20 (Lab 2)
- Período letivo: 2025/1
- Período aulas: 12/03/25 à jul/25
- **[Repositório](https://github.com/fscheidt/oo2)**

</details>
<br><br>

# Aula 3 

## (1) Organização do projeto em módulos

- cada módulo deve conter o arquivo `__init__.py`
- criar arquivo main.py e testar importar Pessoa (aula 2)
- alterar pessoa.py e adicionar `__name__`

## (2) Modelagem transferência pix

- na pasta `aulas/a3` criar o arquivo `conta.py`

```python

class Transacao:
    """ Atributos: op, tipo, data, valor, origem, destino, status """
    pass

class Conta: 
    """ Atributos: saldo, limite, pix, nome, transacoes """
    def transferir(self):
        """ realiza transferência pix """
        pass

    def consulta(self):
        """ consulta saldo da conta """
        pass

# Testar:
# maria = Conta(saldo=20_000, pix="maria@pessoa.br", limite=2000)
# jose = Conta(saldo=-6000, pix="jose@pessoa.br")

```


---

# Aula 2
- Criar ambiente virtual python para o projeto
- Classe Pessoa, PessoaFisica e PessoaJuridia

## Ambiente virtual

Instala um novo ambiente virtual (env) para o projeto:

```bash
cd projeto
python3 -m venv env
source env/bin/activate
```

### instala a biblioteca rich

```bash
pip install rich
```

Teste para verificar se esta sendo usado o python do venv:
```bash
which python3
```

*Alternativa: No caso do comando `python3 -m venv` falhar:*

```bash
cd projeto
python3 -m pip install virtualenv
python3 -m virtualenv env
source env/bin/activate
```


---


# Aula 1 

## Configuração do vscode

- instalar a extensão: ms-python

- usuário windows, download do python: https://www.python.org/downloads/

**Conferir:** se o python está instalado e qual versão:
```console

python3 --version

# >> Python 3.13.2
# versão do lab: 3.10
```

