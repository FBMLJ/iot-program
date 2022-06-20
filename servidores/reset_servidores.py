from time import sleep
import requests




if __name__ == "__main__":
    for i in range(15):
        url_delete = "http://localhost:1026/v2/entities/sensor_{}".format(i)
        requests.delete(url_delete)
        text = requests.post("http://localhost:1026/v2/entities", json={	"id": "sensor_{}".format(i),
                                                                            "type": "sensor",	
                                                                            "dado_atual":{
                                                                                "value": None,
                                                                                "type": "Float"},
                                                                            "historico": {
                                                                                "value": [],
                                                                                "type": "Array"	
                                                                                }
                                                                            })
        