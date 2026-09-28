def pocisti_stevilo(niz):

    #pomožna funkcija za pretvorbo nizov, kot so '$3.051 T', '$225.40', '+1.20%',
    #v dejanske številčne vrednosti (float).
    
    if not niz or niz == "N/A": #  N/A je nekaj kar pise v celici na spletni strani (pomeni not available), not niz pa napisemo ce podatka v htmlju sploh ni
        return None
    
    # odstranimo presledke in znake $, %, +
    niz = niz.replace("$", "").replace("%", "").replace("+", "").strip()
    
    # pretvorimo kratice T (Trillion), B (Billion), M (Million)
    mnozitelj = 1
    if niz.endswith("T"):
        mnozitelj = 1e12 # pomeni 1 in se 12 nicel
        niz = niz[:-1].strip() # dostranimo zadnji znak niza ker zadnji znak je T
    elif niz.endswith("B"):
        mnozitelj = 1e9
        niz = niz[:-1].strip()
    elif niz.endswith("M"):
        mnozitelj = 1e6
        niz = niz[:-1].strip()
        
    try:
        return float(niz) * mnozitelj
    except ValueError: # nastane takrat ko je niz v formatu ki se ga ne da pretvoriti v int ali float
        return None

def izluscaj_podjetja_s_strani(soup):
    # izlušči podatke o podjetjih iz ene strani tabele
    podatki = []
    tabela = soup.find("table")
    if not tabela:
        return podatki

    vrstice = tabela.find_all("tr") # tr je v htmlju table row

    for vrstica in vrstice[1:]:  # preskočimo glavo tabele
        celice = vrstica.find_all("td")  # td oznacuje celice ki niso v glavi

        if len(celice) < 8:  # za primer ce v vrstici manjsa večina podatkv ali pa je to celica z npr <thead\>
            continue

        # izluščimo ime podjetja in njegovo kodo (oz ticker)
        ime_elementa = celice[2].find("div", class_="company-name")  # gre od zunaj navznotr: zacnemo pri znacki div in znotraj nje iscemo company name
        koda_elementa = celice[2].find("div", class_="company-code")

        if ime_elementa:
            ime = ime_elementa.get_text(strip=True) 
        else:
            ime = "N/A"

        if koda_elementa:
            koda = koda_elementa.get_text(strip=True) 
        else:
            koda = "N/A"

        # Povezava do podstrani podjetja (za morebitni nadaljnji zajem)
        #povezava_elem = celice[2].find("a", href=True)
        #povezava = naslov_strani + povezava_elem["href"] if povezava_elem else ""

        # številčni podatki
        market_cap_raw = celice[3].get_text(strip=True)
        cena_raw = celice[4].get_text(strip=True)
        sprememba_raw = celice[5].get_text(strip=True)

        # država
        drzava_element = celice[7].find("span", class_="responsive-hidden")
        if drzava_element:
            drzava = drzava_element.get_text(strip=True)
        else:
            drzava = "N/A"

        # shranimo tako surove kot očiščene podatke
        podatki.append({
            "Ime": ime,
            "Koda": koda,
            "Market_Cap_USD": pocisti_stevilo(market_cap_raw),
            "Cena_USD": pocisti_stevilo(cena_raw),
            "Sprememba_Odstotek": pocisti_stevilo(sprememba_raw),
            "Drzava": drzava,
           # "Povezava": povezava, se nanasa na tist del kode ki je zakomentiran 
        })

    return podatki
