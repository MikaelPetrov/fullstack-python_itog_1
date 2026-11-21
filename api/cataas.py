import requests

from utils.url import transform_to_query_str


def get_image(text: str, params: dict):
    query_string = transform_to_query_str(params)

    url = f"https://cataas.com/cat/cute/says/{text}?{query_string}"
    print(f"LOG: URL - {url}")

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    return response.content
