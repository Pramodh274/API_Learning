from fastapi import APIRouter, HTTPException
from app.models.evaluation_Input import TextInput
from nltk.tokenize import word_tokenize
from nltk.translate import meteor_score as meteor
import nltk

# Initialize router
router = APIRouter()

# Download necessary NLTK resources
nltk.download('punkt', quiet=True)


@router.post("/meteor", tags=["AI_Model"], status_code=200)
async def compute_meteor_score(evaluation_Input: TextInput):
    """
    Compute the METEOR score given reference and candidate strings.
    """
    try:
        # Tokenize reference and candidate strings
        reference_tokens = word_tokenize(evaluation_Input.reference)
        candidate_tokens = word_tokenize(evaluation_Input.candidate)

        # Compute METEOR score
        meteor_score_value = meteor.meteor_score([reference_tokens], candidate_tokens)

        # Return the result
        return {"meteor_score": meteor_score_value}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
