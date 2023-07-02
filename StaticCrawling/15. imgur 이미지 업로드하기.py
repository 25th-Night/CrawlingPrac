import json
import os
from pathlib import Path

from bs4 import BeautifulSoup as BS
import requests as req

# python "StaticCrawling/15. imgur 이미지 업로드하기.py"

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# SECRET
SECRET_DIR = BASE_DIR / ".secrets"
secrets = json.load(open(os.path.join(SECRET_DIR, 'secret.json')))
IMGUR_UPLOAD_URL = secrets["IMGUR_UPLOAD_URL"]
print(IMGUR_UPLOAD_URL)


url = IMGUR_UPLOAD_URL

# 이미지 읽어오기
image_path = "static/img/python.png"

with open(image_path, "rb") as f:
    img = f.read()


files = {
    "image": img,
    "type": "file",
    "name": "python.png"
}
res = req.post(url, files=files)


print(res.status_code)
print(res.text)

# status_code
# 200 -> 성공
# 400 -> 보내는 사람 잘못
# 500 -> 받는 사람 잘못

#
res_dict = res.json()
link = res_dict["data"]["link"]
print(link)

html = f"""
<html>
<head>
    <title>방금 업로드한 이미지</title>
</head>
<body>
<img src="{link}">
</body>
</html>
"""

with open("image.html", "w") as f:
    f.write(html)
