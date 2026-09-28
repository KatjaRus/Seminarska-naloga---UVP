import os
import pandas as pd

def shrani_podatke(vsa_podjetja):
    # 2. podatke pretvorimo v Pandas DataFrame
    df = pd.DataFrame(vsa_podjetja)

    # 3. shranimo v csv datoteko
    os.makedirs("podatki", exist_ok=True)
    pot_do_datoteke = "podatki/podjetja_market_cap.csv"
    df.to_csv(pot_do_datoteke, index=False, encoding="utf-8-sig")

    print(f"\nUspesno shranjenih {len(df)} vrstic v datoteko '{pot_do_datoteke}'.")
    print(df.head())