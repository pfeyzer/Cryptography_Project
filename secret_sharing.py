import secrets

def share_value(bid, prime):
    share1 = secrets.randbelow(prime)
    share2 = secrets.randbelow(prime)
    share3 = (bid - share1 - share2) % prime
    return share1, share2, share3

def reconstruct(shares, prime):
    return sum(shares)% prime