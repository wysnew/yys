from flask import Flask
import requests
from time import time
import hashlib
import json
import sys

chain = []
transactions = []

def createHash(content):
content_encoded = json.dumps(content, sort_keys=True).encode()
return hashlib.sha256(content_encoded).hexdigest()
    
 def createBlock(transactions, nonce, prevHash):
     index = len(chain)
     timestamp = time()
     create_block = f'{index}{timestamp}{nonce}{prevHash}'
     hash = createHash(content_block)
     
block = {
    "index" : index,
    "timestamp" : timestamp,
    "transactions" : transactions,
    "nonce" : nonce,
    "prevHash" : prevHash,
    "hash" : hash,
    "mined" : False
}

return hash, chain.append(block)

#genesis block
createBlock([], 0, 64*"0")

app = Flask(__name__)
@app.route( '/blockchain', methods = ['GET'])

def full_chain():
    response = {
        'chain' = chain
    }