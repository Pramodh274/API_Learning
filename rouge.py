from fastapi import FastAPI
from pydantic import BaseModel
from rouge_score import rouge_scorer
import textstat
from nltk.translate import meteor_score as meteor
from nltk.tokenize import word_tokenize
import nltk
from nltk.translate.bleu_score import sentence_bleu

# Ensure NLTK data is downloaded
nltk.download('punkt')

app = FastAPI()


# Define the Pydantic model for your input data
class TextInput(BaseModel):
    reference: str
    candidate: str


# Initialize the Rouge scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)


@app.get("/")
async def root():
    return {"message": "Welcome to the FAST API!"}


@app.post("/rouge/")
async def evaluate_texts(data: TextInput):
    try:
        # Tokenize the reference and candidate texts
        # reference_tokens = word_tokenize(data.reference)
        # candidate_tokens = word_tokenize(data.candidate)

        # Calculate ROUGE scores
        rouge_scores = scorer.score(data.reference, data.candidate)
        # Convert scores to a more JSON-friendly format
        rouge_scores = {key: value.fmeasure for key, value in rouge_scores.items()}

        # Calculate Flesch-Kincaid grade level and reading ease
        # candidate_fk_grade = textstat.flesch_kincaid_grade(data.candidate)
        # candidate_fk_score = textstat.flesch_reading_ease(data.candidate)

        # Calculate the METEOR score
        # meteor_score_value = meteor.meteor_score([reference_tokens], candidate_tokens)

        #calculate the bleu score
        # bleu_score = sentence_bleu(data.reference, data.candidate)

        result = {
            "rouge_score": rouge_scores,
            # "flesch_kincaid_grade": candidate_fk_grade,
            # "flesch_reading_ease": candidate_fk_score,
            # "meteor_score_value": meteor_score_value,
            # "bleu_score": bleu_score
        }
        return result

    except Exception as e:
        return {"error": str(e)}
