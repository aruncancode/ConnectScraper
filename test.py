from connectapi import ConnectApi
import json

f = open("sensitiveInfo.json", "r")
sensitiveInfo = json.loads(f.read())
f.close()
connect = ConnectApi(sensitiveInfo["username"], sensitiveInfo["password"])
connect.login()
f = open("output.html", "w")
f.write(
    connect.getCustomPage(
        "https://connect.det.wa.edu.au/group/students/ui/overview", raw=True
    )
)
f.close()
