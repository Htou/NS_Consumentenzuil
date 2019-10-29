while True:
    invul = input("geef ons een berichtje :)")
    if len(invul) > 140:
        print("ERROR give an imput of max 140 characters")
    else:
        break

outfile = open('berichten.txt', 'a')
outfile.write(invul + '\n')
