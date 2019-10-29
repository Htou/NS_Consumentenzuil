
import json

credentials = {}
credentials['CONSUMER_KEY'] = 'IGS3kyp7lo1WoIaF9e1eUY8jK'
credentials['CONSUMER_SECRET'] = 'AldbB9aspuKtKJghFJKHAlicth2s0dKABNqChFP9qmOHeiEyHg'
credentials['ACCESS_TOKEN'] = '1189156220092989443-BPUYdAsgmq1V08PWQtfZh3siFZ2Gwb'
credentials['ACCESS_SECRET'] = 'vggdKmRTfljwEms7virGlmg57PRE9hqBC5aZ4tFqfeHm0'

with open('twitter_credentials.json', 'w') as file:
    json.dump(credentials, file)

from TwitterAPI import TwitterAPI
api = TwitterAPI('IGS3kyp7lo1WoIaF9e1eUY8jK',
                 'AldbB9aspuKtKJghFJKHAlicth2s0dKABNqChFP9qmOHeiEyHg',
                 '1189156220092989443-BPUYdAsgmq1V08PWQtfZh3siFZ2Gwb',
                 'vggdKmRTfljwEms7virGlmg57PRE9hqBC5aZ4tFqfeHm0')

r = api.request('statuses/update', {'status':'This is a tweet!'})
print(r.status_code)