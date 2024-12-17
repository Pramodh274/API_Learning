from fastapi import APIRouter, HTTPException
from nltk.tokenize import word_tokenize
import textstat
from app.models.evaluation_Input import FleshInput

router = APIRouter()


@router.post("/flesh", tags=["AI_Model"], status_code=200)
async def get_flesh_score(evaluation_Input: FleshInput):
    try:
        # candidate_tokens = word_tokenize(evaluation_Input.candidate)

        candidate_fk_grade = textstat.flesch_kincaid_grade(evaluation_Input.candidate)
        candidate_fk_score = textstat.flesch_reading_ease(evaluation_Input.candidate)

        result = {
            "flesch_kincaid_grade": candidate_fk_grade,
            "flesch_reading_ease": candidate_fk_score
        }
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
