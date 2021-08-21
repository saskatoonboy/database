import os

files = os.listdir("../database")

for file in files:
    if (not ("." in file or file == "CNAME")):
        ID = file
        file = open(ID+"/index.html","r")
        data = file.read()
        file.close()
        index = data.index("</h3>")+5
        data = data[:index] + "\n      <h3>Spare Codes 0</h3>" + data[index:]
        
        file = open(ID+"/index.html","w")
        file.write(data)
        file.close()
