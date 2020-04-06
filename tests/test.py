from connect_api import ConnectApi
import json
import time

f = open("sensitiveInfo.json", "r")
sensitiveInfo = json.loads(f.read())
f.close()

connect = ConnectApi(
    sensitiveInfo["username"], sensitiveInfo["password"], headless=True
)
connect.login()
# After this is done the python garbage collector will automatically
# close the browser.
time.sleep(2)

print(connect.notices())
