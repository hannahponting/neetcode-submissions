class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        heap = []
        users = self.following[userId] | {userId}
        for user in users:
            tweets = self.tweets[user]
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, idx - 1)
                )
        res = []
        while heap and len(res) < 10:
            neg_time, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                time, nextTweetId = self.tweets[user][idx]
                heapq.heappush(
                    heap,
                    (-time, nextTweetId, user, idx - 1)
                )
        return res

    def follow(self, followerId: int, followeeId: int):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        self.following[followerId].discard(followeeId)