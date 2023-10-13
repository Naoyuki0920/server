import os
import socket
import schedule
from time import sleep

def send_glb(glb_path, ip_addr, port):
    with open(glb_path, "rb") as f:
        glb_data = f.read()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_addr, port))

    sock.sendall(glb_data)
    sock.close()

if __name__ == "__main__":
    glb_path = "./static/image/1/Astronaut.glb"
    ip_addr = "192.168.75.131"
    port = 5000
    schedule.every(120).seconds.do(send_glb(glb_path, ip_addr, port))

    while True:
      schedule.run_pending()
      sleep(1)