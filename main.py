
import newCard
import addCard
import removeCard
import getCardData
import math

def getArgs(cmd):
    
    lastBreak = 0
    args = []
    for index in range(len(cmd)):
        char = cmd[index]
        if char == " ":
            arg = cmd[lastBreak:index]
            if not (arg == ""):
                args.append(arg)
            lastBreak = index+1
    arg = cmd[lastBreak:]
    if not (arg == ""):
        args.append(arg)
    return args

def addValue(value):

    valFile = open("value.txt", "r")
    totalValue = valFile.read()
    totalValue = float(totalValue)
    totalValue = totalValue + value
    totalValue = math.floor(totalValue * 100)/100
    valFile.close()
    valFile = open("value.txt", "w")
    valFile.write(str(totalValue))
    valFile.close()
    return totalValue


barcodeFile = open("barcodes.txt", "r")
barcodesData = barcodeFile.read()
barcodeFile.close()
barcodes = []

while len(barcodesData) > 0:
    index = barcodesData.index("\n")
    if index == -1:
        index = len(barcodesData)
    barcode = barcodesData[:index]
    if not (barcode in barcodes):
        barcodesData = barcodesData[index+2:]

barcodesData = ""

for barcode in barcodes:
    
    barcodesData = barcodesData + barcode + "\n"
    
barcodeFile = open("barcodes.txt", "w")
barcodeFile.write(barcodesData)
barcodeFile.close()

while True:
    
    cmd = input()
    
    args = getArgs(cmd)
    
    if args[0] == "new":
        
                
        name = input("Name\n")
        edition = input("Edition\n")
        color = input("Colour\n")
        rarity = input("Rarity\n")
        kind = input("Type\n")
        image = input("Image\n")
        value = input("Value\n")
        
        newCard.makeCard(name, edition, color, rarity, kind, image, value)
        
    elif args[0] == "add":
        
        code = input("Code\n")
        amount = 1
        if len(args) > 1:
            amount = int(args[1])
        
        addCard.addCard(code, amount)
        
    elif args[0] == "remove":
        
        code = input("Code\n")
        amount = 1
        if len(args) > 1:
            amount = int(args[1])
        
        removeCard.removeCard(code)
    elif args[0] == "get":
        if len(args) == 1:
            print("Need search string")
        else:
            getCardData.search(args[1])
            
    elif args[0] == "count":
        if len(args) == 1:
            print("Need code")
        else:
            file = open(args[1]+"/index.html", "r")
            data = file.read()
            file.close()
            amount = 1
            if len(args) > 2:
                amount = int(args[2])
            indexEnd = data.index("$</h3>\n")
            indexStart = data.index("<h3>")
            value = float(data[indexStart+4:indexEnd])
            print(addValue(value*amount))
            
