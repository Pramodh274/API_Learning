from fastapi import APIRouter, HTTPException
import nltk
from app.models.evaluation_Input import TextInput
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.tokenize import word_tokenize

router = APIRouter()

# nltk.download('punkt')


@router.post("/bleu", tags=["AI_Model"], status_code=200)
async def bleu(evaluation_Input: TextInput):
    try:
        # Tokenize input
        reference_tokens = word_tokenize(evaluation_Input.reference)
        candidate_tokens = word_tokenize(evaluation_Input.candidate)

        smoothing = SmoothingFunction().method4
        bleu_score = sentence_bleu([reference_tokens], candidate_tokens, smoothing_function=smoothing)

        result = {
            "bleu_score": bleu_score
        }
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
