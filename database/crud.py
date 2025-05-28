from models import Base, Filme
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# ============================================
# Configuração do sqlite
# ============================================

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///movies.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)


# ============================================
# Operações CRUD
# ============================================

def get_filme(db: Session, filme_id: int):
    return db.query(Filme).filter(Filme.id == filme_id).all()

def get_filmes(db: Session):
    return db.query(Filme).filter().all()

def add_filme(db: Session, filme: Filme):
    db.add(filme)
    db.commit()

def delete_filme(db: Session, filme_id: int):
    db.query(Filme).filter(Filme.id == filme_id).delete()
    db.commit()
