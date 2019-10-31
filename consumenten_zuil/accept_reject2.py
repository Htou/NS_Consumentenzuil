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


def twitter(message):