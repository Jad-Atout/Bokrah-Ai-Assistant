import os

import requests
from utils.config import BASE_URL

BEARER = os.environ['BEARER']
def _build_headers(token: str = None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"{BEARER}{token}"
    return headers


def post(endpoint: str, body: dict, token: str = None):
    return requests.post(
        f"{BASE_URL}{endpoint}",
        json=body,
        headers=_build_headers(token)
    ).json()


def get(endpoint: str, token: str = None):
    return requests.get(
        f"{BASE_URL}{endpoint}",
        headers=_build_headers(token)
    ).json()


def patch(endpoint: str, body: dict, token: str = None):
    return requests.patch(
        f"{BASE_URL}{endpoint}",
        json=body,
        headers=_build_headers(token)
    ).json()
