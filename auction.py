from commitments import commit_bid, generate_commitment_params
from zk_proofs import generate_range_proof, verify_range_proof
from secret_sharing import share_value
from mpc import mpc_argmax

class Server:
    def __init__(self):
        self.shares = {}

    def receive_share(self, bidder_id, share):
        self.shares[bidder_id] = share

def register_bidder(bidder_id, bid, prime, max_bid, g, h, servers):
    randomness = 123456789  # deterministic for testing
    commitment = commit_bid(bid, randomness, g, h)

    proof = generate_range_proof(bid, randomness, max_bid, commitment)

    if not verify_range_proof(bid, randomness, max_bid, commitment, proof):
        print("Bidder", bidder_id, "rejected")
        return False

    s1, s2, s3 = share_value(bid, prime)
    servers[0].receive_share(bidder_id, s1)
    servers[1].receive_share(bidder_id, s2)
    servers[2].receive_share(bidder_id, s3)

    return True

def run_auction(bidders, prime):
    return mpc_argmax(bidders, prime)

if __name__ == "__main__":
    prime = 2**127 - 1
    max_bid = 50000

    print("\n=== Generating Commitment Parameters ===")
    g, h = generate_commitment_params()

    servers = [Server(), Server(), Server()]

    bids = [-11, -4, -3]
    bidders = []

    print("\n=== Registering Bidders ===")
    for i, b in enumerate(bids, start=1):
        print(f"\nBidder {i}: submitting bid = {b}")

        ok = register_bidder(i, b, prime, max_bid, g, h, servers)
        if not ok:
            print(f"Bidder {i} rejected")
            continue

        shares = (
            servers[0].shares[i],
            servers[1].shares[i],
            servers[2].shares[i]
        )
        bidders.append((i, shares))

        print("  Shares distributed:")
        print(f"    S1: {shares[0]}")
        print(f"    S2: {shares[1]}")
        print(f"    S3: {shares[2]}")

    print("\n=== Server Share Tables ===")
    for i, s in enumerate(servers, start=1):
        print(f"Server {i}: {s.shares}")

    print("\n=== Running MPC Argmax ===")
    winner_id, winning_bid = run_auction(bidders, prime)

    print("\n=== Auction Result ===")
    print(f"Winner ID: {winner_id}")
    print(f"Winning Bid (reconstructed): {winning_bid}")
    print("\n=== End of Auction ===\n")
