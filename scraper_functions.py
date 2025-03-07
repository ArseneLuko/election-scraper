"""
scraper_html_functions.py: 
part of the project 03 in Engeto, main script file: scraper.py
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""

# TODO: possibility to change year (should work with change the link_base 
# valuable eg. https://www.volby.cz/pls/ps2017nss/ -> 
# https://www.volby.cz/pls/ps2021nss/)

# TODO: split get_links_to_districts() and 
# get_links_to_town_results(link_town_results):

# TODO: check for Response 200 

import csv
import requests
from bs4 import BeautifulSoup

link_base = "https://www.volby.cz/pls/ps2017nss/"
link_elections_2017 = link_base + "ps3?xjazyk=CZ"

def get_links_to_districts():
    """From the website volby.cz from results for year 2017 gets links
    to all districts (Okresy) and return them as a dictionary with
    pairs: "name of region": "link"
    """
    # load whole page to a variable and parse it
    html_source = requests.get(link_elections_2017)
    html_beautifulsoup = BeautifulSoup(html_source.text, 'html.parser')

    # find all table tags on page and save them to a variable (list of tables)
    tables = html_beautifulsoup.find_all('table')
    # now lenght of 'tables' is number of occurencies of the tag
    # print(len(tables)) # -> 14 in case of 2017

    # create a dictionary with pairs: name of a region 
    # and a link to its list of towns
    list_of_regions_and_links = {}
    for e, region in enumerate(tables):
        # link 'X' in 'td' with attribut header t*sa3 links to list of all towns in a district - all districts in regions has same attribute: t1sa3, t2sa3, ..., t14sa3 
        # same for the name of district in 'td' tag with header attribute t*sb2
        region_link_header = f't{e + 1}sa3'
        region_name_header = f't{e + 1}sb2'

        # get all td tags wraping links and names of distrits
        all_districts_code = region.find_all('td', {'headers': region_link_header})
        all_districts_name = region.find_all('td', {'headers': region_name_header})

        # get the link and district name and pair them in a dictionary
        for district_code, district_name in zip(all_districts_code, all_districts_name):
            link = district_code.find('a')['href']
            name = district_name.getText()
            list_of_regions_and_links[name] = link_base + link

    return list_of_regions_and_links

def get_links_to_town_results(link_town_results, save_codes=False):
    # load whole page to a variable and parse it
    html_source = requests.get(link_town_results)
    html_beautifulsoup = BeautifulSoup(html_source.text, "html.parser")

    # find all table tags on page and save them to a variable (list of tables)
    tables = html_beautifulsoup.find_all('table')

    # print(html_beautifulsoup.prettify())  # tessting line

    # create a dictionary with pairs: name of a town 
    # and a link to its results
    list_of_towns_and_links = {}
    for e, town in enumerate(tables):
        # link to results is in first collumn - <td> with header 
        # attribute 't*sb1' where the number at second position 
        # is counter for table, same for name 
        # of the town in <td header='t*sb2'>
        town_link_header = f't{e + 1}sb1'
        town_name_header = f't{e + 1}sb2'

        # get all td tags wrapping links and names of towns
        all_towns_code = town.find_all('td', {'headers': town_link_header, 'class': 'cislo'})
        all_towns_name = town.find_all('td', {'headers': town_name_header, 'class': 'overflow_name'})

        # get the link and town name and pair them in a dictionary
        for town_code, town_name in zip(all_towns_code, all_towns_name):
            link = town_code.find('a')['href']
            name = town_name.getText()
            list_of_towns_and_links[name] = (town_code.getText(), link_base + link)

    return list_of_towns_and_links

def scrape_results_for_town(link_to_town='https://www.volby.cz/pls/ps2017/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103'):
    # load whole page to a variable and parse it
    html_source = requests.get(link_to_town)
    html_beautifulsoup = BeautifulSoup(html_source.text, "html.parser")

    # find all table tags on page and save them to a variable (list of tables)
    tables = html_beautifulsoup.find_all('table')

    # scrape registed electors (td with 'sa2' headers), envelopes ('sa3') and valid votes ('sa6')
    registred_electors = tables[0].find('td', {'headers': 'sa2'}).getText()
    envelopes = tables[0].find('td', {'headers': 'sa3'}).getText()
    valid_votes = tables[0].find('td', {'headers': 'sa6'}).getText()

    return (registred_electors, envelopes, valid_votes)

def collect_results(towns_list):
    towns_list = {key: towns_list[key] for key in list(towns_list.keys())[:2]} # testing line - shoren towns_list to avoid too many requests

    row_results_header = ["code", "location", "registred", "envelopes", "valid"]
    results_for_all_town = list()
    results_for_all_town.append(row_results_header)

    for e, (town, code_and_link) in enumerate(towns_list.items()):
        temp_row = [code_and_link[0], town]
        temp_results_for_town = scrape_results_for_town(code_and_link[1])
        for temp_town_number in temp_results_for_town:
            temp_row.append(temp_town_number)
        results_for_all_town.append(temp_row)
    return results_for_all_town

def save_csv(file_name, results):
    results_file = open(file_name, mode='w', encoding='utf-8')
    results_writer = csv.writer(results_file)

    # temporary
    results_writer.writerows(results)
    # for row in results:
    #     results_writer.writerows(results)

    # results_writer.writerow(results[0])
    # results_writer.writerow(results[1])

    results_file.close()

if __name__ == "__main__":
    # temp_results = scrape_results_for_town('http://httpbin.org/status/404') # testing line
    # temp_results = scrape_results_for_town() # testing line

    pass
    

    
    