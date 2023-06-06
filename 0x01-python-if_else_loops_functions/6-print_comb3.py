#!/usr/bin/python3
for d in range(0, 9):
    for (r) in range(d + 1, 10):
        if d == 8 and r == 9:
            print('{}{}'.format(d, r))
        else:
            print('{}{}'.format(d, r), end=', ')
