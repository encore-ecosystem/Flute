from core.utils.protection import get_current_user
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/home",
    tags=["home feed"],
)


@router.get("/")
async def home(user = Depends(get_current_user)):
    return f"Hello from home feed, {user.username}"