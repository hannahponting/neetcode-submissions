class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = sorted(people)

        l = 0
        r = len(people)-1
        boats = 0

        while l <= r:
            current = people[r]
            r -= 1
            if current + people[l] <= limit:
                l  += 1
            boats += 1
        
        return boats