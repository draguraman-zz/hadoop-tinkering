with open("./apsrc_2000_split/apsrc_2000.txt", mode="r") as bigfile:
    reader = bigfile.read()
    for i,part in enumerate(reader.split("AP88")):
        with open("./apsrc_2000_split/splitDocs_" +str(i+1)+".txt", mode="w") as newfile:
            newfile.write("AP88"+part)


