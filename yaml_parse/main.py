import yaml
import json

with open ("app.yaml", "r") as stream:
    try:
        menu = yaml.load(stream)
        print(menu["name"])
        print(menu["location"])
        print("=========")
        print("Menu")
        for meal in menu["menu"]:
            print(meal["name"]+ " - £" + str(meal["price"]))
    except yaml.YAMLError as exc:
        print(exc)
