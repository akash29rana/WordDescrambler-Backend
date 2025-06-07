import requests
from app.core.config import get_redis
import time

def get_meaning_of_word(word: str) -> str:
    result = {}
    result["word"] = word
    
    # redis_client = get_redis()
    # cached = redis_client.get(f"meaning:{word}")
    # if cached:
    #     result["meaning"] = cached
    #     return result
       
    try:
        res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}", timeout=2)
        if res.status_code == 200:
            data = res.json()
            meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
            # redis_client.setex(f"meaning:{word}", 86400, meaning)  # cache for 1 day
            result["meaning"] = meaning + "akash"
            return result
    except:
        pass

    # redis_client.setex(f"meaning:{word}", 86400, "No meaning found.")
    result["meaning"] = "No meaning found.akash"
    return result
