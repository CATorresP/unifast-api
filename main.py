from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
#from fastapi import FastAPI, APIRouter
#from app.routes import items_router, users_router

#app = FastAPI()

#api_v1_router = APIRouter(prefix="/fastapiv1")

#api_v1_router.include_router(items_router)
#api_v1_router.include_router(users_router)

#app.include_router(api_v1_router)
