import requests
import bs4

url = requests.get("https://www.tutorialspoint.com/pygame/pygame_event_objects.htm")
soup = bs4.BeautifulSoup(url.text, "html.parser")

need = soup.find("div", id="mainContent")
print(need)

# TODO: learn regex and then come back to this and do stuff sir
