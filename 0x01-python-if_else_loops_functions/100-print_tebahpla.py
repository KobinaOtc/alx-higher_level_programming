#!/usr/bin/python3
for j in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(j) if j % 2 == 0 else chr(j-32), end='')
