from collections import deque, Counter


# solution 1: brute force simulation with a queue O(n2) time and O(n) space
class SolutionV1:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        while len(students) > 0 and sandwiches[0] in students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students[0])
                students.popleft()
        return len(students)


# solution 2: efficient solution using counting O(n) time and O(1) space
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = Counter(students)
        for s in sandwiches:
            if student_count[s] > 0:
                student_count[s] -= 1
            else:
                return sum(student_count.values())
        return 0