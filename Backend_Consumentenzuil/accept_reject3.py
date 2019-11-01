import datetime
import time

while True:
    infile = open('berichten.txt', 'r') #open berichten.txt als read
    content = infile.readlines()        #lees alle lines van het bestand en stop die waarden in content. het type van content is een list
    infile.close()

    if len(content) != 0:       #als het aantal objecten in de list content ongelijk is aan 0, gebeurt het volgende
        print(str(content))     #print het bericht dat in het bestand staat

        while True:
            jugement = input('Type accept of reject ')      #de gebruiker typt iets in, dit word aan de variabele jugement gegeven
            if jugement == 'accept':        #als de waarde van jugement gelijk is aan 'accept' gebeurt het volgende:
                print('accepted en geplaatst op twitter')       #print tekst

                import json

                credentials = {}    #maak een lege dictionary
                credentials['CONSUMER_KEY'] = 'IGS3kyp7lo1WoIaF9e1eUY8jK'   #vul bij de key 'CONSUMER_KEY' de waarde 'IGS3kyp7lo1WoIaF9e1eUY8jK'
                credentials['CONSUMER_SECRET'] = 'AldbB9aspuKtKJghFJKHAlicth2s0dKABNqChFP9qmOHeiEyHg' #vul bij de key de waardes
                credentials['ACCESS_TOKEN'] = '1189156220092989443-BPUYdAsgmq1V08PWQtfZh3siFZ2Gwb'
                credentials['ACCESS_SECRET'] = 'vggdKmRTfljwEms7virGlmg57PRE9hqBC5aZ4tFqfeHm0'

                with open('twitter_credentials.json', 'w') as file:     #open het bestand 'twitter_credentials.json' als write functie en noem dit 'file'
                    json.dump(credentials, file)        #schrijf in de 'file' de info die staat in de dictionary 'credentials'

                from TwitterAPI import TwitterAPI

                api = TwitterAPI('IGS3kyp7lo1WoIaF9e1eUY8jK',
                                 'AldbB9aspuKtKJghFJKHAlicth2s0dKABNqChFP9qmOHeiEyHg',
                                 '1189156220092989443-BPUYdAsgmq1V08PWQtfZh3siFZ2Gwb',
                                 'vggdKmRTfljwEms7virGlmg57PRE9hqBC5aZ4tFqfeHm0')   #twitterkeys, maakt het mogelijk om te plaatsen op switter

                r = api.request('statuses/update', {'status': content}) #plaats de inhoud van content (dus het bericht)  op twitter
                print(r.status_code)

                break
            elif jugement == 'reject':      #als de gebruiker 'reject'invult gebeurt het volgende:
                x = datetime.datetime.now()         #geef x de waarde van de datum en tijd van nu
                outfile = open('tekstfile.txt', 'a')        #open het bestand tekstfile.txt in append modus
                outfile.write('{1} - {2}: {0} \n'.format(str(content), x.strftime("%Y-%m-%d"), x.strftime("%H:%M:%S")))     #schrijf in de file de waarde van content (dus het berichtje), de datum en de tijd van nu
                outfile.close()
                break
            else:       #als er iets andere word ingevuld gebeurt het volgende:
                print("error, typ accept of reject")

    outfile1 = open('berichten.txt', 'w')       #open het bestand in schrijf functie
    outfile1.write('')      #schrijf niks in het bestand, hierdoor maak je het bestand leeg
    outfile1.close()

    time.sleep(6)       #wacht 6 seconden voor hij verder gaat
