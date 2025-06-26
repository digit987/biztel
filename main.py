from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from app.analyzer import ChatAnalyzer
from app.data_loader import DataLoader
from app.data_cleaner import DataCleaner
from app.data_transformer import DataTransformer
import logging

app = FastAPI(title="Chat Analyzer API")

logging.basicConfig(level=logging.INFO)

class ChatTurn(BaseModel):
    message: str
    agent: str
    sentiment: str
    knowledge_source: List[str]
    turn_rating: str
    article_url: str

class TranscriptInput(BaseModel):
    content: List[ChatTurn]

@app.post("/summarize_transcript/")
def summarize_transcript(data: TranscriptInput):
    try:
        analyzer = ChatAnalyzer(chat_data=[turn.dict() for turn in data.content])
        return analyzer.summarize()
    except Exception as e:
        logging.error(f"Error summarizing transcript: {e}")
        raise HTTPException(status_code=500, detail="Failed to summarize transcript")

@app.get("/dataset_summary/")
def dataset_summary():
    try:
        loader = DataLoader("BiztelAI_DS_Dataset_V1.json")
        raw_data = loader.load_data()

        cleaner = DataCleaner()
        cleaned = cleaner.clean(raw_data)

        transformer = DataTransformer()
        df = transformer.flatten_conversations(cleaned)

        return {
            "total_conversations": len(cleaned),
            "total_messages": len(df),
            "agents": df['agent'].value_counts().to_dict(),
            "sentiments": df['sentiment'].value_counts().to_dict()
        }
    except Exception as e:
        logging.error(f"Error summarizing dataset: {e}")
        raise HTTPException(status_code=500, detail="Failed to process dataset")

@app.post("/transform_raw_input/")
def transform_raw_input(data: Dict):
    try:
        transformer = DataTransformer()
        df = transformer.flatten_conversations({"sample": data})
        return df.to_dict(orient="records")
    except Exception as e:
        logging.error(f"Error transforming input: {e}")
        raise HTTPException(status_code=500, detail="Failed to transform input")