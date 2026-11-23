import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

# Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. 
# Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!


def pokedex():
    pokemonfindtype = []
    lang = "english"
    while True:
        print("1: Rechoose language" "2: print all pokemon names" "3: Search based on type" "4: Search based on name" "5: Move finder")
        action = int(input("Type the number of the action you want to do."))
        if action == 1:
            lang = input("Choose the language you want to use. The options are English, Japanese, Chinese, French.").lower()
        if action == 2:
                for pokemon in data:
                    print(pokemon["name"][lang])
        if action == 3: 
            pokemonfindtype = []
            type1 = input("Type the frist type you want pokemon for.")
            type2 = input("Type the second type you want pokemon for.")
            for pokemon in data:
                 if type1 in pokemon["type"] and type2 in pokemon["type"]:
                    pokemonfindtype.append(pokemon["name"][lang])
            if len(pokemonfindtype) == 0:
                print("Nothing found")
            else: print(pokemonfindtype)
        if action == 4:
            findname = input("fnid")
            if findname.lower() in pokemon(["name"]):
                print
pokedex()