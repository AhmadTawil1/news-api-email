import requests

api_key = '68653f5221de4df1b55da6010dbd9029'
url = ("https://newsapi.org/v2/everything?q=tesla" 
       "&from=2024-12-10&sortBy=publishedAt&" 
       "apiKey=68653f5221de4df1b55da6010dbd9029")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])



