from fastapi import FastAPI, Query
from typing import Optional
from app.services.unscrambler import find_valid_words
from app.services.meaning import get_meaning_of_word
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://192.168.1.3:3000"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/unscramble")
async def unscramble(word: str,
    start_with: Optional[str] = Query(None, alias="start"),
    end_with: Optional[str] = Query(None, alias="end"),
    contains: Optional[str] = Query(None),
    length: Optional[int] = Query(None)):
    return find_valid_words(word, start_with, end_with, contains, length)

@app.get("/meaning")
async def get_meaning(word: str):
    print(get_meaning_of_word(word))
    return get_meaning_of_word(word)

