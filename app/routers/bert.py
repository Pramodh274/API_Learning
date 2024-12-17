from fastapi import APIRouter

router = APIRouter()


@router.get("/bert", tags=["AI_Model"])
async def get_bert_score():
    return {"message": "Bert score endpoint"}
