import hashlib
import re

def process_block(ledger , stamp):
    combined = ledger + str(stamp)
    digest = hashlib.md5(combined.encode())

    return digest.hexdigest()

path = "C:\\Users\\ochen\\Documents\\GitHub\\CagChain\\blocks\\block-3.txt"
data = open(path, "r")
block = "".join(data.readlines()).strip()

stamp = 0

while not re.match("^000000" , process_block(block , stamp)):
    stamp = stamp + 1

print(stamp,process_block(block,stamp))