import socket
import json
from dict_creator import create_dict
import pickle
import time


HOST = socket.gethostname()
PORT = 8888
 

with open("input.txt") as f:
    lines = f.readlines()

#use first five lines for client 1
inputs = lines[:5]
timesents = []
timerecvds = []

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    for prompt in inputs:
        s.sendall(bytes(prompt,encoding='utf8'))
        timesents.append(int(time.time()))


        data = pickle.loads((s.recv(1024)))
        timerecvds.append(int(time.time()))

        outputs = create_dict(data, for_server=True, ClientID="Client 1",iterative=False)

        json_object = json.dumps(outputs, indent=4)
        with open("output_client1.json", "a") as outfile:
            outfile.write(json_object)


    

