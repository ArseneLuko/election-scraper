"""
scraper.py: Third project with Engeto Online Python Akademie,
this script will scrape results from web from elections in 2017 in Czechia for 
specified region. How to use the script, see README.md
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""

import scraper_functions as sf

if __name__ == "__main__":
    # Set the language
    # If there is last argument --english or --en set the language to english
    if sf.sys.argv[-1] in ("--english", "--en"):
        sf.change_language("en")
    elif len(sf.sys.argv) > 3:
        print(sf.language[sf.lang]["unsupported_lang"])

    # Load links for all districts to a dictionary
    district_list = sf.get_links_to_districts(sf.link_elections)
    # district_list = sf.get_links_to_districts('http://httpbin.org/status/404') # testing line

    # Quit if no arguments were given 
    if len(sf.sys.argv) == 1:
        print(sf.language[sf.lang]["no_argv"])
        sf.sys.exit()

    # Output list of reginos
    if sf.sys.argv[1].lower() in ("seznam", "list"):
        for district in district_list.keys():
            print(district)
        sf.sys.exit()

    # Save results to a file
    # Check for 2nd argument, if missing create default file name.
    # If there is no '.csv' extension, it will be added
    # If there are only 2 arguments and last one is --en or --english (so missing file name the .strip() is used to set en.csv or english.csv as a file name)
    if len(sf.sys.argv) >= 3 and sf.sys.argv[2] not in ("--english", "--en"):
        if sf.sys.argv[2][-4:] == '.csv':
            results_file_name = sf.sys.argv[2].strip('-')
        else:
            results_file_name = sf.sys.argv[2].strip('-') + '.csv'
    else:
        results_file_name = 'results.csv'
    
    # Process requested district, if it is existing one
    if sf.sys.argv[1] in district_list:
        district_link = district_list[sf.sys.argv[1]]

        # Get list of towns for the district and scrape results for each town to results
        towns_list = sf.get_links_to_town_results(district_link)
        print(sf.language[sf.lang]["progress"])
        results = sf.collect_results(towns_list)

        # Save results to the csv file and if it exists, print message
        save_status = sf.save_csv(results_file_name, results)
        
        if save_status:
            print(sf.language[sf.lang]["successfully_saved"].format(results_file_name))

    # If the region is not in the list
    else:
        print(sf.language[sf.lang]["missing_district"].format(sf.sys.argv[1]))