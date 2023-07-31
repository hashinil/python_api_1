import requests
from send_email import send_email

api_key = "XXXXXXX"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-06-30&sortBy=publishedAt&" \
      "apiKey=XXXXXXX"

request = requests.get(url)
content = request.json()

message =""
for article in content["articles"]:
    if article["title"] is not None:
        message = message + article["title"] + "\n" + article["description"] + 2*"\n"

message = message.encode("utf-8")

send_email(message)
