import pandas as pd
import csv

f = "filteredData.csv"
df = pd.read_csv(f)


def calculateRatioForAllYears(profituri, cifreAf):
    ratios = []
    for i in range(4):
        if cifreAf[i] == 0:
            ratios.append(0)
        else:
            ratios.append(profituri[i] / cifreAf[i])
    return ratios

def filterByJudet (judete, judet):
    return judet in judete


# profituri starts from 2021 -> 2018
def filterByProfit(profituri):
    # for p in profituri:
    #     if p <= 0:
    #         return False
    # return True
    return profituri[0] > 0

# cifreAf starts from 2021 -> 2018
def filterByCifraAf(cifreAf):
    for c in cifreAf:
        if c <= 0:
            return False
    return True

# ratios starts from 2021 -> 2018
def filterByRatio(ratios):

    # for r in ratios:
    #     if r <= 0.005:
    #         return False
    # return True
    return ratios[0] > 0.005



def filterEntry(entry):
    judete = "ALBA, BRASOV, COVASNA, HARGHITA, MURES, SIBIU"
    judete = judete.split(", ")
    judet = str(entry["Judet"])
    if not filterByJudet(judete, entry["Judet"]):
        return False
    
    cifreAf = [entry["CifraDeAfaceriNetaRON2021"], entry["CifraDeAfaceriNetaRON2020"], entry["CifraDeAfaceriNetaRON2019"], entry["CifraDeAfaceriNetaRON2018"]]
    cifreAf = [float(cifra) for cifra in cifreAf]
    if not filterByCifraAf(cifreAf):
        return False
    
    profituri = [entry["ProfitNetRON2021"], entry["ProfitNetRON2020"], entry["ProfitNetRON2019"], entry["ProfitNetRON2018"]]
    for profit in profituri:
        profit = float(profit)

    if not filterByProfit(profituri):
        return False
        
    ratios = calculateRatioForAllYears(profituri, cifreAf)
    if not filterByRatio(ratios):
        return False
    
    return True

def writeCsvFile(fileName, filteredEntries, header):
    with open (fileName, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for key, value in (filteredEntries.items() if isinstance(filteredEntries, dict) else enumerate(filteredEntries)):
            ratios = calculateRatioForAllYears([value['ProfitNetRON2021'], value['ProfitNetRON2020'], value['ProfitNetRON2019'], value['ProfitNetRON2018']], [value['CifraDeAfaceriNetaRON2021'], value['CifraDeAfaceriNetaRON2020'], value['CifraDeAfaceriNetaRON2019'], value['CifraDeAfaceriNetaRON2018']])
            value['Ratio2021'] = ratios[0]
            value['Ratio2020'] = ratios[1]
            value['Ratio2019'] = ratios[2]
            value['Ratio2018'] = ratios[3]
            writer.writerow([value['Nume'], value['CodFiscal'], value['Judet'], value['Telefon'],value['CodCAEN2021'], value['DescriereCodCAEN2021'], value['Ratio2021'],value['Ratio2020'],value['Ratio2019'],value['Ratio2018'],value['CifraDeAfaceriNetaRON2021'], value['ProfitNetRON2021'], value['CotaDePiata2021'],  value['Salariati2020'], value['CifraDeAfaceriNetaRON2020'], value['ProfitNetRON2020'], value['CotaDePiata2020'], value['CodCAEN2020'], value['DescriereCodCAEN2020'], value['Salariati2019'], value['CifraDeAfaceriNetaRON2019'], value['ProfitNetRON2019'], value['CotaDePiata2019'], value['CodCAEN2019'], value['DescriereCodCAEN2019'], value['Salariati2018'], value['CifraDeAfaceriNetaRON2018'], value['ProfitNetRON2018'], value['CotaDePiata2018'], value['CodCAEN2018'], value['DescriereCodCAEN2018']])
        # for key, value in [if filteredEntries.items():
        #     ratios = calculateRatioForAllYears([value['ProfitNetRON2021'], value['ProfitNetRON2020'], value['ProfitNetRON2019'], value['ProfitNetRON2018']], [value['CifraDeAfaceriNetaRON2021'], value['CifraDeAfaceriNetaRON2020'], value['CifraDeAfaceriNetaRON2019'], value['CifraDeAfaceriNetaRON2018']])
        #     value['Ratio2021'] = ratios[0]
        #     value['Ratio2020'] = ratios[1]
        #     value['Ratio2019'] = ratios[2]
        #     value['Ratio2018'] = ratios[3]
        #     writer.writerow([value['Nume'], value['CodFiscal'], value['Judet'], value['Telefon'],value['CodCAEN2021'], value['DescriereCodCAEN2021'], value['Ratio2021'],value['Ratio2020'],value['Ratio2019'],value['Ratio2018'],value['CifraDeAfaceriNetaRON2021'], value['ProfitNetRON2021'], value['CotaDePiata2021'],  value['Salariati2020'], value['CifraDeAfaceriNetaRON2020'], value['ProfitNetRON2020'], value['CotaDePiata2020'], value['CodCAEN2020'], value['DescriereCodCAEN2020'], value['Salariati2019'], value['CifraDeAfaceriNetaRON2019'], value['ProfitNetRON2019'], value['CotaDePiata2019'], value['CodCAEN2019'], value['DescriereCodCAEN2019'], value['Salariati2018'], value['CifraDeAfaceriNetaRON2018'], value['ProfitNetRON2018'], value['CotaDePiata2018'], value['CodCAEN2018'], value['DescriereCodCAEN2018']])
        file.close()
    return "The file has been written successfully"




filteredEntries = {}
bune = []
for index, entry in df.iterrows():
    if filterEntry(entry):
        bune.append(entry)
bune.sort(key=lambda x: x["CodCAEN2021"], reverse=True)

fileName = "finalData.csv"
header = ['Nume','CodFiscal','Judet','Telefon','CodCAEN2021','DescriereCodCAEN2021','Ratio2021','Ratio2020','Ratio2019','Ratio2018','CifraDeAfaceriNetaRON2021','ProfitNetRON2021','CotaDePiata2021','Salariati2020','CifraDeAfaceriNetaRON2020','ProfitNetRON2020','CotaDePiata2020','CodCAEN2020','DescriereCodCAEN2020','Salariati2019','CifraDeAfaceriNetaRON2019','ProfitNetRON2019','CotaDePiata2019','CodCAEN2019','DescriereCodCAEN2019','Salariati2018','CifraDeAfaceriNetaRON2018','ProfitNetRON2018','CotaDePiata2018','CodCAEN2018','DescriereCodCAEN2018']

try: 
    writeCsvFile(fileName, bune, header)
except Exception as e:
    print(f"Error writing the file: {e}")

