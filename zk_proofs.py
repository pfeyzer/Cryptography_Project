import hashlib

def generate_range_proof(bid, randomness, maxBid, commitment):
    if not (0 <= bid <= maxBid):
        return None
    h = hashlib.sha256()
    h.update(str(bid).encode())
    h.update(str(randomness).encode())
    h.update(str(maxBid).encode())
    h.update(str(commitment).encode())
    return h.hexdigest()

def verify_range_proof(bid, randomness, maxBid, commitment, proof):
    if not (0 <= bid <= maxBid):
        return False
    h = hashlib.sha256()
    h.update(str(bid).encode())
    h.update(str(randomness).encode())
    h.update(str(maxBid).encode())
    h.update(str(commitment).encode())
    calc = h.hexdigest()
    return calc == proof
