class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        boats = 0
        l = 0
        r = len(people)-1

        while l <= r:
            if people[r] + people[r-1] <= limit:
                r -= 2
            elif people[r] + people[l] <= limit:
                r -= 1
                l += 1
            else:
                r -= 1
            boats += 1
        return boats
            
