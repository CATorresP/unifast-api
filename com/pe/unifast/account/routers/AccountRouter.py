from fastapi import APIRouter

from main import app

router = APIRouter()


@app.post("/account")
async def login(form_data: str):
    return {"myaccount": "SI"}
