import requests
from simple_chalk import chalk, green, red, blue

spacex = requests.get("https://api.spacexdata.com/v3/ships")

LIGHT_PURPLE = "\033[1;35m"
PURPLE = "\033[0;35m"

for ship in spacex.json() :

    name=ship["ship_name"]
    type=ship["ship_type"]
    roles=ship["roles"]

    print(LIGHT_PURPLE + name, red(type), blue(roles))
