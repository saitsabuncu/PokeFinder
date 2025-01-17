import requests
import tkinter as tk
from tkinter import messagebox


def get_pokemon_data(pokemon_name):
    """
    Belirli bir Pokémon'un bilgilerini çeker.

    Args:
        pokemon_name (str): Bilgileri çekilecek Pokémon'un adı.

    Returns:
        dict: Pokémon bilgilerini içeren bir sözlük.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]]
        }
    else:
        return {"error": "Bu Pokémon bulunamadı!"}


def search_pokemon():
    """
    Kullanıcıdan alınan Pokémon adını kullanarak bilgileri ekranda gösterir.
    """
    pokemon_name = entry.get()
    if not pokemon_name:
        messagebox.showwarning("Hata", "Lütfen bir Pokémon adı girin!")
        return

    pokemon_data = get_pokemon_data(pokemon_name)
    if "error" in pokemon_data:
        messagebox.showerror("Hata", pokemon_data["error"])
    else:
        result_label.config(text=(
            f"Ad: {pokemon_data['name']}\n"
            f"Boy: {pokemon_data['height']} dm\n"
            f"Ağırlık: {pokemon_data['weight']} hg\n"
            f"Tipler: {', '.join(pokemon_data['types'])}\n"
            f"Yetenekler: {', '.join(pokemon_data['abilities'])}"
        ))


# Tkinter arayüzü oluşturma
window = tk.Tk()
window.title("Pokémon Bilgileri")
window.geometry("400x400")

# Giriş alanı
entry_label = tk.Label(window, text="Pokémon Adı:")
entry_label.pack(pady=10)
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Arama butonu
search_button = tk.Button(window, text="Ara", command=search_pokemon)
search_button.pack(pady=10)

# Sonuç etiketi
result_label = tk.Label(window, text="", justify="left", font=("Arial", 10))
result_label.pack(pady=20)

# Uygulama başlatma
window.mainloop()
