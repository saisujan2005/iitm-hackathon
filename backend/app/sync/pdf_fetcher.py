import requests


def download_pdf(url: str):

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    return response.content