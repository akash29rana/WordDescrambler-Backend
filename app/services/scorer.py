POINTS = {
    **dict.fromkeys("aeioulnstr", 1),
    **dict.fromkeys("dg", 2),
    **dict.fromkeys("bcmp", 3),
    **dict.fromkeys("fhvwy", 4),
    "k": 5,
    **dict.fromkeys("jx", 8),
    **dict.fromkeys("qz", 10)
}

def calculate_score(word):
    return sum(POINTS.get(c, 0) for c in word.lower())

