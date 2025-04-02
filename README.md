# Election scraper

## How to Run It
Run the main script 'scraper.py' with at least one argument: the name of the district for which you want results (more details below). The second argument is the name of a CSV file (without the file extension). If you provide only one argument, the script will run and save results to the file 'results.csv' (note that it will overwrite an older one if it exists). You can list all districts by running the script with the 'list' argument. The primary language is Czech; you can run the script in English using '--en' or '--english' as the last argument.<br>
To save the results from the district of Frýdek-Místek to the file vysledky_z_FM.csv, run the script: 
```scraper.py Frýdek-Místek vysledky_z_FM.csv```<br>
If you want the script to communicate in English, add the argument '--en': 
```scraper.py Frýdek-Místek vysledky_z_FM.csv --en```

## Name of District - First Argument
Input a region name, using the exact form as it is stored in Czech language. For example: ```scraper.py Praha```
To list all regions, run ```scraper.py list```.

## File Name - Second Argument
Input the file name without spaces as the second argument. You can omit the '.csv' extension; it will be added automatically. You can also omit the second argument completely; the script will save results to 'results.csv'.

## Language - Last Argument
If you use "--en" or "--english" as the last argument, it will change the language to English.

# Election scraper - česky

Jednoduchý skript, který stáhne výsledky pro všechny volební okrsky ve zvoleném okrese z roku 2017 ze stránek volby.cz. Hlavní skript se nachází v souboru 'scraper.py'. Napsáno jako cvičení v rámci [Engeto akademie][https://engeto.cz].

## Jak skript spustit
Spusťte hlavní skript 'scraper.py' s alespoň jedním argumentem: názvem okresu, pro který chcete výsledky (více podrobností níže). Druhý argument je název CSV souboru (bez přípony souboru). Pokud poskytnete pouze jeden argument, skript se spustí a uloží výsledky do souboru 'results.csv' (vezměte na vědomí, že přepíše starší soubor, pokud existuje). Můžete vypsat všechny okresy spuštěním skriptu s argumentem 'seznam'. Primární jazyk je čeština; skript můžete spustit v angličtině pomocí "--en" nebo "--english" jako posledního argumentu.<br>
Pro uložení výsledků z okresu Frýdek-Místek do souboru vysledky_z_FM.csv spusťe skript: ```scraper.py Frýdek-Místek vysledky_z_FM.csv```<br>
Pokud chcete, aby skript komunikoval v angličtině, přidejte argument '--en': ```scraper.py Frýdek-Místek vysledky_z_FM.csv --en```

## Název okresu - první argument
Zadejte název okresu, použijte přesnou formu, jak je uložena. Například: ```scraper.py Praha```
Pro vypsání všech okresu spusťte ```scraper.py seznam```.

## Název souboru - druhý argument
Zadejte název souboru bez mezer jako druhý argument. Můžete vynechat příponu '.csv'; ta bude automaticky přidána. Můžete také zcela vynechat druhý argument; skript uloží výsledky do 'results.csv'.

## Jazyk - poslední argument
Pokud použijete "--en" nebo "--english" jako poslední argument, změní jazyk na angličtinu.