from bs4 import BeautifulSoup
import csv
import requests

url = 'https://archives.marist.edu/LTP/Graphic%20Materials/Roberson2.1.1.1/panama2.1.1.1.18.xml'
xml = requests.get(url)
soup = BeautifulSoup(xml.content, 'xml')

file = open('test.csv', 'w')
writer = csv.writer(file)


c01 = soup.find('c01')
subject = c01.unittitle.text

for c02 in soup.find_all('c02'):
    unitid = c02.unitid.text
    unittitlec02 = c02.unittitle.text
    box = c02.container.text
    date = c02.unitdate.text

    ident = ['LTPGM',box,unitid]
    identifier = ('_'.join(ident))                                         #working identifier




    did = c02.find('did')
    index = did.find('materialspec', label='index').text
    negative = did.find('materialspec', label='negativenumber').text
    boolnum = bool(negative)

    numberlist =[index, negative]

    if boolnum == True:
        numberlist.insert(0, 'Index ')
        numberlist.insert(2, ' - Negative ')                                #working number
        number = (''.join(numberlist))
    else:
        numberlist.insert(0, 'Index ')
        number = (''.join(numberlist))




    inches = c02.extent.text
    f = []
    for i in inches:
        f.append(i)

    #No decimals
    #f.insert(1, '" ')                                                       #working format
    #f.insert(3, ' ')                                                        #may need to chaneg due to different things
    #f.insert(5, '"')

    #Decimals
    f.insert(3, '" ')
    f.insert(5, ' ')
    f.insert(9, '"')

    format = (''.join(f))





    creator = 'blank'
    collection = 'Lowell Thomas Graphic Materials'          # may need to change based on what collection
    medium  = 'Glass Plate Negative'                        # may need to change based on what collection
    media = 'blank'


    #print(identifier, ' ', number, ' ', format, ' ', creator, ' ', subject, ' ', unittitlec02, ' ', collection, ' ', date, ' ', media)

    writer.writerow([identifier, number, format, creator, subject, unittitlec02, collection, date, medium, media])

file.close()