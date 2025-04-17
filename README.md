# Election scraper (Česky)

Jednoduchý skript, který stáhne výsledky pro všechny volební okrsky ve zvoleném okrese z roku 2017 ze stránek volby.cz a uloží je do csv souboru. Napsáno jako cvičení v rámci Engeto akademie: <https://engeto.cz>.

## Instalace requirements.txt
Nainstalujte si modul 'pip' -> <https://pip.pypa.io/en/stable/installation/><br>
Vytvořte ve zvoleném adresáři virtuální prostředí -> <https://docs.python.org/3/library/venv.html#creating-virtual-environments><br>
Pomocí ```pip install -r requirements.txt``` nainstalujte potřebné knihovny do zvoleného adresáře a do něj nakopírujte všechny soubory projektu (případně naklonujte pomocí git)

## Jak skript spustit
Spusťte skript `main.py` se dvěma argumenty: **názvem okresu**, pro který chcete výsledky (více podrobností níže) a **názevem CSV souboru**. Spuštění skriptu s jedním argumentem `seznam` vypíše všechny okresy. Primární jazyk je čeština; skript můžete spustit v angličtině pomocí `--en` nebo `--english` jako posledního argumentu.

### Příklady spuštění
Pro uložení výsledků z okresu Frýdek-Místek do souboru vysledky_z_FM.csv spusťe skript:<br>
```main.py Frýdek-Místek vysledky_z_FM.csv```<br>
Pokud chcete, aby skript komunikoval v angličtině, přidejte argument '--en':<br>
```main.py Frýdek-Místek vysledky_z_FM.csv --en```<br>
Pokud chcete výsledky pro okres, který obsahuje v názvu mezery, zadejte název okresu do uvozovek:<br>
```main.py 'Rychnov nad Kněžnou' vysledky_z_rychnova.csv```

## Argumenty

### Název okresu - první argument
Zadejte název okresu, použijte přesný název okresu (dodržujte diakritiku a velikost písmen): ```main.py 'Ústí nad Orlicí' usti_n_orlici.csv```<br>
Pro vypsání všech okresů spusťte ```main.py seznam```.

### Název souboru - druhý argument
Zadejte název souboru jako druhý argument. Můžete vynechat příponu '.csv'; ta bude automaticky přidána. ```main.py Praha vysledky-praha```

### Jazyk - poslední nepovinný argument
Pokud použijete '--en' nebo '--english' jako poslední argument, změní jazyk na angličtinu. Vynecháním argumentu se skript spustí v češtině.
```main.py Praha results-praha.csv --en```

# Election scraper (English)
A simple script that downloads results for all electoral districts in the selected district from 2017 from the website volby.cz and saves them to a CSV file. Written as an exercise within the Engeto Academy: <https://engeto.cz>.

## Installation of requirements.txt
Install the 'pip' module -> <https://pip.pypa.io/en/stable/installation/><br>
Create a virtual environment in the chosen directory -> <https://docs.python.org/3/library/venv.html#creating-virtual-environments><br>
Use ```pip install -r requirements.txt``` to install the necessary libraries in the chosen directory and copy all project files into it (or clone using git).

## How to run the script
Run the `main.py` script with two arguments: **the name of the district** for which you want the results (more details below) and **the name of the CSV file**. Running the script with one argument `list` will list all districts. The primary language is Czech; you can run the script in English by using `--en` or `--english` as the last argument.

### Examples of running
To save results from the district of Frýdek-Místek to the file vysledky_z_FM.csv, run the script:<br>
`main.py Frýdek-Místek vysledky_z_FM.csv`<br>
If you want the script to communicate in English, add the argument '--en':
`main.py Frýdek-Místek vysledky_z_FM.csv --en`<br>
If you want results for a district that has spaces in its name, enclose the district name in quotes:<br>
`main.py 'Rychnov nad Kněžnou' vysledky_z_rychnova.csv`

## Arguments
### District name - first argument
Enter the name of the district, use the exact name of the district (pay attention to diacritics and capitalization): `main.py 'Ústí nad Orlicí' usti_n_orlici.csv` <br>
To list all districts, run `main.py list`.

### File name - second argument
Enter the file name as the second argument. You can omit the '.csv' extension; it will be added automatically. `main.py Praha vysledky-praha`

### Language - last optional argument
If you use '--en' or '--english' as the last argument, it will change the language to English. By omitting the argument, the script will run in Czech.
`main.py Praha results-praha.csv --en`