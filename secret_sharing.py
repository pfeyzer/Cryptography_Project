import secrets

def share_value(bid, prime):
    s1 = secrets.randbelow(prime)
    s2 = secrets.randbelow(prime)
    s3 = (bid - s1 - s2) % prime
    return s1, s2, s3
