from datetime import datetime, timedelta
from typing import Dict

import tweepy
from tweepy import API, Status
from tweepy.models import ResultSet

pinned_tweet_id: str = "1315626771874635778"


def is_older_than_2_weeks(tweet):
    date_tweet: datetime = tweet.created_at
    two_weeks_ago = datetime.now() - timedelta(days=14)
    return date_tweet < two_weeks_ago


def is_not_pinned(tweet: Status):
    return tweet.id != pinned_tweet_id


def delete(tweet: Status):
    tweet.destroy()


authent_dict: Dict = {
    "Consumer API Keys": {
        "API key": "***",
        "API secret key": "***"
    },
    "Access token & access token secret": {
        "Access token": "***",
        "Access token secret": "***"
    }
}


class TweetsSuppressor:

    def __init__(self) -> None:
        auth = tweepy.OAuthHandler(authent_dict["Consumer API Keys"]["API key"],
                                   authent_dict["Consumer API Keys"]["API secret key"])
        auth.set_access_token(authent_dict["Access token & access token secret"]["Access token"],
                              authent_dict["Access token & access token secret"]["Access token secret"])
        self.api = tweepy.API(auth)

    def get_tweets(self, page_id: int) -> ResultSet:
        return self.api.user_timeline(page=page_id, count=100)

    def delete_older_tweets(self):
        for page_id in range(3, 10000):
            tweets = self.get_tweets(page_id)
            if len(tweets)==0:
                print('fini!')
                break
            for tweet in tweets:
                if is_older_than_2_weeks(tweet) and is_not_pinned(tweet):
                    print(f"{tweet.text=} \n {tweet.created_at.isoformat()=}")
                    delete(tweet)
