from time import time
import hashlib
import json

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transations = [],
        self.transaction_history = []

        self.new_block(previous_hash="the times",proof=100)
    def new_block(self,proof,previous_hash=None):
        block = {
            "index" : len(self.chain) +1,
            "timestamp": time(),
            "transactions": time(),
            "proof":proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),

        }

        self.pending_transations = []
        self.chain.append(block)

        return block
    @property
    def last_block(self):
            return self.chain[-1]
        
    def new_transaction(self,sender,recipient,amount):
            transaction = {
                "sender": sender,
                "recipient": recipient,
                "amount": amount
            }

            self.pending_transations.append(transaction)
            self.transaction_history.append(transaction)
            return self.last_block["index"]+1

    def hash(self,block):
            string_object = json.dumps(block,sort_keys=True)
            block_string = string_object.encode()

            raw_hash = hashlib.sha256(block_string)
            hex_hash = raw_hash.hexdigest()

            return hex_hash

blockchain =  Blockchain()

t1 = blockchain.new_transaction("camp","daniel","2 cardano")
t1 = blockchain.new_transaction("smith","jeff","1 btc")
blockchain.new_block(12345)


