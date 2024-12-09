from fastapi import FastAPI
from app.routers import signup

app = FastAPI()

# Include the signup router
app.include_router(signup.router)
