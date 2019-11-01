import oauth2 as oauth
import json


def Request(url, key, secret, http_method='GET', post_body=b'', http_headers=None): #Request en authenticatie
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
    'https://api.twitter.com/1.1/search/tweets.json?q=from%3AConsumentenzui1', #pakt twitter data via API
    '1189156220092989443-BPUYdAsgmq1V08PWQtfZh3siFZ2Gwb',
    'vggdKmRTfljwEms7virGlmg57PRE9hqBC5aZ4tFqfeHm0')

data = json.loads(response)  # laad data via response
tweets = data['statuses']   #maakt obect van data


def fetch_tweets():
    "Pakt tweets, datums en gebruikts uit tweets:data, deze worden geformateerd naar strings en elk op een eigen regel gezet als 1 object,"
    posts = list()
    for post in data['statuses']:
        posts.append("{}'\n'{}'\n'{}".format(post['text'], post['created_at'], post['user']['screen_name'])) #tweets, datums en users worden bewaard in een list: posts
    return (posts)