from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
# use an ec curve
curve =ec.SECP256R1()

def generate_commitment_params():
    private_key =ec.generate_private_key(curve)
    g =private_key.public_key()                     #base point
    h =ec.generate_private_key(curve).public_key()  #second generator
    return g, h

def commit_bid(bid, randomness, g, h):
    #pedersen commitment: c = bg + rh

    c1 =g.public_numbers().x *bid
    c2 =h.public_numbers().x *randomness
    return (c1 +c2)

def verify_commitment(c, bid, randomness, g, h):
    calc =commit_bid(bid, randomness, g, h)
    return calc ==c

