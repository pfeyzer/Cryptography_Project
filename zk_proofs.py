import hashlib

def generate_range_proof(bid, r, maxBid):
   #simple hash proof,  proof = H(bid || r || Bmax)

    if not (0 <= bid <= maxBid):
        return None  # invalid can't generate proof

    h = hashlib.sha256()
    h.update(str(bid).encode())
    h.update(str(r).encode())
    h.update(str(maxBid).encode())
    return h.hexdigest()

def verify_range_proof(bid, r, maxBid, proof):
    if not (0 <= bid <= maxBid):
        return False

    h =hashlib.sha256()
    h.update(str(bid).encode())
    h.update(str(r).encode())
    h.update(str(maxBid).encode())
    calc =h.hexdigest()

    return calc ==proof
