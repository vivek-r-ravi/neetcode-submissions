# user ID hash map with list values for tweets and with hash set values for followers
# O(1) time for init, follow, unfollow, postTweet; O()
class Twitter:
    def __init__(self):
        self.users_tweets = defaultdict(list)
        self.users_followers = defaultdict(set)
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users_tweets[userId].append((self.tweet_count, tweetId))
        self.tweet_count+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        max_heap = []
        self.users_followers[userId].add(userId)
        for user in self.users_followers[userId]:
            if self.users_tweets[user]:
                heapq.heappush_max(
                    max_heap, (self.users_tweets[user][-1][0], user, len(self.users_tweets[user])-1, self.users_tweets[user][-1][1])
                )
        while len(out) < 10 and max_heap:
            _, user, idx, tweetId = heapq.heappop_max(max_heap)
            out.append(tweetId)
            idx-=1
            if idx>=0:
                heapq.heappush_max(
                    max_heap, (self.users_tweets[user][idx][0], user, idx, self.users_tweets[user][idx][1])
                )
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users_followers[followerId].discard(followeeId)
