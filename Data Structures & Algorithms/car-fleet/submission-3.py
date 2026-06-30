# monotonic stack (after sorting by pos + calculating time to reach target)
# O(nlogn) time and O(n) space
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, (target - pos) / sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        for pos, time in cars:
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)


# use last time variable (after sorting by pos + calculating time to reach target)
# O(nlogn) time and O(n) space
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, (target - pos) / sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse=True)
        fleet_time = 0
        fleet_count = 0
        for pos, time in cars:
            if fleet_time >= time:
                continue
            fleet_time = time
            fleet_count += 1
        return fleet_count