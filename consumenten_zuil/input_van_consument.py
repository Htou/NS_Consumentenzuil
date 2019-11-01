while True: #de volgende loop word steeds herhaald tot er uit de loop word gebroken:
    """"Input met maximaal 140 tekens, die naar berichten.txt schrijft"""

    invul = input("geef ons een berichtje: ")   #de gebuiker kan een berichtje achterlaten
    if len(invul) > 140:        #als het bericht meer dan 140 tekens bevat gebeurt het volgende:
        print("ERROR geef maximaal een input van 140 characters")
    else:   #als het minder of gelijk aan 140 tekens bevat gebeurt het volgende:
        break   #break uit de loop

outfile = open('berichten.txt', 'a')    #open het bestand berichten.txt met de functie append
outfile.write(invul + '\n')         #schrijf in het bestand de waarde van invul en een enter
outfile.close()     #sluit het bestand
