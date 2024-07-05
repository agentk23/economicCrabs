import pandas as pd

f = "filteredData.csv"
df = pd.read_csv(f)

judete = "ALBA, BRASOV, COVASNA, HARGHITA, MURES, SIBIU"
judete = judete.split(", ")

# filter by judet, 
# filter by CifraDeAfaceriNetaRON2021, filter by ProfitNetRON2021 > 0
# filter by ProfitNetRON2021 / CifraDeAfaceriNetaRON2021 > 0.1



