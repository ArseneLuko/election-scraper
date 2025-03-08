"""
scraper.py: third project with Engeto Online Python Akademie,
this script will scrape...
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""

import sys
import scraper_functions

language = {
    "no_argv": "Nezadali jste žádný argument. Pro nápovědu se podívejte do souboru README.md. Program ukončen.",
    "missing_district": "Region » {} « není v seznamu regionů. Pro vypsání regionů spusťte skript s argumentem: seznam",
    "successfully_saved": "Soubor » {} « byl úspěšně uložen.",
    "progress": "Stahuji vyžádané data, chvíli to může trvat..."
}

if __name__ == "__main__":
    # load links for all districts
    district_list = scraper_functions.get_links_to_districts(scraper_functions.link_elections)
    
    # quit if no arguments were given 
    if len(sys.argv) == 1:
        print(language["no_argv"])
        sys.exit()

    # output list of reginos
    if sys.argv[1].lower() == "seznam":
        # TODO call it as a function
        for district in district_list.keys():
            print(district)
        sys.exit()
    
    # process requested district, if it is existing one
    if sys.argv[1] in district_list:
        district_link = district_list[sys.argv[1]]

        # get list of towns for the district and crape results for each to results
        towns_list = scraper_functions.get_links_to_town_results(district_link)
        print(language["progress"])
        results = scraper_functions.collect_results(towns_list)

        # save results to a file
        # check for 2nd argument
        if len(sys.argv) > 2: 
            results_file_name = sys.argv[2] + '.csv'
        else:
            results_file_name = 'results.csv'

        # save results to a csv file
        save_status = scraper_functions.save_csv(results_file_name, results)
        
        if save_status:
            print(language["successfully_saved"].format(results_file_name))

    else:
        print(language["missing_district"].format(sys.argv[1]))