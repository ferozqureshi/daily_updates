import requests
import pandas as pd




from bs4 import BeautifulSoup

# HTML structure

# Parse the HTML content using BeautifulSoup
url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'

def main():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

# Find all <tr> elements
    tr_elements = soup.find_all('tr')

    # Extract links with the desired date
    links = []
    for tr in tr_elements:
        td_elements = tr.find_all('td')
        if len(td_elements) == 4:
            date_td = td_elements[1]
            link_td = td_elements[0]
            if date_td.text.strip() == '2022-02-07 14:02':
                link = link_td.find('a')
                if link is not None:
                    links.append(link['href'])


    # Process or store the extracted links as needed
    print('Links:', links[0])
    
    csv_link = url+links[0]
    response = requests.get(csv_link)

# Save the CSV file locally
    csv_file_path = 'data.csv'
    with open(csv_file_path, 'wb') as file:
        file.write(response.content)

    # Read the CSV file using pandas
    df = pd.read_csv(csv_file_path)

    # Find the highest HourlyDryBulbTemperature
    highest_temperature = df['HourlyDryBulbTemperature'].max()

    print('Highest HourlyDryBulbTemperature:', highest_temperature)



if __name__ == "__main__":
    main()
