import requests
from bs4 import BeautifulSoup

# req_url = 'https://connect.det.wa.edu.au/'
url = 'https://connect.det.wa.edu.au/group/students/ui/my-settings/assessment-outlines'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}

session_requests = requests.Session()

result = session_requests.post(url, data={
    'ssousername': '',
    'password': '',
    'acceptterms': 'acceptterms'})


data = session_requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")

print(soup)
