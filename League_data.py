import requests
from bs4 import BeautifulSoup

def scrape_team_urls_PL():
    league_url = 'https://fbref.com/fr/comps/9/Statistiques-Premier-League'
    # Effectuer une requête GET pour obtenir le contenu de la page
    response = requests.get(league_url)
    response.raise_for_status()  # Vérifier que la requête a réussi

    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Naviguer vers le div contenant la table
    table_container = soup.find('div', id='div_results2023-202491_overall')

    if table_container is None:
        raise ValueError("Le div contenant la table n'a pas été trouvé.")

    # Trouver la table dans le div
    table = table_container.find('table', id='results2023-202491_overall')

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
                team_urls.append("https://fbref.com/"+href)
            else:
                print("Aucun lien trouvé dans la ligne.")

    # Renvoyer la liste des URLs
    return team_urls
def scrape_team_urls_Ligue1():
    league_url = 'https://fbref.com/fr/comps/13/Statistiques-Ligue-1'
    # Effectuer une requête GET pour obtenir le contenu de la page
    response = requests.get(league_url)
    response.raise_for_status()  # Vérifier que la requête a réussi

    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Naviguer vers le div contenant la table
    table_container = soup.find('div', id='div_results2023-2024131_overall')

    if table_container is None:
        raise ValueError("Le div contenant la table n'a pas été trouvé.")

    # Trouver la table dans le div
    table = table_container.find('table', id='results2023-2024131_overall')

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
                team_urls.append("https://fbref.com/"+href)
            else:
                print("Aucun lien trouvé dans la ligne.")

    # Renvoyer la liste des URLs
    return team_urls

def scrape_team_urls_Bundesliga():
    league_url = 'https://fbref.com/fr/comps/20/Statistiques-Bundesliga'
    # Effectuer une requête GET pour obtenir le contenu de la page
    response = requests.get(league_url)
    response.raise_for_status()  # Vérifier que la requête a réussi

    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Naviguer vers le div contenant la table
    table_container = soup.find('div', id='div_results2023-2024201_overall')

    if table_container is None:
        raise ValueError("Le div contenant la table n'a pas été trouvé.")

    # Trouver la table dans le div
    table = table_container.find('table', id='results2023-2024201_overall')

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
                team_urls.append("https://fbref.com/"+href)
            else:
                print("Aucun lien trouvé dans la ligne.")

    # Renvoyer la liste des URLs
    return team_urls

def scrape_team_urls_SerieA():
    league_url = 'https://fbref.com/fr/comps/11/Statistiques-Serie-A'
    # Effectuer une requête GET pour obtenir le contenu de la page
    response = requests.get(league_url)
    response.raise_for_status()  # Vérifier que la requête a réussi

    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Naviguer vers le div contenant la table
    table_container = soup.find('div', id='div_results2023-2024111_overall')

    if table_container is None:
        raise ValueError("Le div contenant la table n'a pas été trouvé.")

    # Trouver la table dans le div
    table = table_container.find('table', id='results2023-2024111_overall')

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
                team_urls.append("https://fbref.com/"+href)
            else:
                print("Aucun lien trouvé dans la ligne.")

    # Renvoyer la liste des URLs
    return team_urls

def scrape_team_urls_Liga():
    league_url = 'https://fbref.com/fr/comps/12/Statistiques-La-Liga'
    # Effectuer une requête GET pour obtenir le contenu de la page
    response = requests.get(league_url)
    response.raise_for_status()  # Vérifier que la requête a réussi

    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Naviguer vers le div contenant la table
    table_container = soup.find('div', id='div_results2023-2024121_overall')

    if table_container is None:
        raise ValueError("Le div contenant la table n'a pas été trouvé.")

    # Trouver la table dans le div
    table = table_container.find('table', id='results2023-2024121_overall')

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
                team_urls.append("https://fbref.com/"+href)
            else:
                print("Aucun lien trouvé dans la ligne.")

    # Renvoyer la liste des URLs
    return team_urls



