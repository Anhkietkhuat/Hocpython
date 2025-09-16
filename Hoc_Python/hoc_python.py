import struct
import serial
import json
import base64
from Crypto.Cipher import AES
# ser = serial.Serial("COM5", 115200)
while True:
    with open("data.txt","r", encoding="utf8") as f:
        for line in f:
            print(line.strip("\n")) #bo xuong dong thua

