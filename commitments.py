from cryptography.hazmat.primitives.asymmetric import ec

curve = ec.SECP256R1()

def generate_commitment_params():
    g = ec.generate_private_key(curve).public_key()
    h = ec.generate_private_key(curve).public_key()
    return g, h

def commit_bid(bid, randomness, g, h):
    c1 = g.public_numbers().x * bid
    c2 = h.public_numbers().x * randomness
    return c1 + c2
