import requests
from send_email import send_email

api_key = '68653f5221de4df1b55da6010dbd9029'
url = ("https://newsapi.org/v2/everything?q=tesla" 
       "&from=2024-12-10&sortBy=publishedAt&" 
       "apiKey=68653f5221de4df1b55da6010dbd9029")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
message = ""
for article in content["articles"]:
    if article["title"] is not None:
        title = article["title"]
        description = article["description"]
        sep = "---------------------------------------------"
        message += title + "\n" + description + "\n" + sep + "\n"

print(message)
send_email(message)

