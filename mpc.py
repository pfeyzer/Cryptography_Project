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


def mpc_add(a, b, p=p):
    return [(a[i] + b[i]) % p for i in range(3)]


def mpc_sub(a, b, p=p):
    return [(a[i] - b[i]) % p for i in range(3)]


def mpc_mult(a, b, p=p):
    A = reconstruct(a, p)
    B = reconstruct(b, p)
    prod = (A * B) % p
    return share_value(prod, p)


def compute_difference_share(ai, bi, p=p):
    return (ai - bi) % p


def reconstruct_difference(diffs, p=p):
    return sum(diffs) % p


def compare(a, b, p=p):
    diffs = []
    for i in range(3):
        diffs.append(compute_difference_share(a[i], b[i], p))
        D = reconstruct_difference(diffs, p)
        D_signed = signed(D, p)
    if D_signed > 0:
        return 1
    elif D_signed < 0:
        return -1
    else:
        return 0


def mpc_argmax(bidders, p=p):
    if not bidders:
        return None, None
    current_id = bidders[0][0]
    current_shares = bidders[0][1]
    for bidder_id, shares in bidders[1:]:
        c = compare(shares, current_shares, p)
    if c == 1:
        current_id = bidder_id
        current_shares = shares
        winning_bid = reconstruct(current_shares, p)
        return current_id, winning_bid