import pandas as pd

# Load the CSV data
file_path = 'Lista-SUN2018_6-august-2019_admisi.csv'
data = pd.read_csv(file_path, delimiter=',', names=['entryId', 'id', 'company name', 'status', 'location'])

# Filter data based on location containing "BRASOV" or "MURES"
filtered_data = data[data['location'].str.contains('BRASOV|MURES', na=False)]

# Create curl commands
curl_commands = []

for index, row in filtered_data.iterrows():
    company_name = row['company name']
    company_name = company_name.replace(".", "")
    company_name = company_name.replace("SC", "")
    company_name = company_name.replace("SRL", "")
    company_name = company_name.replace("&", " ")
    company_name = company_name.strip()
    encoded_company_name = company_name.replace(' ', '+')
    curl_command = (
        f"curl 'https://www.listafirme.ro/search.asp' --compressed -X POST "
        f"-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0' "
        f"-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' "
        f"-H 'Accept-Language: en,en-US;q=0.7,en-GB;q=0.3' "
        f"-H 'Accept-Encoding: gzip, deflate, br, zstd' "
        f"-H 'Referer: https://www.listafirme.ro/search.asp' "
        f"-H 'Content-Type: application/x-www-form-urlencoded' "
        f"-H 'Origin: https://www.listafirme.ro' "
        f"-H 'Alt-Used: www.listafirme.ro' "
        f"-H 'Connection: keep-alive' "
        f"-H 'Cookie: G_ENABLED_IDPS=google; g_state={{\"i_p\":1719947129694,\"i_l\":1}};' "
        f"-H 'Upgrade-Insecure-Requests: 1' "
        f"-H 'Sec-Fetch-Dest: document' "
        f"-H 'Sec-Fetch-Mode: navigate' "
        f"-H 'Sec-Fetch-Site: same-origin' "
        f"-H 'Sec-Fetch-User: ?1' "
        f"-H 'Priority: u=1' "
        f"--data-raw 'searchfor={encoded_company_name}&jud=0'"
    )
    curl_commands.append(curl_command)

# Save curl commands to a text file
with open('curl_commands.txt', 'w') as file:
    for command in curl_commands:
        file.write(command + "\n")

