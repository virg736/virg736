import json
import requests
import re
import matplotlib.pyplot as plt
from datetime import datetime

# ---- Files ----
json_file = "profile-views.json"
chart_file = "profile-views-chart.png"
badge_file = "profile-views-badge.svg"

# ---- GitHub Username ----
USERNAME = "virg736"

# -----------------------------------------------------------
# 1. Récupérer le vrai compteur de vues depuis Komarev
# -----------------------------------------------------------
# Utilise la même URL que celle de ton badge GitHub (important !)
komarev_url = f"https://komarev.com/ghpvc/?username={USERNAME}&color=blue"
counter_svg = requests.get(komarev_url).text

# Extraire le nombre (accepte les virgules : 3,623)
match = re.search(r'>([\d,]+)<', counter_svg)

# Convertir en entier (supprimer la virgule)
views_today = int(match.group(1).replace(",", "")) if match else 0

print(f"[INFO] Views today extracted from Komarev: {views_today}")

# -----------------------------------------------------------
# 2. Charger le JSON existant
# -----------------------------------------------------------
with open(json_file, "r") as f:
    data = json.load(f)

today = datetime.now().strftime("%Y-%m-%d")

# Ajouter la nouvelle valeur
data["views"].append({"date": today, "count": views_today})

# Sauvegarde du JSON
with open(json_file, "w") as f:
    json.dump(data, f, indent=4)

print("[INFO] JSON updated successfully")

# -----------------------------------------------------------
# 3. Générer le graphique PNG
# -----------------------------------------------------------
dates = [v["date"] for v in data["views"]]
counts = [v["count"] for v in data["views"]]

plt.figure(figsize=(10, 5))
plt.plot(dates, counts)
plt.xlabel("Date")
plt.ylabel("Profile Views")
plt.title("GitHub Profile Views Evolution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(chart_file)

print("[INFO] Chart updated successfully")

# -----------------------------------------------------------
# 4. Mettre à jour le badge SVG personnalisé
# -----------------------------------------------------------
badge_svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="150" height="30">
  <rect width="150" height="30" fill="#555"/>
  <rect x="80" width="70" height="30" fill="#007ec6"/>
  <text x="10" y="20" fill="white" font-size="14">Profile views</text>
  <text x="95" y="20" fill="white" font-size="14">{views_today}</text>
</svg>
"""

with open(badge_file, "w") as f:
    f.write(badge_svg)

print(f"[INFO] Badge updated with {views_today} views.")