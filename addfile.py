import os 
import shutil
import csv 
import sys 

def process_file(filename, path, file_type):
    
    #stampa le informazioni del file 
    name = filename.split(".")
    size = os.path.getsize("{}/{}".format(path,filename))
    text = "{} type:{} size:{}B ".format(name[0],file_type, size)
    print(text)
    
    #scivo le informazioni nel file racap.csv
    with open("{}/recap.csv".format(path), "a", newline="") as file: 
        writer = csv.writer(file)
        writer.writerow( [name[0], "type:{}".format(file_type), "size:{} B".format(size)] )
    
    #se non c'è la cartella la crea
    if not os.path.isdir("{}\{}".format(path, file_type)): 
        os.mkdir("{}\{}".format(path, file_type))
    
    #muove il file 
    shutil.move("{}\{}".format(path, filename), "{}\{}".format(path, file_type))


filename = sys.argv[1]
if not os.path.isfile("files\{}".format(filename)):
    print("ERROR! {} does not exist".format(filename))
else:
    directory = r"files"
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            process_file(filename, directory, "images")
        if filename.endswith(".mp3"):
            process_file(filename, directory, "Audio")
        if filename.endswith(".txt") or filename.endswith("odt"):
            process_file(filename, directory, "docs")
        