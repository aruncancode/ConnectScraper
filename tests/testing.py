from connect_scraper import ConnectScraper
import json

# from connect_scraper.classes import Class

f = open("sensitiveInfo.json", "r")
sensitiveInfo = json.loads(f.read())
f.close()

connect = ConnectScraper(
    sensitiveInfo["username"], sensitiveInfo["password"], headless=False
)
connect.login()

# === TESTING ===
# clss = Class(connect, name="2020 Yr 10 GATE HaSS Combined", id=1932630127)
clss = connect.classes.update().list[2]
out = clss.learners.teachers()
# === TESTING ===

pass  # pause before the end
