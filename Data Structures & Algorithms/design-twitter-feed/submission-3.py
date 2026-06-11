class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        stack = []
        if userId not in self.follows[userId]:
            self.follows[userId].add(userId)
        for follow in self.follows[userId]:
            stack +=  self.posts[follow]
        stack = stack
        heapq.heapify(stack)
        result = []
        while stack and len(result) != 10:
            result.append(heapq.heappop(stack)[1])
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
