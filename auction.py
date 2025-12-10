class SimpleAuctionOrchestrator:
    def __init__(self, p=p, min_bid=100, max_bid=1000):
        self.p = p
        self.min_bid = min_bid
        self.max_bid = max_bid
        self.bidders = []
        self.server_storage = {1: {}, 2: {}, 3: {}}


    


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