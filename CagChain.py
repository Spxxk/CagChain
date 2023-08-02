import hashlib
import re

def process_block(ledger , stamp):
    combined = ledger + str(stamp)
    digest = hashlib.md5(combined.encode())

    return digest.hexdigest()

path = "C:\\Users\\ochen\\Documents\\GitHub\\CagChain\\blocks\\block1.txt"




stamp = 0

while not re.match("^0000" , process_block("test" , stamp)):
    stamp = stamp + 1
    
print(stamp)


