import League_data
import Team_data
import Player_data


url_pl = League_data.scrape_team_urls_PL()
url_bl = League_data.scrape_team_urls_Bundesliga()
url_l1 = League_data.scrape_team_urls_Ligue1()
url_sa = League_data.scrape_team_urls_SerieA()
url_ll = League_data.scrape_team_urls_Liga()
teamdata_pl = []
for url in url_pl:
    teamdata_pl.append(Team_data.scrape_player_links(url, Team_data.id_suffix["PL"]))

print(teamdata_pl)