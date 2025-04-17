"""
scraper_html_functions.py: part of the project 03 in Engeto "Election Scraper", main script file: main.py
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek__77224
"""

import os

lang = "cz"

language = {
    "cz": {
        "no_argv": "Nezadali jste potřebný počet argumentů. Pro nápovědu se podívejte do souboru README.md. Program ukončen.",
        "missing_district": "Region » {} « není v seznamu regionů. Pro vypsání regionů spusťte skript s argumentem: seznam",
        "successfully_saved": "Soubor » {} « byl úspěšně uložen.",
        "progress": "Stahuji vyžádané data, chvíli to může trvat...",
        "request_error": "Nastala chyba modulu 'request' při pokusu našíst obsah. Chyba:\n{}",
        "missing_table_tag": "Na zadané adrese se nenachází předpokládaná data (tag <table>)",
        "address_check": "Zkontrolujte požadovanu adresu:\n{}",
        "error_404": "Chyba: Stránka nenalezena (404)",
        "error_unknown": "Chyba: Neznámá chyba ({})",
        "unsupported_lang": "Unsupported language. Continue in czech. / Nepodporovaný jazyk, pokračuji v četině.",
        "no_primary_file": "Soubor » {} « není hlavní soubor. Spusťe skript » main.py « / File » {} « is not the main file. Run the script » main.py «"
    },
    "en": {
        "no_argv": "You did not provide the required number of arguments. For help, please refer to the README.md file. Program terminated.",
        "missing_district": "Region » {} « is not in the list of regions. To display the regions, run the script with the argument: list.",
        "successfully_saved": "The file » {} « has been successfully saved.",
        "progress": "Downloading requested data, this may take a moment...",
        "request_error": "An error occurred in the 'request' module while trying to retrieve content. Error:\n{}",
        "missing_table_tag": "The expected data (tag <table>) is not found at the specified address",
        "address_check": "Please check the requested address:\n{}",
        "error_404": "Error: Page not found (404)",
        "error_unknown": "Error: Unknown error ({})",
        "unsupported_lang": "Unsupported language. Continue in czech. / Nepodporovaný jazyk, pokračuji v četině.",
        "no_primary_file": "Soubor » {} « není hlavní soubor. Spusťe skript » main.py « / File » {} « is not the main file. Run the script » main.py «"
    }
}

def change_language(choosen_lang: str):
    """Set the languege by changing global variable 'lang'

    Args:
        choosen_lang (str): two character code for language
    """
    global lang
    lang = choosen_lang

if __name__ == "__main__":
    print(language[lang]["no_primary_file"].format(os.path.basename(__file__), os.path.basename(__file__)))