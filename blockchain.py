import hashlib 
import datetime
import random
import json

index = 0
transactions = []

# Creates a Block and return the Block    
def ablock():
    block = {
        'BlockIndex' : 123,
        'Timestamp': datetime.datetime.utcnow().timestamp(),
        'PrevHash' : '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',
        'Nonce' : 0,
        'Transactions': transactions,
    }
    return block

# This creates a transaction and adds it to the list of transactions
def transaction():
    transact = [str({
        'TransactionIndex' : index,
        'SenderAddress': hex(random.getrandbits(256)),
        'RecipientAddress': hex(random.getrandbits(256)),
        'Amount': random.getrandbits(4),
        'Message': 'testmessage',
    }),
    {'Signature': getHash()}
    ]
    return transact

# Creates a SHA-256 hash for a signature of the transactioin
def getHash():
    txn_time = json.dumps(datetime.datetime.utcnow().timestamp()).encode()
    return hashlib.sha256(txn_time).hexdigest()


while len(transactions) != 100:
    transactions.append(
        transaction()  
    )
    index += 1
    
print(ablock())
