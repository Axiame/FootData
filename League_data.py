import requests
from bs4 import BeautifulSoup

# L'URL de la page à scraper
url = 'https://fbref.com/fr/comps/9/Statistiques-Premier-League'

# Effectuer une requête GET pour obtenir le contenu de la page
response = requests.get(url)
response.raise_for_status()  # Vérifier que la requête a réussi

# Analyser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Naviguer vers le div contenant la table
table_container = soup.find('div', id ='div_results2023-202491_overall')

if table_container is None:
    raise ValueError("Le div contenant la table n'a pas été trouvé.")

# Trouver la table dans le div
table = table_container.find('table', id = 'results2023-202491_overall')

if table is None:
    raise ValueError("La table n'a pas été trouvée dans le div.")

# Accéder au tbody de la table
tbody = table.find('tbody')

if tbody is None:
    raise ValueError("Le tbody n'a pas été trouvé dans la table.")

# Extraire les URLs des équipes
team_urls = []
for row in tbody.find_all('tr'):
    # Trouver l'élément "td" dans chaque ligne
    td_element = row.find('td')

    if td_element:
        a_tag = td_element.find('a')
        if a_tag and 'href' in a_tag.attrs:
            # Extraire le lien (href) contenu dans l'élément "td"
            href = a_tag['href']
            team_urls.append(href)
        else:
            print("Aucun lien trouvé dans la ligne.")

# Afficher les URLs
for url in team_urls:
    print(url)
