def criando_servico():
    import requests

    url = "http://localhost:4041/iot/services"

    payload = {"services": [
            {
                "apikey": "4jggokgpepnvsb2uv4s40d59ov",
                "cbroker": "http://orion:1026",
                "entity_type": "Thing",
                "resource": "/iot/json"
            }
        ]}
    headers = {
        "Content-Type": "application/json",
        "fiware-service": "openiot",
        "fiware-servicepath": "/"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)