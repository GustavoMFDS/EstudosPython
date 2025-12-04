from sqlalchemy.orm import sessionmaker
from models import Usuario, db
def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    
    finally:
        session.close()