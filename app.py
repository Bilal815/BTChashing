from hashlib import sha256
import time

MAX_NONCE = 100000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value: { nonce }")
            return new_hash
        
    raise BaseException(f"Couldn't find any bitcoin after trying { MAX_NONCE } times")


if __name__ == '__main__':
    transactions = '''
    Dhaval -> Bhavin = 20 BTC,
    Poofia -> Nanny = 1 BTC,
    Puffia -> Nani = 10 BTC,
    '''
    difficulty_level = 0
    start = time.time()
    print("Mining Started!")
    new_hash = mine(5, transactions, 'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78', difficulty_level);
    total_time = str(time.time() - start)
    print(f"Mining ended. Mining took: { total_time } seconds")
    print(new_hash)