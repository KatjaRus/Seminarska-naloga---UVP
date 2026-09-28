from pridobi import naslov_strani, pridobi_html_strani
from izlusci import izluscaj_podjetja_s_strani
from shrani import shrani_podatke

def zajemi_vsa_podjetja(stevilo_strani=5): # izberemo le prvih 500 podjetji (100 na stran)
    #zajame podatke skozi več strani (paginacija)
    vsi_podatki = []
    
    for stran in range(1, stevilo_strani + 1):
        print(f"Zajemam stran {stran} od {stevilo_strani}...")
        url = f"{naslov_strani}/page/{stran}/"
        soup = pridobi_html_strani(url)
        
        if soup: # ce je nalaganje uspelo soup obstaja, ce soup ne obstaja za nobeno stran funkcija vrne [], ce ne obstaja samo za eno stran vrne podatke za ostale 4 strani 
            shranjeni_podatki = izluscaj_podjetja_s_strani(soup)
            vsi_podatki.extend(shranjeni_podatki)
            print(f"Pridobljeno {len(shranjeni_podatki)} podjetij.")

    return vsi_podatki

if __name__ == "__main__":
    # 1. zajamemo podatke iz vseh 5 strani (skupaj 500 podjetij)
    vsa_podjetja = zajemi_vsa_podjetja(stevilo_strani=5)
    # 2. in 3. shranimo
    shrani_podatke(vsa_podjetja)