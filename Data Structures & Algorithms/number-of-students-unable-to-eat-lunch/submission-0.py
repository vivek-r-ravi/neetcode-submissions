from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        while len(students)>0 and sandwiches[0] in students:
            if students[0]==sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students[0])
                students.popleft()

        return len(students)