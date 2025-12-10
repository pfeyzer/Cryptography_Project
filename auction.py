from commitments import commit_bid, verify_commitment
from zk_proofs import generate_range_proof, verify_range_proof
from secret_sharing import share_value

class SimpleAuctionOrchestrator:
    def __init__(self, p=p, min_bid=100, max_bid=1000):
        self.p = p
        self.min_bid = min_bid
        self.max_bid = max_bid
        self.bidders = []
        self.server_storage = {1: {}, 2: {}, 3: {}}

    def register_bidder(bidder_id, bid, prime, max_bid, servers):
        # commitment
        commitment, randomness = commit_bid(bid)

        # range proof
        proof = generate_range_proof(bid, randomness, max_bid)

        # verify proof before accepting
        if not verify_range_proof(commitment, proof):
            print("Bidder", bidder_id, "rejected: invalid range proof")
            return False

        # secret sharing for the bid
        share1, share2, share3 = share_value(bid, prime)

        # send shares to servers
        servers[0].receive_share(bidder_id, share1)
        servers[1].receive_share(bidder_id, share2)
        servers[2].receive_share(bidder_id, share3)

        return True


    


    def run_auction(self):
        winner_id, winning_bid = mpc_argmax(self.bidders, self.p)
        return winner_id, winning_bid


if __name__ == "__main__":
    orch = SimpleAuctionOrchestrator()
    bids = [150, 920, 600]
    for i, b in enumerate(bids, start=1):
        shares = share_value(b)
        orch.register_bidder(i, b, shares)
        print("Example 1:", orch.run_auction())


    orch = SimpleAuctionOrchestrator()
    bids = [350, 350, 100, 300]
    for i, b in enumerate(bids, start=1):
        shares = share_value(b)
        orch.register_bidder(i, b, shares)
        print("Example 2:", orch.run_auction())


    orch = SimpleAuctionOrchestrator()
    bids = [10, 999, 300, 700, 2000]
    for i, b in enumerate(bids, start=1):
        shares = share_value(b)
        orch.register_bidder(i, b, shares)
        print("Example 3:", orch.run_auction())