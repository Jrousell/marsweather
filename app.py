import requests
import colours
import matplotlib.pyplot as plt

ships = requests.get("https://api.spacexdata.com/v3/ships")
rockets = requests.get("https://api.spacexdata.com/v3/rockets")


def pri(colour, text, colour2, text2):
    print(colours.getColour(colour) + text, colours.getColour(colour2) + text2)

def basic():
    for ship in ships.json():

        name=ship["ship_name"]
        type=ship["ship_type"]
        roles=ship["roles"]

        pri("LIGHT_BLUE", name)
        pri("BLUE", type)
        for role in roles :
            pri("GREEN", role)   
        
        print("\n")

def getRocketData():

    _rockets = []
    _masses = []

    for rocket in rockets.json():
        _rockets.append(rocket["rocket_name"])
        _masses.append(rocket["mass"]["kg"])

    return {
        "rockets": _rockets, 
        "masses": _masses
    }

rocketData = getRocketData()

fig, ax = plt.subplots()

rockets = rocketData["rockets"]
masses = rocketData["masses"]

bar_labels = rockets
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(rockets, masses, label=bar_labels, color=bar_colors)
ax.set_ylabel('Weight in KG')
ax.set_title('SpaceX Rocket Weights by Name and Mass')
ax.legend(title='Fruit color')

plt.show()