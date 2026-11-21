import os
import requests

from dotenv import load_dotenv

# Загружаем переменные из файла .env в окружение
load_dotenv()

GROUP_NAME = os.getenv("GROUP_NAME", "group")
YANDEX_API = os.getenv("YANDEX_API", "")
OAUTH_TOKEN = os.getenv("OAUTH_TOKEN", "")


def create_folder(folder):
    params = {"path": f"/{folder}"}
    headers = {"Authorization": f"OAuth {OAUTH_TOKEN}"}

    response = requests.put(YANDEX_API, headers=headers, params=params, timeout=30)
    if response.status_code != 409:  # 409 означает, что папка уже существует
        response.raise_for_status()


def upload_file(remote_path, data):
    params = {"path": remote_path, "overwrite": "true"}
    headers = {"Authorization": f"OAuth {OAUTH_TOKEN}"}

    response = requests.get(
        f"{YANDEX_API}/upload",
        headers=headers,
        params=params,
        timeout=30,
    )
    response.raise_for_status()

    upload = requests.put(response.json()["href"], data=data, timeout=60)
    upload.raise_for_status()
