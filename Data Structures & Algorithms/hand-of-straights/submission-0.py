class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counts = Counter(hand)
        hand = sorted(hand)

        for i in hand:
            if counts[i]:
                for j in range(i, i+groupSize):
                    if not counts[j]:
                        return False
                    counts[j] -= 1
        return True
                