while True:
    """"Input met maximaal 140 tekens, die naar berichten.txt schrijft"""

    invul = input("geef ons een berichtje: ")
    if len(invul) > 140:
        print("ERROR geef maximaal een input van 140 characters")
    else:
        break

outfile = open('berichten.txt', 'a')
outfile.write(invul + '\n')
outfile.close()



