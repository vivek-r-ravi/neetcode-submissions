class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        pos_speed=[(a,(target-a)/b) for a,b in zip(position,speed)]
        pos_speed.sort(reverse=True,key=lambda x: x[0])
        stack=[]
        for i in range(n):
            if stack and stack[-1][1]>=pos_speed[i][1]:
                continue
            stack.append(pos_speed[i])
        return len(stack)
