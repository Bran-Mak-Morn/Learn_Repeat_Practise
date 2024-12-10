import pandas as pd


def ods_to_csv(ods_file, csv_file):
    # Načti .ods soubor
    data = pd.read_excel(ods_file, engine='odf')

    # Vyber pouze první tři sloupce
    data = data.iloc[:, :3]

    # Odstraní prázdné řádky
    data = data.dropna(how='all')

    # Ulož data do .csv souboru
    data.to_csv(csv_file, index=False, header=False)


# run the function
ods_to_csv('words_to_review.ods', 'words_to_review.csv')