class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()

        senate = list(senate)
        for index, letter in enumerate(senate):
            if letter == 'R':
                R.append(index)
            else:
                D.append(index)

        
        while R and D:
            RTurn = R.popleft()
            DTurn = D.popleft()

            if RTurn > DTurn:
                D.append(DTurn + len(senate))
            else:
                R.append(RTurn + len(senate))
        
        return 'Radiant' if R else "Dire"