import requests
from bs4 import BeautifulSoup

# L'URL de la page que vous souhaitez scraper
url = "https://fbref.com/fr/equipes/054efa67/Statistiques-Bayern-Munich"
#url = "https://fbref.com/fr/equipes/e2d8892c/Statistiques-Paris-Saint-Germain"

# Envoyer une requête GET pour récupérer la page
response = requests.get(url, verify=False)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Utiliser BeautifulSoup pour analyser la page
    soup = BeautifulSoup(response.text, 'html.parser')
    #cela ne marchera pas car il faudra garder l'id par championnat (div_stats_standard_ : 20 pour la bundes, 13 pour la ligue 1....)
    # Trouver le div avec l'ID "div_stats_standard_20"
    div_stats = soup.find('div', {'id': 'div_stats_standard_20'})

    if div_stats:
        # Trouver la table "stats_standard_20" à l'intérieur du div
        table = div_stats.find('table', {'id': 'stats_standard_20'})

        if table:
            # Trouver le tbody de la table
            tbody = table.find('tbody')

            if tbody:
                # Parcourir les lignes (tr) dans le tbody
                for row in tbody.find_all('tr'):
                    # Trouver l'élément "th" dans chaque ligne
                    th_element = row.find('th')

                    if th_element:
                        # Extraire le lien (href) contenu dans l'élément "th"
                        href = th_element.find('a')['href']
                        print(href)
        else:
            print("Table 'stats_standard_20' introuvable.")
    else:
        print("Div 'div_stats_standard_20' introuvable.")
else:
    print("La requête a échoué avec le code", response.status_code)
