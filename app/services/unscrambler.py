from itertools import permutations
from app.services.scorer import calculate_score


# import nltk
# nltk.download('wordnet')
# from nltk.corpus import wordnet



# word_list = set(word.name().split('.')[0] for word in wordnet.all_synsets())

# Load words.txt once
with open("app/data/words.txt") as f:
    ENGLISH_WORDS = set(w.strip().lower() for w in f if w.strip().isalpha())

def find_valid_words(input_word: str, start_with=None, end_with=None, contains=None, length=None):
    result = {}
    input_word = input_word.lower()

    for size in range( len(input_word),1,-1):
        perms = set(''.join(p) for p in permutations(input_word, size))
        valid = []

        for word in perms:
            if word not in ENGLISH_WORDS:
                continue
            if start_with and not word.startswith(start_with):
                continue
            if end_with and not word.endswith(end_with):
                continue
            if contains and contains not in word:
                continue
            if length and len(word) != length:
                continue

            valid.append({
                "word": word,
                "points": calculate_score(word)
            })

        if valid:
            result[f"{size}_letter_words"] = sorted(valid, key=lambda x: -x["points"])

    return result
