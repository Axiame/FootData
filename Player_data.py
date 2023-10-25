import requests
from bs4 import BeautifulSoup

def scrape_player_stats(url):
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
        # Ignorer les lignes spécifiées
        if index in [12, 16, 17, 34, 35, 61, 62, 81, 82, 100, 101, 121, 122, 149, 150]:
            continue

        # Extraire le texte du premier élément <th> dans la ligne (nom de la statistique)
        th_element = row.find("th")
        stat_name = th_element.get_text(strip=True)

        # Extraire le texte du premier élément <td> dans la ligne (valeur de la statistique)
        td_elements = row.find_all("td", class_="right")
        stat_value = td_elements[0].get_text(strip=True)  # Premier élément <td> contient la valeur

        # Ajouter la paire clé-valeur au dictionnaire
        stats_dict[stat_name] = stat_value

    # Supprimer l'entrée vide s'il y en a une
    stats_dict.pop('', None)

    # Parcourir le dictionnaire de statistiques pour convertir les valeurs
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

    return stats_dict  # Retourner le dictionnaire des statistiques
print(scrape_player_stats("https://fbref.com/en/players/810e3c74/Jesse-Lingard"))

