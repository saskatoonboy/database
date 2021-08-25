# print barcodes at 130% scale

import os
import math

def getCheck(barcode):
    num1 = 0
    num2 = 0
    
    for dig in range(0,12):
        digit = int(barcode[dig])
        if dig % 2 == 0:
            num1 = num1 + digit
        else:
            num2 = num2 + digit
            
    num2 = num2*3
    check = 10 - ((num1+num2)%10)
    if check == 10:
        check = 0
        
    return str(check)

barcodesFile = open("barcodes.txt", "r")
barcodes = []
for line in barcodesFile:
    barcodes.append(line[0:len(line)-1])
barcodesFile.close()
colours = ["blue", "black", "red", "green", "white"]
editions = ["eighth edition", "dragon's maze", "magic 2013", "magic 2011", "magic 2010", "mirage", "avacyn restored",
            "battle for zendikar", "shards of alara", "magic 2012", "innistrad", "eventide", "shadows over innistrad",
            "scars of mirrodin", "sorin vs tibalt", "duels of the planeswalkers", "dark ascension", "fire and lightning",
            "return to ravnica", "new phyrexia", "coldsnap", "mirrodin besieged", "magic 2014", "saviors of kamigawa",
            "theros", "gatecrash", "zendikar", "torment", "seventh edition", "saviors of kamigawa", "onslaught",
            "eternal masters", "blessed vs cursed","zendikar vs eldrazi", "born of the gods", "worldwake", "magic 2015",
            "nemesis", "fourth edition"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
while True:
    cardName = input("Name\n")
    edition = input("Edition\n")
    color = input("Colour\n")
    rarity = input("Rarity\n")
    cardType = input("Type\n")
    imageAddress = input("Image\n")

    part1 = str(alphabet.find(cardName[0].lower()))

    if len(part1) < 2:
        part1 = "0" + part1

    part2 = str(editions.index(edition.lower()))

    while (len(part2) < 3):
        part2 = "0" + part2
    
    uniqueCode = part1 + str(colours.index(color.lower())) + part2
    barcode = uniqueCode + "000000"
    count = -1
    while barcode in barcodes:
        count = count + 1
        countString = str(count)
        while len(countString) < 6:
            countString = "0" + countString
        barcode = uniqueCode + countString

        if (os.path.exists("/Users/eric/Documents/GitHub/database/"+barcode+getCheck(barcode)+"/index.html")):
            testFile = open("/Users/eric/Documents/GitHub/database/"+barcode+getCheck(barcode)+"/index.html", "r")
            contents = testFile.read()
            testFile.close()
            testName = contents[119:]
            char = 0
            testEdition = ""
            while char < len(testName):
                if testName[char] == "<":
                    testEdition = testName[char:]
                    testEdition = testEdition[16:]
                    testName = testName[:char]
                char = char + 1
                
            char = 0
            while char < len(testEdition):
                if testEdition[char] == "<":
                    testEdition = testEdition[:char]
                char = char + 1
                
            if cardName == testName and edition == testEdition:
                print(barcode)
                thing = 100/0
        
    barcodes.append(barcode)
    print(barcode)
    barcodesFile = open("barcodes.txt", "a")
    barcodesFile.write(barcode+"\n")
    barcodesFile.close()
    
    
    barcode = barcode + getCheck(barcode)
            
    os.mkdir("/Users/eric/Documents/GitHub/database/"+barcode+"/")
    dataFile = open("/Users/eric/Documents/GitHub/database/"+barcode+"/index.html", "w")
    data = """<!DOCTYPE HTML>
<html>
    <head>
        <title>Eric's mtg database</title>
    </head>
    <body>
        
      <h1>"""+cardName+"""</h1>
      <h2>"""+edition+"""</h2>
      <h2>"""+color+"""</h2>
      <h2>"""+rarity+"""</h2>
      <h2>"""+cardType+"""</h2>
      <h3>Own 0</h3>
      <img src="""+imageAddress+""">

    </body>
</html>"""
    
    dataFile.write(data)
    dataFile.close()
        
    files = os.listdir("../database")
    loadFile = open("load.js", "a")
                        
    loadFile.write("new CardEntry(\""+barcode+"\", '"+cardName+"', '"+color+"', '"+rarity+"', '"+edition+"');\n")

    loadFile.close()

# eighth edition - 0
# dragon's maze - 1
# magic 2013 - 2
# magic 2011 - 3
# magic 2010 - 4
# mirage - 5
# avacyn restored - 6
# battle for zendikar - 7
# shards of alara - 8
# magic 2012 - 9
# inistrad - 10
# eventide - 11
# shadows over inistrad - 12
# scars of mirrodin - 13
# sorin vs tibalt - 14
# duels of the planeswalkers - 15
# dark ascension - 16
# fire and lightning - 17
# return of ravnica - 18
# new phyrexia - 19
# coldsnap - 20
# mirrodin besieged - 21
# magic 2014 - 22
# saviors of kamigawa - 23
# theros - 24
# gatecrash - 25
# zendikar - 26
# torment - 27
# seventh edition - 28
# saviors of kamigawa - 29
# onslaught - 30
# eternal masters - 31
# blessed vs cursed - 32
# zendikar vs eldrazi - 33
# born of the gods - 34
# worldwake - 35
# magic 2015 - 36
# nemesis - 37
# fourth edition - 38
