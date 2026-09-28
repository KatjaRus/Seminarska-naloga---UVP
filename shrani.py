import os
import pandas as pd
import json

def shrani_v_json(podatki, ime_datoteke):
    with open(ime_datoteke, "w", encoding="utf-8") as f:
        json.dump(podatki, f, ensure_ascii=False, indent=4)

def shrani_podatke(vsa_podjetja):
    # 2. podatke pretvorimo v Pandas DataFrame
    df = pd.DataFrame(vsa_podjetja)

    # 3. shranimo v csv datoteko
    os.makedirs("podatki", exist_ok=True)
    pot_do_csv = "podatki/podjetja_market_cap.csv"
    df.to_csv(pot_do_csv, index=False, encoding="utf-8-sig")

    # 4. shranimo še v json datoteko v isto mapo
    pot_do_json = "podatki/podjetja_market_cap.json"
    shrani_v_json(vsa_podjetja, pot_do_json)

    print(
        f"\nUspešno shranjenih {len(df)} vrstic v CSV in JSON znotraj mape 'podatki'!"
    )