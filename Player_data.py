import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
#url = "https://fbref.com/fr/joueurs/0d7b6576/scout/365_m1/Rapport-de-scouting-Elye-Wahi"
url = "https://fbref.com/fr/joueurs/21a66f6a/scout/365_m1/Rapport-de-scouting-Harry-Kane"
# Envoyer une requête et récupérer le contenu HTML
response = requests.get(url, verify=False)
html_content = response.content

# Analyser le contenu HTML avec Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Trouver le <tbody> à l'intérieur de la classe "table_container tabbed current is_setup"
table_container = soup.find(id="scout_full_FW")
tbody = table_container.find("tbody")

# Initialiser le dictionnaire
stats_dict = {}

# Trouver tous les éléments <tr> dans le <tbody>
data_rows = tbody.find_all("tr")

# Parcourir les lignes de données
for index, row in enumerate(data_rows):
    # Ignorer les lignes avec les numéros 16 et 17
    if index ==12 or index == 16 or index == 17 or index == 34 or index == 35 or index == 61 or index == 62 or index == 81 or index == 82 or index == 100 or index == 101 or index == 121 or index == 122 or index == 149 or index == 150:
        continue

    # Extraire le texte du premier élément <th> dans la ligne (nom de la statistique)
    th_element = row.find("th")
    stat_name = th_element.get_text(strip=True)

    # Extraire le texte du premier élément <td> dans la ligne (valeur de la statistique)
    td_elements = row.find_all("td", class_="right")
    stat_value = td_elements[0].get_text(strip=True)  # Premier élément <td> contient la valeur

    # Ajouter la paire clé-valeur au dictionnaire
    stats_dict[stat_name] = stat_value
    print(stats_dict)
# Imprimer le dictionnaire complet
print(stats_dict)
print(len(stats_dict))
#afficher toutes les clés du dictionnaire
print(stats_dict.keys())
# Parcourir le dictionnaire de statistiques
del(stats_dict[''])
for stat_name, stat_value in stats_dict.items():
    if "%" in stat_value:
        stat_value = stat_value.replace("%", "")
        stat_value = float(stat_value) / 100  # Convertir en décimal
        stats_dict[stat_name] = stat_value  # Mettre à jour la valeur dans le dictionnaire

for stat_name, stat_value in stats_dict.items():
    try:
        stat_value = float(stat_value)
        stats_dict[stat_name] = stat_value
    except ValueError:
        print("Impossible de convertir la valeur en nombre flottant", stat_name)
# Imprimer le dictionnaire mis à jour
print(stats_dict)




