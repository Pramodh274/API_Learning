from fastapi import APIRouter, HTTPException
from app.models.evaluation_Input import TextInput
from rouge_score import rouge_scorer
import nltk

router = APIRouter()

nltk.download('punkt')

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)


@router.post("/rouge", tags=["AI_Model"], status_code=200)
def rouge(evaluation_Input: TextInput):
    try:
        # Calculate ROUGE scores
        rouge_scores = scorer.score(evaluation_Input.reference, evaluation_Input.candidate)
        # Convert scores to a more JSON-friendly format
        rouge_scores = {key: value.fmeasure for key, value in rouge_scores.items()}

        result = {
            "rouge_score": rouge_scores
        }
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
