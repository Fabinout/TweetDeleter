from datetime import datetime
from unittest import TestCase

from tweepy import Status

from delete_old_tweets import is_older_than_2_weeks


class TestTweetsSuppressor(TestCase):

    def test_is_not_older_than_2_weeks(self):
        tweet = Status()
        tweet.created_at = datetime.now()
        self.assertFalse(
            is_older_than_2_weeks(tweet))

    def test_is_older_than_2_weeks(self):
        tweet = Status()
        tweet.created_at = datetime(day=6, month=10, year=1975)
        self.assertTrue(
            is_older_than_2_weeks(tweet))
