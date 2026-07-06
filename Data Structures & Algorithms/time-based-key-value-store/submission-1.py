# upper bound binary search
# O(logn) time O(mn) space
class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map[key]
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        return arr[l - 1][1] if l != 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
