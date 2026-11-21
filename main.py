import os
import time
import json

from dotenv import load_dotenv

from api.cataas import get_image
from api.yandex import create_folder, upload_file

from utils.file import safe_filename

# Загружаем переменные из файла .env в окружение
load_dotenv()

HEIGHT = int(os.getenv("HEIGHT", 300))
GROUP_NAME = os.getenv("GROUP_NAME", "group")
JSON_FILE = "cats_info.json"


def main():
    t = time.time_ns() // 1_000_000
    params = {"height": HEIGHT, "t": t}

    text = input("Введите текст для картинки: ").strip()
    file_name = f"{safe_filename(text)}.jpg"

    data = get_image(text, params)

    create_folder(GROUP_NAME)
    upload_file(f"/{GROUP_NAME}/{file_name}", data)

    report = [{"file_name": file_name, "size": len(data)}]
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Файл {file_name} загружен в папку {GROUP_NAME}, размер: {len(data)} байт.")
    print(f"Информация сохранена в {JSON_FILE}.")


if __name__ == "__main__":
    main()
