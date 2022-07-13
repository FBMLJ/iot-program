def atualizar_valor(id, valor):
    # return
    import requests

    url = "http://localhost:7896/iot/json"
    print(id)
    querystring = {"k":"4jggokgpepnvsb2uv4s40d59ov","i": id}

    payload = {"v": valor}
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    print(response.text)