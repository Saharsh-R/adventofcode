import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://adventofcode.com/2023/day/1/input"
cookies = {"session": os.getenv("AOC_SESSION_COOKIE")}

response = requests.get(URL, cookies=cookies, timeout=5)

if response.status_code == 200:
    file_path = Path(__file__).resolve().parent / "d1_input.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)
        print("Data written to file successfully")
else:
    print(f"Failed to fetch data, status code: {response.status_code}")
