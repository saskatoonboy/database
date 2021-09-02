import os

files = os.listdir()

for name in files:
    
    if not (("." in name) or name == "CNAME"):
        
        file = open(name+"/index.html", "r")
        data = file.read()
        file.close()
        
        if not ("$</h3>" in data):
            
            index = data.index("<h3>")
            data = data[:index] + "<h3>0.00$</h3>\n      " + data[index:]
            file = open(name + "/index.html", "w")
            file.write(data)
            file.close()
