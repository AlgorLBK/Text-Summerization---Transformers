from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class Text(BaseModel):
    text: str

model_name = "google-t5/t5-small"
revision = "main"
token = "your_hugging_face_token"
summarizer = pipeline("summarization", model=model_name, revision=revision, token=token)


def t_summarize(text):
    summary = summarizer(text, max_length=130, min_length=50, do_sample=False)
    summary_text = summary[0]['summary_text']
    print(summary_text)
    return summary_text

@app.post("/")
def summarize(text: Text):
    summary = t_summarize(text.text)
    return {"summary": summary}

@app.get("/")
def okay():
    return {"message": "okay"}