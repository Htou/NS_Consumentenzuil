import time

vorige = 0

while True:
    infile = open('berichten.txt', 'r')
    content = infile.readlines()
    print(type(content))
    infile.close()

    listMessages = []
    counter = 0
    for lines in content:
        counter += 1
        listMessages.append(lines)

    if vorige < counter:
        new = listMessages[-1]
        print(new)
        vorige = counter
    else:
        vorige = counter
        pass
    time.sleep(6)
