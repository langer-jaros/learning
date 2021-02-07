import sys

l = []

for idx, x in enumerate(sys.stdin):
    l.append(x)
    print(x)

print('---')

for idx, ll in enumerate(l):
    print(ll)
