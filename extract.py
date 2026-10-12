import requests
import csv

base_url = "https://brixhub.to/api/v1/search "
extraction_list_path = "./list.csv"
result_path = "./data"

with open(extraction_list_path, mode="r", encoding="utf-8", newline="") as fichier:
    reader = csv.DictReader(fichier)
    people_list = list(reader)
    #print(data)

def get_people_info(surname, name):
    print(f"Extraction des informations de : {name} {surname}")
    r = requests.post("https://api.brixhub.ru/api/v1/search", json={
    "nom_famille": name,
    "prenom": surname,
})  
    return r.json()


def get_peoples_info(people_list):
    for people in people_list:
        data = get_people_info(people["surname"], people["name"])

        with open(result_path + "/" + people["name"] + "_" + people["surname"] + ".json", 'w') as file:
            file.write(str(data))

get_peoples_info(people_list)