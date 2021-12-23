from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
	text: str

app=FastAPI()
translator=pipeline("translation_en_to_ru", "Helsinki-NLP/opus-mt-en-ru")

@app.get("/")
def root():
	return {"message": "Happy New Year!"}

@app.post("/predict/")
def predict(item: Item):
	return translator(item.text)[0] 

  
