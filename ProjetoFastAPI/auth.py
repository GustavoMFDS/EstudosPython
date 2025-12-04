from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencias import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy .orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])
@auth_router.get("/")
async def auth():
    """
    Rota de autenticação
    """
    return {"menssagem": "Voce está na rota de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email()).first()
    if usuario:
        #Ja existe um usuario com esse email
        raise HTTPException(status_code=400, detail="E-mail do usuario ja cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha())
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem": f"usuario cadastrado com sucesso {usuario_schema.email}"}
    