from commitments import commit_bid, verify_commitment
from zkproofs import generate_range_proof, verify_range_proof
from secretsharing import share_value

def register_bidder(bidder_id, bid, prime, max_bid, servers):
    # commitment
    commitment, randomness = commit_bid(bid)

    # range proof
    proof = generate_range_proof(bid, randomness, max_bid)

    # verify proof before accepting
    if not verify_range_proof(commitment, proof):
        print("Bidder", bidder_id, "rejected: invalid range proof")
        return false

    # secret sharing for the bid
    share1, share2, share3 = share_value(bid, prime)

    # send shares to servers
    servers[0].receive_share(bidder_id, share1)
    servers[1].receive_share(bidder_id, share2)
    servers[2].receive_share(bidder_id, share3)

    return True

def run_auction():
