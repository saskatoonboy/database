import os

while True:

    name = input("Name\n")

    files = os.listdir("../database")

    for file in files:
        if (not ("." in file or file == "CNAME")):
            barcode = file
            
            file = open(barcode+"/index.html","r")
            data = file.read()
            file.close()
            
            openCommand = False
            openCommandNext = False
            isHeader = False
            text = ""
            values = []
            for index in range(len(data)):
                char = data[index]
                if char == "<":
                    command = data[index+1:index+3]
                    if command == "h1" or command == "h2":
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
                    values.append(text)
                    text = ""
            if len(values) > 1:
                if name.lower() in values[0].lower():
            
                
                    print(values[0] + " - " + values[1] + ": " + barcode)
