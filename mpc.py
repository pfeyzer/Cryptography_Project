import random

p = 2**127 - 1

def share_value(x, p=p):
    s1 = random.randrange(p)
    s2 = random.randrange(p)
    s3 = (x - s1 - s2) % p
    return s1, s2, s3

def reconstruct(shares, p=p):
    return sum(shares) % p

def signed(x, p=p):
    return x if x <= p//2 else x - p

def compare(a, b, p=p):
    diffs = []
    for i in range(3):
        diffs.append((a[i] - b[i]) % p)
        D = sum(diffs) % p
        D_signed = signed(D, p)
    if D_signed > 0:
        return 1
    if D_signed < 0:
        return -1
    return 0

def mpc_argmax(bidders, p=p):
    if not bidders:
        return None, None
    current_id, current_shares = bidders[0]
    for bidder_id, shares in bidders[1:]:
        if compare(shares, current_shares, p) == 1:
            current_id = bidder_id
            current_shares = shares
    return current_id, reconstruct(current_shares, p)
