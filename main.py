
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
    totalValue = int(totalValue)
    totalValue = totalValue + value
    valFile.close()
    valFile = open("value.txt", "w")
    valFile.write(str(totalValue))
    valFile.close()
    return totalValue

lastCode = ""

while True:
    
    cmd = input()
    
    args = getArgs(cmd)
    
    if args[0] == "new":
        
                
        name = input("Name\n")
        #edition = input("Edition\n")
        #color = input("Colour\n")
        #rarity = input("Rarity\n")
        kind = input("Type\n")
        #name = "Island"
        edition = "Magic 2012"
        color = "Blue"
        rarity = "Common"
        #kind = "Basic Land - Island"
        image = input("Image\n")
        value = input("Value\n")
        
        lastCode = newCard.makeCard(name, edition, color, rarity, kind, image, value)
        
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
            
            if args[1] == "last":
                args[1] = lastCode
            
            file = open(args[1]+"/index.html", "r")
            data = file.read()
            file.close()
            amount = 1
            if len(args) > 2:
                amount = int(args[2])
            indexEnd = data.index("$</h3>\n")
            indexStart = data.index("<h3>")
            value = int(data[indexStart+4:indexEnd].replace(".", ""))
            print(addValue(value*amount)/100)
    elif args[0] == "addCount":
        if len(args) > 1:
            print(addValue(int(args[1].replace(".", "")))/100)
            
