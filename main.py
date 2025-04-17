"""
main.py: Third project with Engeto Online Python Akademie,
this script will scrape results from web from elections in 2017 in Czechia for 
specified region. How to use the script, see README.md
author: Lukáš Karásek
e-mail: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""

import sys
import csv
import os
import requests
from bs4 import BeautifulSoup

import scraper_language as slang

link_base = "https://www.volby.cz/pls/ps2017nss/"
link_elections = link_base + "ps3?xjazyk=CZ"

def load_all_tables(webpage: str):
    """Load all table tags from a provided link and return them as a list.

    Args:
        webpage (str): Link to a webpage to be scraped.

    Returns:
        list: List of table tags
    """

    try:
        html_source = requests.get(webpage)

        if html_source.status_code == 200:
            pass  # successfully loaded
        elif html_source.status_code == 404:
            print(slang.language[slang.lang]["error_404"])
            print(slang.language[slang.lang]["address_check"].format(webpage))
            sys.exit()
        else:
            print(slang.language[slang.lang]["error_unknown"].format(html_source.status_code))
            sys.exit()
    except requests.exceptions.RequestException as e:
        print(slang.language[slang.lang]["request_error"].format(e))
        sys.exit()

    html_beautifulsoup = BeautifulSoup(html_source.text, 'html.parser')

    # Find all table tags on page and return them (list of tables),
    # if there is no <table> tag: exit the script
    tables = html_beautifulsoup.find_all('table')
    if len(tables):
        return tables
    else:
        print(slang.language[slang.lang]["missing_table_tag"])
        print(slang.language[slang.lang]["address_check"].format(webpage))
        sys.exit()

def get_links_to_districts(webpage: str):
    """Scrape links to all regions from the provided webpage and return them as a dictionary with pairs: "name of region": "link"

    Args:
        webpage (str): Link to webpage with election results

    Returns:
        dict: Dictionary of all regions {"name of region": "link"}
    """

    tables = load_all_tables(webpage)
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

def get_links_to_town_results(link_town_results: str):
    """Scrape all towns and it's code and link from the link

    Args:
        link_town_results (str): Link to region from district_link list

    Returns:
        dict: {'town_name': ('code', 'link')}
    """

    tables = load_all_tables(link_town_results)
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

def scrape_results_for_town(link_to_town: str):
    """Scrape registred electors, envelopes, valid votes, all party names and their votes for one town.

    Args:
        link_to_town (str): Link to one town in choosen region from towns_list from district_link list

    Returns:
        tuple: (registred_electors, envelopes, valid_votes, tuple(party_names), tuple(party_votes))
    """
    tables = load_all_tables(link_to_town)

    # scrape registed electors (<td> with 'sa2' headers), envelopes ('sa3') 
    # and valid votes ('sa6') 
    # (they all are in first table on the page)
    registred_electors = tables[0].find('td', {'headers': 'sa2'}).getText()
    envelopes = tables[0].find('td', {'headers': 'sa3'}).getText()
    valid_votes = tables[0].find('td', {'headers': 'sa6'}).getText()

    party_names = []
    party_votes = []

    # cycle through tables (skip first table where there are no party results)
    for e, table in enumerate(tables[1:]):
        # set counters for party name (td with header t*sb1) and votes (td with t*sb3) - * = order of table
        party_name_header =  f't{e + 1}sb2'
        party_vote_header =  f't{e + 1}sb3'

        # store all party names and all results (order is same in both lists)
        all_party_names = table.find_all('td', {'headers': party_name_header, 'class': 'overflow_name'})
        all_party_votes = table.find_all('td', {'headers': party_vote_header, 'class': 'cislo'})

        for name, votes in zip(all_party_names, all_party_votes):
            party_names.append(name.getText())
            party_votes.append(votes.getText())

    return (registred_electors, envelopes, valid_votes, tuple(party_names), tuple(party_votes))

def collect_results(towns_list: str):
    """Collect data for all towns in choosen region. And store them in list of lists, where each list represents one row.

    Args:
        towns_list (str): Link to all town's in choosen region.

    Returns:
        list: list of lists, where each list represents one row \n
        order: ['code', 'location', 'registred', 'envelopes', 'valid', '1st_party_name', '2nd_party_name', ... ,'nth_party_name']
        
    """
    towns_list = {key: towns_list[key] for key in list(towns_list.keys())[:2]} # testing line - shorten towns_list to avoid too many requests while testing

    row_results_header = ["code", "location", "registred", "envelopes", "valid"]
    results_for_all_town = list()
    results_for_all_town.append(row_results_header)

    for e, (town, code_and_link) in enumerate(towns_list.items()):
        temp_row = [code_and_link[0], town]
        temp_results_for_town = scrape_results_for_town(code_and_link[1])

        # store first three values (registed electors, envelopes and valid votes)
        for temp_town_number in temp_results_for_town[:3]:
            temp_row.append(temp_town_number)

        # adding party names and votes to row
        for party_name, party_votes in zip(temp_results_for_town[3], temp_results_for_town[4]):
            # only for the first time add party names to header (which is already added to results_for_all_town)
            if e == 0:
                row_results_header.append(party_name)
            temp_row.append(party_votes)
        
        # add actual row to the list of all rows
        results_for_all_town.append(temp_row)
    return results_for_all_town

def save_csv(file_name, results):
    """Save '.csv' file with provided file name and return True if file exists

    Args:
        file_name (str): Name of file to be saved (*.csv)
        results (list): List of lists - rows to be saved

    Returns:
        bool: Returns true if file exists after savig
    """

    with open(file_name, mode='w', encoding='utf-8') as results_file:
        results_writer = csv.writer(results_file)
        results_writer.writerows(results)

    # Check if file was created and send it as result
    return os.path.isfile(file_name)

if __name__ == "__main__":
    # Set the language
    if sys.argv[-1] in ("--english", "--en"):
        slang.change_language("en")
    elif len(sys.argv) > 3:
        print(slang.language[slang.lang]["unsupported_lang"])

    # Check for number of arguments 
    if len(sys.argv) < 3:
        print(slang.language[slang.lang]["no_argv"])
        sys.exit()

    # Load links for all districts to a dictionary
    district_list = get_links_to_districts(link_elections)

    # Output list of reginos
    if sys.argv[1].lower() in ("seznam", "list"):
        for district in district_list.keys():
            print(district)
        sys.exit()

    # Get a file name from 2nd argument
    if sys.argv[2][-4:] == '.csv':
        results_file_name = sys.argv[2].strip('-')
    else:
        results_file_name = sys.argv[2].strip('-') + '.csv'

    # Process requested district, if it is existing one
    if sys.argv[1] in district_list:
        district_link = district_list[sys.argv[1]]

        # Get list of towns for the district and scrape results for each
        towns_list = get_links_to_town_results(district_link)
        print(slang.language[slang.lang]["progress"])
        results = collect_results(towns_list)

        # Save results to the csv file and if it exists, print message
        save_status = save_csv(results_file_name, results)
        
        if save_status:
            print(slang.language[slang.lang]["successfully_saved"].format(results_file_name))

        # If the region is not in the list
    else:
        print(slang.language[slang.lang]["missing_district"].format(sys.argv[1]))