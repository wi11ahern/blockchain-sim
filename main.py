from block_chain import Blockchain


def main():
    block_chain = Blockchain()
    for i in range(999_999_999):
        block_chain.mine_blocks()
        print(f"Length of block chain: {len(block_chain.chain)}")


if __name__ == '__main__':
    main()


