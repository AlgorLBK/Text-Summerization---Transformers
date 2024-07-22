from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class Text(BaseModel):
    text: str

summarizer = pipeline("summarization")

def t_summarize(text):
    summary = summarizer(text, max_length=100, min_length=10, do_sample=False)
    summary_text = summary[0]['summary_text']
    print(summary_text)
    return summary_text

@app.post('/')
async def summarize(text: Text):
    summary_text = t_summarize(text.text)
    return {"summary": summary_text}