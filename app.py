import requests
import colours

spacex = requests.get("https://api.spacexdata.com/v3/ships")

def pri(colour, text):
    print(colours.getColour(colour) + text)

for ship in spacex.json() :

    name=ship["ship_name"]
    type=ship["ship_type"]
    roles=ship["roles"]

    pri("LIGHT_BLUE", name)
    pri("BLUE", type)
    for role in roles :
        pri("GREEN", role)   
    
    print("\n")


