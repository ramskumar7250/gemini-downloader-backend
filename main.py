from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Framer (UI) से कनेक्शन के लिए CORS ऑन करना जरूरी है
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # अभी टेस्टिंग के लिए सबको अलाउ किया है
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

@app.post("/get-video/")
async def get_video_link(data: VideoRequest):
    input_url = data.url
    
    if not input_url:
        raise HTTPException(status_code=400, detail="URL की जरूरत है")
    
    try:
        # यहाँ बाद में हमारा स्क्रैपिंग लॉजिक आएगा जो वाटरमार्क हटाएगा
        # अभी टेस्टिंग के लिए हम वही लिंक वापस भेज रहे हैं
        direct_video_url = input_url
        
        return {"status": "success", "download_url": direct_video_url}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))