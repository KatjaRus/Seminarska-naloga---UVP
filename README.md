# Analiza tržne kapitalizacije in nihanja vodilnih svetovnih podjetij

V tej seminarski nalogi sem analizirala 500 največjih javno kotirajočih podjetij (angleškega publicly traded companies) na svetu po tržni kapitalizaciji ter preučila njihovo porazdelitev, koncentracijo kapitala in nihanja cen delnic.

---

## Pridobivanje podatkov

Zajem podatkov poteka preko datotek `pridobi.py`, `izlusci.py` in `shrani.py`, ki jih povezuje glavna datoteka `main.py`. Pridobljeni podatki se samodejno shranijo v datoteko `podatki/podjetja.csv`.

Za vsako podjetje sem pridobila naslednje podatke:
* **Ime podjetja** (Name)
* **Symbol / Oznaka** (Ticker)
* **Tržna kapitalizacija** (Market Cap v USD)
* **Cena delnice** (Price v USD)
* **Dnevna sprememba** (Daily Change v %)
* **Država sedeža** (Country)

---

## Analiza podatkov

Analiza je razdeljena na pet glavnih tematskih sklopov:

1. **Geografska porazdelitev:** Pregled Top 10 držav z največjim skupnim tržnim kapitalom in največjim številom podjetij na seznamu Top 500.
2. **Tržna koncentracija:** Analiza deleža skupne vrednosti prvih 10 največjih podjetij v primerjavi s preostalimi 490 podjetji.
3. **Paretovo pravilo (80/20):** Preverjanje, ali manjšinski odstotek vodilnih podjetij obvladuje pretežni del skupnega kapitala trga.
4. **Korelacija in regresija:** Analiza povezave med velikostjo podjetja (tržno kapitalizacijo) in njegovim dnevnim nihanjem tečaja.
5. **Detekcija osamelcev (Z-score):** Identifikacija podjetij z ekstremno odstopajočimi dnevnimi skoki ali padci cen delnic.

---

## Kako zagnati projekt?

Za zagon projekta potrebuješ naložen **Python 3.10** ali novejši ter knjižnice `pandas`, `matplotlib`, `numpy` in `scipy`.

### 1. Zajem podatkov
Če želiš znova zajeti podatke s spleta in osvežiti CSV datoteko, poženi skripto:

```bash
python main.py