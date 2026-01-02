import tweepy
import os
import random

# Authentication using GitHub Secrets
client = tweepy.Client(
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
)

def get_tweet():
    # Similar style to Zeroplag
    messages = [
        "Is that essay due tonight? Let us handle the heavy lifting while you relax. 📝✨",
        "Top-tier academic assistance is just a DM away. Quality work, zero plagiarism. 🎓✅",
        "Don't let dissertation stress get to you. Reach out for professional help today! 📚🚀",
        "Need help with your online classes or research papers? We've got you covered. 💻💯"
    ]
    
    tags = "#AssignmentHelp #EssayDue #HomeworkHelp #DissertationHelp #AcademicTwitter"
    
    return f"{random.choice(messages)}\n\n{tags}"

try:
    tweet_text = get_tweet()
    client.create_tweet(text=tweet_text)
    print("Tweet posted successfully!")
except Exception as e:
    print(f"Error occurred: {e}")
