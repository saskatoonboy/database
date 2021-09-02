

def decodeData(dataFile, loadFile):
        
    file = dataFile.read()
    openCommand = False
    openCommandNext = False
    isHeader = False
    text = ""
    values = []
    for index in range(len(file)):
        char = file[index]
        if char == "<":
            command = file[index+1:index+3]
            if command == "h1" or command == "h2" or command == "h3":
                isHeader = True
            elif "/" in command:
                openCommand = False
                isHeader = False
            else:
                isHeader = False
        elif char == ">":
            if isHeader:
                openCommandNext = True
                        
        if openCommand and isHeader:
            text = text + char
                    
        if openCommandNext:
            openCommandNext = False
            openCommand = True
                    
        if (not openCommand) and (not text == ""):
            print(text)
            values.append(text)
            text = ""
                        
    loadFile.write("new CardEntry('"+barcode+"', '"+values[0]+"', '"+values[2]+"', '"+values[3]+"', '"+values[1]+"');\n")


def loadCard(barcode):

    loadFile = open("load.js", "r")
    loadData = loadFile.read()
    loadFile.close()

    if loadData.find(barcode) == -1:
        loadFile = open("load.js", "a")
        cardFile = open(barcode+"/index.html", "r")
        decodeData(cardFile, loadFile)
        loadFile.close()
        cardFile.close()
        
    else:
        print("barcode already loaded")
