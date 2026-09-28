import os
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd #pandas tukaj importamo zato da lažje shranimo pridobljene podatke v datoteko csv. (D)

naslov_strani = "https://companiesmarketcap.com" # glavni naslov spletne strani


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
} 
# ta vrstica poskrbi da nas spletna stran ne blokira ko poizkusimo dobiti podatke


def pridobi_html_strani(url):
    # pomomožna funkcija, ki pošlje zahtevo na URL in vrne BeautifulSoup objekt.
    try:
        odgovor = requests.get(url, headers=HEADERS, timeout=10) # z url povemo kero spletno stran obiskujemo s headers pa kdo jo obuskuje. timeout=10 posktbi da ce se spletna stran ne odzove po 10 sekundah sproži napako
        odgovor.raise_for_status() #preveri ali spletna stran vrne napako kot na primer 404 Not found, raise_for_status je ugrajena funkcija knjižnice requests
        return BeautifulSoup(odgovor.text, "html.parser") 
    
        # BeautifulSoup surovo besedilo spletne strani pretvori v strukturo, po kateri lahko iščemo elemente (znčke, tabele, razrede)
        # odgovor.text je surovo html besedilo ki smo ga dobili iz spletne strani in po jaterem lahko iščemo značke, tabele, classe
        # html.parser je vgrajen pythonov prevajalnik ki ustvari objekt soup v katerem lahko uporabljamo ukaze kot so .find() in .find_all()
        # BeautifulSoup je razred, odgovor.text je IZ kje naj preber besedilo, html.parser pa KATERO orodje naj uporabi za razumevanje besedila

    except Exception as error:
        print(f"Napaka pri pridobivanju strani {url}: {error}")
        return None
    # z uporabo try in expect povemo pythonu da ce gre pri try kaj narobe da naj ne zruši programa ampak nadaljuje na blok expect