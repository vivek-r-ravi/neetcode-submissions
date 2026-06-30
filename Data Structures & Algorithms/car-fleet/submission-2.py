class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        cars=[(a,(target-a)/b) for a,b in zip(position,speed)]
        cars.sort(reverse=True)
        stack=[]
        for i in range(n):
            if stack and stack[-1]>=cars[i][1]:
                continue
            stack.append(cars[i][1])
        return len(stack)
