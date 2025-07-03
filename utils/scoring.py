import textstat

def readability_score(text):
    try:
        score = textstat.flesch_reading_ease(text)
        return round(score / 10, 2)  # Normalize to 0–10 scale
    except:
        return 0

def keyword_match_score(response, prompt):
    keywords = [word.lower() for word in prompt.split() if len(word) > 3]
    count = sum(1 for word in keywords if word in response.lower())
    return round(min(count / len(keywords) * 10, 10), 2)

def length_score(text):
    length = len(text.split())
    if length > 40:
        return 10
    elif length > 20:
        return 7
    elif length > 10:
        return 5
    else:
        return 2
