import requests
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

#connection data

username = "SkillsUSA"
password = "Let'sLearnSomeSkills"
encryptKey = "5732987429837adf5afa3413fed43b1c5732987429837adf5afa3413fed43b1c"
InitVec = "2982749274329283074efeadc24342ef"
server = "http://10.129.38.229:3000/login"

#begin the real code!!!!

connection = requests.post(server, json={
  "username": username,
  "password": password
}
)
resJSON = json.loads(connection.text) 
msgBA = bytes.fromhex(resJSON["encryptedMessage"])
keyBA = bytes.fromhex(encryptKey)
vecBA = bytes.fromhex(InitVec)

cipher = AES.new(keyBA, AES.MODE_CBC, iv=vecBA)
original_data = unpad(cipher.decrypt(msgBA), AES.block_size).decode("UTF-8")

print(original_data)