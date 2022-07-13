import requests

def criando_device(tipo,id,x,y):

    url = "http://localhost:4041/iot/devices"
    device_id = "{}:{}".format(tipo, id)
    payload = {"devices": [
            {
                "device_id": device_id,
                "entity_name": "urn:ngsi-ld:{}:{}".format(tipo,id),
                "entity_type": "{}".format(tipo),
                "timezone": "American/Brazil",
                "attributes": [
                    {
                        "object_id": "v",
                        "name": "valor",
                        "type": "Float"
                    }
                ],
                "static_attributes": [
                    {
                        "name": "refStore",
                        "type": "Relationship",
                        "value": "urn:ngsi-ld:Store:001"
                    },
                    {
                        "name": "position_x",
                        "type": "Integer",
                        "value": x
                    },
                    {
                        "name": "position_y",
                        "type": "Integer",
                        "value": y
                    }
                ]
            }
        ]}
    headers = {
        "Content-Type": "application/json",
        "fiware-service": "openiot",
        "fiware-servicepath": "/"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
    return device_id