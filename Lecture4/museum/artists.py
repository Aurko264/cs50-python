import requests

def get_artist(query, limit):
    try:
        response = requests.get(
            "http://api.artic.edu/api/v1/agents/search", {"q": query, "lim": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return[]

    content = response.json()
    return [artist["title"] for artist in content["data"]]