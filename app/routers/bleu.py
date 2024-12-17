from fastapi import APIRouter

router = APIRouter()


@router.get("/bleu", tags=["AI_Model"])
async def get_bleu_score():
    return {"message": "BLEU score endpoint"}
