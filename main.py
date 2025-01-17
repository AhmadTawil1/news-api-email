import requests
from send_email import send_email
from datetime import date, timedelta

# Get today's date
today = date.today()

# Subtract 30 days
thirty_days_ago = today - timedelta(days=30)

# Format the result in 'YYYY-MM-DD'
formatted_date = thirty_days_ago.strftime('%Y-%m-%d')

topic = "Nvidia"

api_key = '68653f5221de4df1b55da6010dbd9029'
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       f"from={formatted_date}&"
       "sortBy=publishedAt&" 
       "apiKey=68653f5221de4df1b55da6010dbd9029&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
message = ""
for article in content["articles"][:20]:
    if article["title"] and article["description"] and article["url"] is not None:
        title = article["title"]
        description = article["description"]
        link = article["url"]
        sep = "---------------------------------------------"
        message += title + "\n" + description + "\n" + link + "\n" + sep + "\n"

print(message)
send_email(message)

