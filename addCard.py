lastName = None
while True:
    name = input("What is the id code?\n")
    if name == "":
        name = lastName
    else:
        lastName = name

    cardFile = open(name+"/index.html", "r")
    data = cardFile.read()
    cardFile.close()

    index = data.index("Own")
    count = int(data[index+4:index+5])+1
    data = data[:index+4]+str(count)+data[index+5:]

    cardFile = open(name+"/index.html", "w")
    cardFile.write(data)
    cardFile.close()
