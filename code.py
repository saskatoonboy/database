import os

files = os.listdir("../database")
loadFile = open("load.js", "w")

for file in files:
    if (not ("." in file or file == "CNAME")):
        ID = file
        file = open(ID+"/index.html","r").read()
        print(file)
        openCommand = False
        openCommandNext = False
        isHeader = False
        text = ""
        values = []
        for index in range(len(file)):
            char = file[index]
            if char == "<":
                command = file[index+1:index+3]
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
                print(text)
                values.append(text)
                text = ""
                    
        loadFile.write("new CardEntry('"+ID+"', '"+values[0]+"', '"+values[2]+"', '"+values[3]+"', '"+values[1]+"');\n")
    
loadFile.close()
