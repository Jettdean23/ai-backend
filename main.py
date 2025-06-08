from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

def generate_caption_and_hashtags(topic: str, platform: str) -> (str, List[str]):
    caption = f"🔥 {topic} is a game changer! Learn how it works on {platform} 🚀"
    hashtags = [f"#{platform.lower()}", "#personalbrand", "#creatorlife", "#ai", "#marketing"]
    return caption, hashtags

def generate_thumbnail_url(topic: str, description: str) -> str:
    return f"https://placehold.co/600x400?text={topic.replace(' ', '+')}"

class GenerateRequest(BaseModel):
    topic: str
    platform: str
    description: Optional[str] = ""

class GenerateResponse(BaseModel):
    caption: str
    hashtags: List[str]
    thumbnail: str

@app.post("/api/generate", response_model=GenerateResponse)
def generate_content(req: GenerateRequest):
    caption, hashtags = generate_caption_and_hashtags(req.topic, req.platform)
    thumbnail = generate_thumbnail_url(req.topic, req.description or "")
    return GenerateResponse(caption=caption, hashtags=hashtags, thumbnail=thumbnail)