import oauth2 as oauth
import json

from pip._internal.commands.list import tabulate


def Request(url, key, secret, http_method='GET', post_body=b'', http_headers=None):
    consumer = oauth.Consumer(key="IGS3kyp7lo1WoIaF9e1eUY8jK",
                              secret="AldbB9aspuKtKJghFJKHAlicth2s0dKABNqChFP9qmOHeiEyHg")
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)
    request = client.request(
        url,
        method=http_method,
        body=post_body,
        headers=http_headers)

    return request


request, response = Request(
    'https://api.twitter.com/1.1/search/tweets.json?q=from%3AConsumentenzui1',
    '1189156220092989443-BPUYdAsgmq1V08PWQtfZh3siFZ2Gwb',
    'vggdKmRTfljwEms7virGlmg57PRE9hqBC5aZ4tFqfeHm0')

data = json.loads(response)
tweets = data['statuses']


def fetch_tweets():
    posts = list()
    for post in data['statuses']:
        posts.append([post['text'], post['created_at'], post['user']['screen_name']])
    print(posts)


fetch_tweets()
