class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        boats = 0
        l =0
        r = len(people)-1

        while l <= r:
            boat = people[r]
            if boat + people[l] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats