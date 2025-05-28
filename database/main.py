import crud
from crud import SessionLocal, init_db
from models import Filme

# ============================================
# Script para testar as operações crud
# ============================================

def test_create_movie():
    db = SessionLocal()
    filme = Filme(
        titulo="Avatar",
        ano=2009
    )
    crud.add_filme(db, filme)
    
def test_list_movies():
    db = SessionLocal()
    return [(f.id, f.titulo, f.ano) for f in crud.get_filmes(db)]
     
def test_delete_movie(filme_id: int):
    db = SessionLocal()
    crud.delete_filme(db, filme_id)

if __name__ == "__main__":
    from rich import print
    # Initialize Database
    init_db()
    # test_create_movie() # teste de inserção de um filme
    test_delete_movie(1)
    results = test_list_movies() # select all

    print(results)
