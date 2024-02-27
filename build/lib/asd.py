import requests
from bs4 import BeautifulSoup
import re
import sys
import pandas as pd

meteo_blue_url = 'https://www.meteoblue.com/de/wetter/outdoorsports/seeing/davos_schweiz_2661039'
meteo_blue_columns = ["Hour",
                        "Low",
                        "Mid",
                        "High",
                        "ArcSec.",
                        "Idex_1",
                        "Index_2",
                        "Jet_Stream",
                        "Bot (km)",
                        "Top (km)",
                        "K/100m",
                        "Temp",
                        "Rel. Hum.",
                        "celestial_bodies"
                        ]


def _get_weather_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Failed to retrieve the webpage: Status code {response.status_code}")
        sys.exit(1)
    return html_content

def _get_df_from_meteo(html, columns):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    pattern = re.compile(r'^hour-row (?=\S)')
    matching_rows = table.find_all('tr', class_=pattern)
    data = []
    pattern = re.compile(r'')
    for row in matching_rows:
        row_data = []
        celestial_data=[]
        for td in row.find_all('td'):
            if 'celestial' in td.get('class', []):
                inner_table = td.find('table')
                if inner_table:
                    # Iterate through each row of the inner table
                    for tr in inner_table.find_all('tr'):
                        # Extract text from each cell within this row, stripping leading/trailing whitespace
                        celestial_row = [cell.get_text(strip=True) for cell in tr.find_all(['th', 'td'])]
                        celestial_data.append(celestial_row)
                row_data.append(celestial_data)
                break
            else:
                row_data.append(td.get_text(strip=True))
            

        # Append the row data to the list
        data.append(row_data)
    df = pd.DataFrame(data,columns=columns)
    return df


def get_day():
    html = _get_weather_html(meteo_blue_url)
    df = _get_df_from_meteo(html, meteo_blue_columns)
    return df

if "__main__" == __name__:
    print(get_day())



