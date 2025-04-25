import wikipedia, json, os

CACHE_PATH = "data/cached_wiki.json"

def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r") as f:
            return json.load(f)
    return {}

def save_cache(data):
    with open(CACHE_PATH, "w") as f:
        json.dump(data, f)

def search_wikipedia(query: str) -> str:
    cache = load_cache()
    if query in cache:
        return cache[query]

    try:
        summary = wikipedia.summary(query, sentences=3)
        cache[query] = summary
        save_cache(cache)
        return summary
    except Exception as e:
        return f"Failed: {e}"
