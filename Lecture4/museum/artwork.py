import requests

def get_artworks(query, limit):
    try:
        response = requests.get(
            "http://api.artic.edu/api/v1/artworks/search", {"q": query, "lim": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return[]

    content = response.json()
    return [artwork["title"] for artwork in content["data"]]