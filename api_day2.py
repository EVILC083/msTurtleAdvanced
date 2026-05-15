import webbrowser
import requests


pokemon_name = input("Enter a Pokemon name: ").strip().lower()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
response = requests.get(url, timeout=15)

if response.status_code == 200:
	data = response.json()
	photo_url = data["sprites"]["front_default"]

	print("\n--- Pokemon Info ---")
	print("Name:", data["name"].title())
	print("ID:", data["id"])
	print("Height:", data["height"])
	print("Weight:", data["weight"])

	if photo_url:
		print("Photo URL:", photo_url)
		open_photo = input("Open photo in browser? (y/n): ").strip().lower()
		if open_photo == "y":
			webbrowser.open(photo_url)
			print("Opened Pokemon photo in your browser.")
	else:
		print("No photo is available for this Pokemon.")
else:
	print("Pokemon not found.")