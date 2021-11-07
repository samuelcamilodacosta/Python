import json
#create dicionary
dicionary = {
    "CHAVES":["CHAVES DO 8", "14/11/2021", "ROOM_01"],
    "QUICO":["QUICO FLORES", "20/11/2021", "ROOM_02"],
    "FLORINDA":["DONA FLORINDA", "18/11/2021", "ROOM_02"]
}

#create json
with open("Chapter 5/File Json/bd1.json", "w") as json_file:
    json.dump(dicionary,json_file)

#read json
with open("Chapter 5/File Json/bd.json", "r") as file_json:
    dicionary = json.load(file_json)
    for key, dates in dicionary.items():
        print(key + " : " + str(dates))