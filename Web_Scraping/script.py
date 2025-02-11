from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Forbes_list_of_the_most_valuable_football_clubs'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

world_table = soup.find_all('table')[0]
world_table_titles = world_table.find_all('th')
world_table_columns = [title.text.strip() for title in world_table_titles]
world_data = world_table.find_all('tr')

df = pd.DataFrame(columns = world_table_columns)

for data in world_data[1:]:
    row_data = data.find_all('td')
    individual_row_data = [row.text.strip() for row in row_data]

    length = len(df)
    df.loc[length] = individual_row_data
