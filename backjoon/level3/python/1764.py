import sys

# input_lines = open(0).readlines()
n, k = map(int, sys.stdin.readline().rstrip().split())

first_hear = set()
first_see = set()
for _ in range(n):
    first_hear.add(sys.stdin.readline().rstrip())

for _ in range(k):
    first_see.add(sys.stdin.readline().rstrip())

first_hear.intersection_update(first_see)

print(len(first_hear))
for person in sorted(first_hear):
    print(person)


m,a,*b=open(0).read().split()
n=int(m)
d={*b[n:]}&{*b[:n]}
print(len(d),*sorted(d))