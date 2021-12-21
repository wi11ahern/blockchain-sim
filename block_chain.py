import time
from typing import List
from block import Block


class Blockchain:
    _proof_of_work_difficulty = 5

    def __init__(self):
        self.chain: List[Block] = []
        self._create_genesis_block()

    @property
    def last_block(self):
        return self.chain[-1]

    def _create_genesis_block(self):
        genesis_block = Block(
            index=0,
            timestamp=time.time(),
            previous_hash="",
            nonce=0,
        )
        self.chain.append(genesis_block)
        print(f"Genesis Block:\n{genesis_block}")
        print(f"Hash:\n{genesis_block.calculate_hash()}\n")

    def mine_blocks(self):
        new_block = Block(
            index=self.last_block.index + 1,
            timestamp=time.time(),
            previous_hash=self.last_block.calculate_hash(),
            nonce=self.last_block.nonce + 1,
        )

        proof = self.get_proof_of_work(new_block)
        self.add_block(new_block, proof)
        return new_block.index

    def get_proof_of_work(self, block: Block):
        calculated_hash = block.calculate_hash()

        while not calculated_hash.startswith('0' * self._proof_of_work_difficulty):
            block.nonce += 1
            calculated_hash = block.calculate_hash()

        return calculated_hash

    def add_block(self, block: Block, proof: str):
        previous_hash = self.last_block.calculate_hash()
        if previous_hash != block.previous_hash:
            return False

        if not self.validate_proof(block, proof):
            return False

        self.chain.append(block)
        print(f"New Block:\n{block}")
        print(f"Hash:\n{block.calculate_hash()}\n")

        return True

    def validate_proof(self, block: Block, block_hash):
        return block_hash.startswith('0' * self._proof_of_work_difficulty) and block_hash == block.calculate_hash()

