import requests
from send_email import send_email

search_term = "tesla"
api_key = "XXXXXXX"
url = "https://newsapi.org/v2/everything?" \
      f"q={search_term}&" \
      "from=2023-06-30&sortBy=publishedAt&" \
      "apiKey=XXXXXXX&" \
      "language=en"

request = requests.get(url)
content = request.json()

message = "Subject: Today's News" + "\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = message + article["title"] + "\n" \
                  + article["description"] + "\n" \
                  + article["url"] + 2*"\n"

message = message.encode("utf-8")

send_email(message)
