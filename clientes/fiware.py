import requests
import json
def get_all_sensor():
    url = "http://localhost:1026/v2/entities/"

    payload = ""
    headers = {
        "fiware-service": "openiot",
        "fiware-servicepath": "/"
    }

    response = requests.request("GET", url, data=payload, headers=headers)

    return json.loads(response.text)
    
print(get_all_sensor())