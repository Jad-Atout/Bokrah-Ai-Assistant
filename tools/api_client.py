import requests
from utils.config import BASE_URL, AUTH_HEADER


def post(endpoint: str, body: dict):
    return requests.post(f"{BASE_URL}{endpoint}", json=body, headers=AUTH_HEADER).json()


def get(endpoint: str):
    return requests.get(f"{BASE_URL}{endpoint}", headers=AUTH_HEADER).json()


def patch(endpoint: str, body: dict):
    return requests.patch(f"{BASE_URL}{endpoint}", json=body, headers=AUTH_HEADER).json()
