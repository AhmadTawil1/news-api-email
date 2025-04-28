# 📰 Daily News Email Automation

A **Python-based automation tool** that fetches the latest news using **NewsAPI** and sends it via email.  
This project enables users to receive **daily news summaries** in their inbox.

## 📌 Features
✔ **Fetches real-time news using NewsAPI**  
✔ **Formats news articles into structured email content**  
✔ **Sends automated emails via SMTP**  
✔ **Customizable to fetch news based on topics**  
✔ **Configurable date range for news articles**  
✔ **UTF-8 support for international news**

## 🛠️ Setup

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd news-api-email
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Unix/MacOS
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root with the following variables:
   ```
   NEWS_API_KEY=your_news_api_key
   EMAIL_USERNAME=your_email@gmail.com
   EMAIL_PASSWORD=your_app_specific_password
   RECEIVER_EMAIL=recipient@email.com
   ```

## ⚙️ Configuration

- Edit `main.py` to change the news topic and date range
- Configure email settings in `send_email.py`
- The default configuration fetches news from the last 30 days

## 🚀 Usage

1. **Manual Execution**
   ```bash
   python main.py
   ```

2. **Automated Execution (Windows)**
   - Use the provided `run_news_fetcher.bat` file
   - Set up a Windows Task Scheduler to run it daily

## 🔒 Security Notes

- Never commit your API keys or email credentials
- Use app-specific passwords for Gmail
- Keep your `.env` file secure and never share it

## 📝 Requirements

- Python 3.7+
- NewsAPI account and API key
- Gmail account with app-specific password
- Required Python packages (see requirements.txt)

## 🤝 Contributing

Feel free to submit issues and enhancement requests!
