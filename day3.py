import requests

pokemon_name = input("Enter a Pokémon name: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n--- Pokémon Info ---")
    print("Name:", data["name"].title())
    print("ID:", data["id"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])
    print("\nTypes:")

for type_info in data["types"]:
    print("-", type_info["type"]["name"])
else:
    print("Pokémon not found.")
    for type_info in data["types"]:
        print("-", type_info["type"]["name"])
    for type_info in data["types"]:
        print(data["abilities"])
        print("\nAbilities:")

for ability_info in data["abilities"]:
    print("-", ability_info["ability"]["name"])
    print(data["stats"])
    print("\nBase Stats:")

for stat_info in data["stats"]:
    stat_name = stat_info["stat"]["name"]
    stat_value = stat_info["base_stat"]
    print(f"- {stat_name}: {stat_value}")
    for stat_info in data["stats"]:
        stat_name = stat_info["stat"]["name"]
        stat_value = stat_info["base_stat"]
        print(f"- {stat_name}: {stat_value}")

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    def display_pokemon(data):
     print("\n========================")
    print("      Pokémon Info")
    print("========================")

    print("Name:", data["name"].title())
    print("ID:", data["id"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])

    print("\nTypes:")
    for type_info in data["types"]:
        print("-", type_info["type"]["name"].title())

    print("\nAbilities:")
    for ability_info in data["abilities"]:
        print("-", ability_info["ability"]["name"].title())

    print("\nBase Stats:")
    for stat_info in data["stats"]:
        stat_name = stat_info["stat"]["name"]
        stat_value = stat_info["base_stat"]
        print(f"- {stat_name.title()}: {stat_value}"
              while True:
    pokemon_name = input("\nEnter a Pokémon name or ID, or type 'quit': ").lower()

    if pokemon_name == "quit":
        print("Goodbye!")
        break

    data = get_pokemon_data(pokemon_name)

    if data:
        display_pokemon(data)
    else:
        print("Pokémon not found. Please try again.")
        strongest_stat = ""
strongest_value = 0

for stat_info in data["stats"]:
    stat_name = stat_info["stat"]["name"]
    stat_value = stat_info["base_stat"]

    if stat_value > strongest_value:
        strongest_value = stat_value
        strongest_stat = stat_name

print("\nStrongest Stat:")
print(f"{strongest_stat.title()}: {strongest_value}")
battle_score = 0

for stat_info in data["stats"]:
    stat_name = stat_info["stat"]["name"]
    stat_value = stat_info["base_stat"]

    if stat_name == "attack" or stat_name == "defense" or stat_name == "speed":
        battle_score += stat_value

print("\nBattle Score:", battle_score)
save = input("Save this Pokémon to favorites? yes/no: ").lower()

if save == "yes":
    with open("favorites.txt", "a") as file:
        file.write(data["name"].title() + "\n")

    print("Saved to favorites.txt!")
    first = input("Enter the first Pokémon: ")
second = input("Enter the second Pokémon: ")

first_data = get_pokemon_data(first)
second_data = get_pokemon_data(second)
def calculate_battle_score(data):
    battle_score = 0

    for stat_info in data["stats"]:
        stat_name = stat_info["stat"]["name"]
        stat_value = stat_info["base_stat"]

        if stat_name == "attack" or stat_name == "defense" or stat_name == "speed":
            battle_score += stat_value

    return battle_score
    print("\n========================")
print("      Pokémon Info")
print("========================")
# This function gets Pokémon data from the API
def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    response.json()def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
        import requests

def get_pokemon_data(pokemon_name):
    # function code here

def display_pokemon(data):
    # function code here

while True:
    # main program code here
while True:
pokemon_name = input("Enter a Pokémon: ")data = get_pokemon_data(pokemon_name)
display_pokemon(data)
data = get_pokemon_data(pokemon_name)

if data:
    display_pokemon(data)
else:
    print("Pokémon not found.")