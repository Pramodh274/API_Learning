from fastapi import FastAPI
from app.routers import signup, rouge, bleu_score, bert, flesh_kinkaid
# from app.routers import bleu
from app.routers import meteor

app = FastAPI()

# Include the signup router
app.include_router(signup.router)
app.include_router(rouge.router)
app.include_router(meteor.router)
# app.include_router(bleu.router)
app.include_router(bert.router)
app.include_router(flesh_kinkaid.router)
app.include_router(bleu_score.router)