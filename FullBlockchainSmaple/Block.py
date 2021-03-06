from time import time
import hashlib
import json

class Block(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new Block and adds it to the chain
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    @property
    def last_block(self):
     # Returns the last Block in the chain
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Hashes a Block
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
