import requests
import time
from bs4 import BeautifulSoup

while True:
    # enter city name
    city = "helsingborg"

    # creating url and requests instance
    url = "https://www.klart.se/se/sk%C3%A5ne-l%C3%A4n/v%C3%A4der-helsingborg/"
    response = requests.get(url)
    
    # getting raw data
    soup = BeautifulSoup(response.text, 'html.parser')
    temp = soup.find(class_="temp-high")
    temptext = temp.text.strip()
    print(temptext)
    
    requests.post("https://ntfy.sh/vaderhemma123", data=("temp"+temptext).encode('utf-8'), 
                            headers={ "Title": "Weather", 
                        "Icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/CloudColors.jpg/230px-CloudColors.jpg"})
    time.sleep(1800)
