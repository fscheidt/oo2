from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

""" 
Classe que representa a entidade Filme
"""

Base = declarative_base()

class Filme:
    """ 
    Classe Filme usada na aplicação (nicegui)
    """
    def __init__(self,
        titulo: str,
        ano: int,
        diretor: str = None,
        pais_origem: str = None):
        
        self.id: int = None
        self.titulo: str = titulo
        self.ano: int = ano
        self.diretor: str = diretor
        self.pais_origem: str = pais_origem
        
        def __repr__(self):
            return f"<Filme(titulo={self.titulo}, ano={self.ano})>"


class FilmeBase(Base):
    """ 
    Classe FilmeBase é usada pelo SQLAlchemy para mapear a tabela filmes 
    """
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    diretor = Column(String, nullable=False)
    pais_origem = Column(String, nullable=False)
    
    def __repr__(self):
        """ 
        Método (opcional) para printar o objeto filme (debug) 
        """
        return f"""<FilmeBase⛁
    id={self.id}, 
    titulo={self.titulo}, 
    diretor={self.diretor},
    pais_origem={self.pais_origem},
    ano={self.ano})>"""


if __name__ == "__main__":

    filme = Filme(
        titulo="Avatar",
        ano=2009,
        diretor="Matheus",
        pais_origem="USA",
    )

    # Cria uma instancia da classe FilmeBase (sqlalchemy)
    filme_db = FilmeBase(**filme.__dict__)

    print(filme_db)


