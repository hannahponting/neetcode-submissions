class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand = defaultdict(int)

        for b in bills:
            if b == 10:
                if hand[5] > 0:
                    hand[5] -= 1
                else:
                    return False
            if b == 20:
                if (hand[10] > 0  and hand[5] > 0):
                    hand[10] -= 1
                    hand[5] -= 1
                elif hand[5] > 2:
                    hand[5] -= 3
                else:
                    return False
            hand[b] += 1
            print(hand)
        return True
