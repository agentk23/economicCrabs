import csv
import subprocess
import time
from bs4 import BeautifulSoup
import pandas as pd


# Function to perform a cURL request and return the HTML content
def perform_curl_request(curl_command):
    try:
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error performing cURL request: {e}")
        return ''


# Function to extract hrefs from HTML content
def extract_hrefs_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    hrefs = []
    for td in soup.find_all('td', class_='clickable-row'):
        a_tag = td.find('a')
        if a_tag and 'href' in a_tag.attrs:
            hrefs.append(a_tag['href'])
    return hrefs


# Read the cURL commands from the file
curl_commands_file = 'curl_commands.txt'
with open(curl_commands_file, 'r') as file:
    curl_commands = file.readlines()

# List to store results
results = []
# Iterate over the cURL commands
with open('hrefs_buffer.csv', 'a') as f_object:
    dictWriter = csv.DictWriter(f_object, fieldnames=['index', 'command', 'hrefs'])
    index = 0
    for command in curl_commands:
        command = command.strip()
        index+= 1
        if command:
            html_content = perform_curl_request(command)
            hrefs = extract_hrefs_from_html(html_content)
            dictWriter.writerow({'index': index, 'command': command, 'hrefs': hrefs})
            results.append({'command': command, 'hrefs': hrefs})

            time.sleep(5)
    f_object.close()
# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Save results to a CSV file
results_df.to_csv('extracted_hrefs.csv', index=False)

print("Extracted hrefs have been written to extracted_hrefs.csv")
