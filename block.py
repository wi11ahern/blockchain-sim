import json
import time
from hashlib import sha256


class Block:
    def __init__(self, index: int, timestamp: time, previous_hash: str, nonce: int):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=4)

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

