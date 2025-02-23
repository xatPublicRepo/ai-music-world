import openai
import tweepy

# Set up OpenAI API
openai.api_key = "your_openai_api_key"

# Set up Twitter API (X API)
twitter_api_key = "your_twitter_api_key"
twitter_api_secret = "your_twitter_api_secret"
twitter_access_token = "your_twitter_access_token"
twitter_access_secret = "your_twitter_access_secret"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)
api = tweepy.API(auth)

# Fetch trending hashtags
def get_trending_hashtags(woeid=1):  # woeid=1 is for worldwide trends
    trends = api.get_place_trends(woeid)
    hashtags = [trend["name"] for trend in trends[0]["trends"] if trend["name"].startswith("#")]
    return hashtags[:5]  # Get top 5 trending hashtags

# Generate song lyrics using GPT
def generate_lyrics(hashtags):
    prompt = f"Write a creative song lyrics based on these trending hashtags: {', '.join(hashtags)}. Make it catchy and poetic!"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Main execution
hashtags = get_trending_hashtags()
lyrics = generate_lyrics(hashtags)

print("🎶 Trending Hashtags-Based Lyrics 🎶")
print(lyrics)