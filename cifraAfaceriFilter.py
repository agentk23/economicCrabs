# to get all the data I collected and try to filter it by profit / loss
# import csv 

import pandas as pd
import numpy as np
import csv


# FOLOSESTE FUNCTII BA TERMINATULE
# read the data
input_csv = "data/extracted_hrefs.csv"
large_data_csv = "data/Baza_de_date_Firme.csv"

df = pd.read_csv(input_csv)
firme_bd = pd.read_csv(large_data_csv, low_memory=False)

# get the coduri fiscale from hrefs
coduriFiscale = []

for entry in df['hrefs']:
    if entry:
        cod = entry.split("-")[-1]
        cod = cod.split("/")[0]
        coduriFiscale.append(cod)

# create a dictionary with the coduri fiscale
coduriDict = {}
for cod in coduriFiscale:
    if cod and cod != '[]':
        coduriDict[cod] = False



matches = {}


# iterate through large data and get the matches and the necessary data
for index, row in firme_bd.iterrows():
    string = str(row['CodFiscal'])
    if string in coduriDict:
        matches[row['CodFiscal']] = row
        coduriDict[string] = True

header = ['Nume','CodFiscal','Judet','Telefon','CifraDeAfaceriNetaRON2021','ProfitNetRON2021','CotaDePiata2021','CodCAEN2021','DescriereCodCAEN2021','Salariati2020','CifraDeAfaceriNetaRON2020','ProfitNetRON2020','CotaDePiata2020','CodCAEN2020','DescriereCodCAEN2020','Salariati2019','CifraDeAfaceriNetaRON2019','ProfitNetRON2019','CotaDePiata2019','CodCAEN2019','DescriereCodCAEN2019','Salariati2018','CifraDeAfaceriNetaRON2018','ProfitNetRON2018','CotaDePiata2018','CodCAEN2018','DescriereCodCAEN2018']

with open ('filteredData.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for key, value in matches.items():
        writer.writerow([value['Nume'], value['CodFiscal'], value['Judet'], value['Telefon'], value['CifraDeAfaceriNetaRON2021'], value['ProfitNetRON2021'], value['CotaDePiata2021'], value['CodCAEN2021'], value['DescriereCodCAEN2021'], value['Salariati2020'], value['CifraDeAfaceriNetaRON2020'], value['ProfitNetRON2020'], value['CotaDePiata2020'], value['CodCAEN2020'], value['DescriereCodCAEN2020'], value['Salariati2019'], value['CifraDeAfaceriNetaRON2019'], value['ProfitNetRON2019'], value['CotaDePiata2019'], value['CodCAEN2019'], value['DescriereCodCAEN2019'], value['Salariati2018'], value['CifraDeAfaceriNetaRON2018'], value['ProfitNetRON2018'], value['CotaDePiata2018'], value['CodCAEN2018'], value['DescriereCodCAEN2018']])
    file.close()
# procentul de profit / cifraDeAfaceri

