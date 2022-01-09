
import newCard
import addCard
import removeCard
import getCardData
import math

def getType(code):
    split = code.lower().split()
    rawSplit = code.split()
    index = 0
    output = ""
    for segment in split:
        if index == 0:
            if segment == "e":
                output = output + "Enchantment "
            elif segment == "s":
                output = output + "Sorcery "
            elif segment == "i":
                output = output + "Instant "
            elif segment == "c":
                output = output + "Creature "
            elif segment == "ec":
                output = output + "Enchantment Creature "
            else:
                output = output + rawSplit[0] + " "
        elif index == 1:
            output = output + "- "
            if split[0] == "e" and segment == "a":
                output = output + "Aura "
            elif split[0] == "c" or split[0] == "ec":
                subCreatures = ["Bird", "Griffin", "Wall", "Angel", "Cat", "Spirit", "Human", "Elephant", "Pegasus", "Fox", "Kithkin", "Elf",
                                "Insect", "Plant Hound", "Hound", "Beast", "Dryad", "Elk", "Wolf", "Snake", "Fungus", "Bear", "Spider",
                                "Rhino", "Centaur", "Crocodile Frog", "Satyr", "Wurm", "Crocodile", "Basilisk", "Boar", "Plant", "Eldrazi",
                                "Sliver"]
                creatureCodes = ["bd", "g", "wl", "a", "ct", "sp", "hu", "ep", "pe", "fx", "k", "ef", "i", "plho", "ho", "be", "d", "ek", "wf",
                                 "sn", "fg", "br", "sd", "r", "ce", "cf", "sy", "wm", "cd", "ba", "bo", "pl", "el", "sl"]
                if segment in creatureCodes:
                    output = output + subCreatures[creatureCodes.index(segment)] + " "
                else:
                    output = output + rawSplit[1] + " "
                
            else:
                output = output + rawSplit[1] + " "
        elif index == 2:
            if split[0] == "c":
                subTypes = ["Warrior Ally", "Warrior", "Monk", "Horror", "Druid", "Scout", "Scout Ally", "Shaman", "Drone", "Werewolf"]
                typeCodes = ["waal", "wa", "m", "h", "dr", "sc", "scal", "sh", "do", "ww"]
                if segment in typeCodes:
                    output = output + subTypes[typeCodes.index(segment)] + " "
                else:
                    output = output + rawSplit[2] + " "
            else:
                output = output + rawSplit[2] + " "
        else:
            output = output + rawSplit[index] + " "
        
        index = index + 1
        
    return output
    
    
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
        edition = input("Edition\n")
        #color = input("Colour\n")
        #rarity = input("Rarity\n")
        kind = getType(input("Type\n"))
        #name = "Plains"
        #edition = "Magic 2012"
        color = "Green"
        rarity = "Common"
        #kind = "Basic Land - Plains"
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
        
    elif args[0] == "test":
        print(getType(input()))
            
