import requests
import os
import logging
from datetime import date, timedelta
from dotenv import load_dotenv
from send_email import send_email

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('news_fetcher.log'),
        logging.StreamHandler()
    ]
)

# Load environment variables
load_dotenv()

def fetch_news():
    try:
        # Get configuration from environment variables
        api_key = os.getenv('NEWS_API_KEY')
        topic = os.getenv('NEWS_TOPIC', 'Nvidia')  # Default to 'Nvidia' if not set
        days_back = int(os.getenv('NEWS_DAYS_BACK', '30'))  # Default to 30 days if not set

        if not api_key:
            raise ValueError("NEWS_API_KEY not found in environment variables")

        # Calculate date range
        today = date.today()
        start_date = today - timedelta(days=days_back)
        formatted_date = start_date.strftime('%Y-%m-%d')

        # Construct API URL
        url = (
            "https://newsapi.org/v2/everything?"
            f"q={topic}&"
            f"from={formatted_date}&"
            "sortBy=publishedAt&"
            f"apiKey={api_key}&"
            "language=en"
        )

        # Make request with error handling
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            content = response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching news: {str(e)}")
            return None

        # Validate API response
        if content.get('status') != 'ok':
            logging.error(f"News API error: {content.get('message', 'Unknown error')}")
            return None

        # Format message
        message = ""
        for article in content.get("articles", [])[:20]:
            if all(article.get(field) for field in ["title", "description", "url", "publishedAt"]):
                message += (
                    f"{article['title']}\n"
                    f"{article['description']}\n"
                    f"{article['publishedAt']}\n"
                    f"{article['url']}\n"
                    "---------------------------------------------\n"
                )

        if not message:
            logging.warning("No valid articles found")
            return None

        return message

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return None

def main():
    logging.info("Starting news fetch process")
    message = fetch_news()
    
    if message:
        try:
            send_email(message)
            logging.info("Email sent successfully")
        except Exception as e:
            logging.error(f"Error sending email: {str(e)}")
    else:
        logging.error("Failed to fetch news or no valid articles found")

if __name__ == "__main__":
    main()

