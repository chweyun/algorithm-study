import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

print(1 if s*len(t) == t*len(s) else 0)