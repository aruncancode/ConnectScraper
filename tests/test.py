from connect_api import ConnectApi
import json
import time

f = open("sensitiveInfo.json", "r")
sensitiveInfo = json.loads(f.read())
f.close()

connect = ConnectApi(
    sensitiveInfo["username"], sensitiveInfo["password"], headless=False
)
connect.login()

time.sleep(2)

print(connect.test())
