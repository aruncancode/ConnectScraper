from connect_scraper import ConnectScraper
import json

f = open("sensitiveInfo.json", "r")
sensitiveInfo = json.loads(f.read())
f.close()

connect = ConnectScraper(
    sensitiveInfo["username"], sensitiveInfo["password"], headless=False
)
connect.login()

# === TESTING ===
out = connect.getHomePage().getNextSubmissions()
# === TESTING ===

pass  # pause before the end
