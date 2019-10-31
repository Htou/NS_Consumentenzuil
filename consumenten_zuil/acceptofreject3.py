import datetime
import time

while True:
    infile = open('berichten.txt', 'r')
    content = infile.readlines()
    infile.close()

    if len(content) != 0:
        print(str(content))

        while True:
            jugement = input('Type accept of reject ')
            if jugement == 'accept':
                print('accepted en geplaatst op twitter')

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

                r = api.request('statuses/update', {'status': content})
                print(r.status_code)

                break
            elif jugement == 'reject':
                x = datetime.datetime.now()
                outfile = open('tekstfile.txt', 'a')
                outfile.write('{1} - {2}: {0} \n'.format(str(content), x.strftime("%Y-%m-%d"), x.strftime("%H:%M:%S")))
                outfile.close()
                break
            else:
                print("error, typ accept of reject")

    outfile1 = open('berichten.txt', 'w')
    outfile1.write('')
    outfile1.close()

    time.sleep(6)
