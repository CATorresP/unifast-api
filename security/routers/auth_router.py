from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/")
async def read_users():
    return [{"username": "johndoe"}, {"username": "alice"}]
