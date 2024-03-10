import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

cookies = {"session": os.getenv("AOC_SESSION_COOKIE")}


parent_dir = Path(__file__).resolve().parent

for day in [2]:
    response = requests.get(
        f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies, timeout=5
    )
    if response.status_code == 200:
        file_path = parent_dir / f"d{day}" / f"d{day}_input.txt"
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)
            print("Data written to file successfully")
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")
        print(f"Error reason: {response.reason}")
