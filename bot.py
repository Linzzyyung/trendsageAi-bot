import os
import tweepy
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_api():
    client = tweepy.Client(
        consumer_key=os.getenv("TWITTER_API_KEY"),
        consumer_secret=os.getenv("TWITTER_API_SECRET"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    user = client.get_me(user_fields=["username"])
    logger.info(f"✅ Authenticated as @{user.data.username}")
    return client

def post_tweet(client, text="🚀 Hello from my bot! #PythonBot"):
    try:
        client.create_tweet(text=text)
        logger.info("✅ Tweet posted successfully.")
    except Exception as e:
        logger.error(f"❌ Failed to post tweet: {e}")

def main():
    client = create_api()
    post_tweet(client, text="📢 This is TrendSageAI tweeting live! #CryptoBot")

if __name__ == "__main__":
    main()
