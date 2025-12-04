from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def orders():
    """
    Rota de pedidos, precisa de autenticação para rodar
    """
    return {"menssagem": "Voce está na rota de pedidos"}
