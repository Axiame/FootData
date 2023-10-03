import requests
from bs4 import BeautifulSoup

id_suffix = {"PL": "9", "Ligue1": 13, "Bundesliga": 20, "SerieA": 11, "LaLiga": 12}

def scrape_player_links(url, league_suffix):
    # Liste pour stocker les liens récupérés
    player_links = []

    # Extraire le nom de l'équipe de l'URL
    team_name = url.split('Statistiques-')[-1].split('/')[0]

    # Ajouter le nom de l'équipe au début de la liste
    player_links.append(team_name)

    # Envoyer une requête GET pour récupérer la page
    response = requests.get(url, verify=False)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Utiliser BeautifulSoup pour analyser la page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Construire les identifiants en fonction du suffixe fourni
        div_id = f'div_stats_standard_{league_suffix}'
        table_id = f'stats_standard_{league_suffix}'

        # Trouver le div avec l'ID construit
        div_stats = soup.find('div', {'id': div_id})

        if div_stats:
            # Trouver la table avec l'ID construit à l'intérieur du div
            table = div_stats.find('table', {'id': table_id})

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
                            # Ajouter le lien à la liste
                            player_links.append("https://fbref.com"+href)
    else:
        print("La requête a échoué avec le code", response.status_code)

    return player_links  # Retourner la liste des liens

# Exemple d'utilisation :
url = "https://fbref.com/fr/equipes/18bb7c10/Statistiques-Arsenal"
league_suffix = id_suffix["PL"]  # Utiliser le suffixe de la Premier League
player_links = scrape_player_links(url, league_suffix)
for link in player_links:
    print(link)
