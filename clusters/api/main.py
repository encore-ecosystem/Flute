from src.routes import *
from fastapi import FastAPI
from src import PORT
app            = FastAPI()
app.include_router(auth_router)
app.include_router(home_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=PORT)