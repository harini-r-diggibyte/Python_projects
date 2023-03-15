from collections import namedtuple

N = int(input())
total = 0
student = namedtuple('student', input().split())
for i in range(N):
    field1, field2, field3, field4 = input().split()
    s = student(field1, field2, field3, field4)
    total += int(s.MARKS)
    avg=total/N
print(format(avg,".2f"))