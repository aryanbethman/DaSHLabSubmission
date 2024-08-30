import socket
from transformers import pipeline
import pickle


HOST = socket.gethostname()
PORT = 8888

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(5)
    conn, addr = s.accept()

    with conn:
        while True:
            data = conn.recv(1024).decode('utf8')
            data_list = data.split("\n")[0]
            print(data_list)
            
            pipe = pipeline("text-generation")

            outputs = pipe(data_list)
            outputs = pickle.dumps((outputs))
            conn.sendall(outputs)

            if not data:
                break





        


